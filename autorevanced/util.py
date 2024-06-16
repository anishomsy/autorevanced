import json
import os
import subprocess
import requests
from tqdm import tqdm
from apkpure.apkpure import ApkPure
import re


def autorevanced(name: str = "youtube"):
    revanced_files = get_files()
    apk = get_apk(name)
    output = build(apk, revanced_files)
    return output


def get_files():
    # Loop through the urls and get the files
    urls = [
        "https://api.revanced.app/v2/revanced-patches/releases/latest",
        "https://api.revanced.app/v2/revanced-integrations/releases/latest",
        "https://api.revanced.app/v2/revanced-cli/releases/latest",
    ]
    files = []

    for url in urls:
        res = requests.get(url).json()
        assets = res["release"]["assets"]
        # for i in range(len(downloads) - 1):
        #     name = downloads[i]["name"]
        #     print(f"Downloading: {name}")
        #     downloader(downloads[i]["browser_download_url"], name)
        for asset in assets[:-1]:
            dl_url = asset["browser_download_url"]
            path = downloader(dl_url)
            if not path:
                return None
            files.append(path)

    return files


def get_apk(name: str = "com.google.android.youtube", version: str = "Latest"):
    # get the apk from apkpure
    package_name = name
    api = ApkPure()
    info = ""
    if not name == "com.google.android.youtube":
        info = json.loads(api.get_info(name=name))

        package_name = info["package_name"]

    with open("./revanced-files/patches.json") as jdata:
        data = json.load(jdata)

    # get the current recommended revanced version. This need to be improved
    compatable_versions = []
    for item in data:
        if (
            item["name"] == "Spoof client"
            and item["compatiblePackages"][0]["name"] == package_name
        ):
            compatable_versions = item["compatiblePackages"][0]["versions"]
            break
    # Get the apk
    if not version == "Latest":
        if version in compatable_versions:
            return api.download(package_name, version)
    file_path = api.download(package_name, compatable_versions[-1])

    return file_path


def build(apk="", revanced_files=[]):
    if apk == "":
        raise Exception("Please provide an apk!")
    if len(revanced_files) != 4:
        raise Exception("There was an error with revanced files!")
    path = os.getcwd()
    filename = os.path.basename(apk)

    filename = "revanced_" + filename
    output = os.path.join(path, f"output/{filename}")
    os.makedirs(os.path.dirname(output), exist_ok=True)
    err_code = subprocess.run(
        [
            f"cd {path} && java -jar {revanced_files[-1]} patch {apk} -b {revanced_files[1]} -m {revanced_files[2]} -o {output}"
        ],
        capture_output=True,
        text=True,
        check=False,
        shell=True,
    )
    if err_code.returncode != 0:
        raise Exception(err_code.stderr)

    return err_code.stdout


def downloader(url: str) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
    }

    r = requests.get(url, stream=True, allow_redirects=True, headers=headers)

    d = r.headers["content-disposition"]

    fname = re.findall("filename=(.+)", d)[0].strip('"')
    print(f"Downloading {fname}")

    fname = os.path.join(os.getcwd(), f"revanced-files/{fname}")

    os.makedirs(os.path.dirname(fname), exist_ok=True)

    if os.path.exists(fname):
        if int(r.headers.get("content-length", 0)) == os.path.getsize(fname):
            print("File Exists!")
            return os.path.realpath(fname)

    with tqdm.wrapattr(
        open(fname, "wb"),
        "write",
        miniters=1,
        total=int(r.headers.get("content-length", 0)),
    ) as file:
        for chunk in r.iter_content(chunk_size=4 * 1024):
            if chunk:
                file.write(chunk)
    print("Download Complete!")
    return os.path.realpath(fname)
