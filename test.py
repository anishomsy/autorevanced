from autorevanced.util import build, get_files, get_apk


files = get_files()
print(files)
apk = get_apk("youtube")
print(apk)
file = build(apk, files)

print(file[0])
print(f"file location: {file[1]}")
