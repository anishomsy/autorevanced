# AutoReVanced

AutoReVanced is a Python script designed to automate the process of downloading and patching APKs (Android application packages) with ReVanced patches. This tool simplifies the process of fetching the necessary files, downloading the desired APK, and applying patches to create a customized APK.

## Features

- Automatically download the latest ReVanced patches, integrations, and CLI tools.
- Download APKs directly from ApkPure.
- Apply ReVanced patches to the downloaded APK.
- Supports custom package names and versions.

## Requirements

- Python 3.6 or higher
- Requests library
- tqdm library
- apkpure library
- Java Runtime Environment (JRE)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/anishomsy/autorevanced.git
   cd autorevanced
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

4. Ensure that Java is installed on your system and is available in your PATH.

## Usage

To use AutoReVanced, you can run the `index.py` script to automatically build YouTube ReVanced:

```bash
python index.py
```

This will download and patch the YouTube APK with the latest ReVanced patches.

Alternatively, you can call the autorevanced function with the name of the desired APK. By default, it targets the YouTube app.

Example:

```python
from autorevanced.util import autorevanced

output = autorevanced("youtube")
print(output)
```

### Functions

#### `autorevanced(name: str = "youtube") -> str`

Main function to automate the process of downloading and patching an APK.

- `name`: The name of the application to download and patch. Default is "youtube".

#### `get_files() -> list`

Fetches the latest ReVanced patches, integrations, and CLI tools.

#### `get_apk(name: str = "com.google.android.youtube", version: str = "Latest") -> str`

Downloads the specified APK from ApkPure.

- `name`: The package name of the APK. Default is "com.google.android.youtube".
- `version`: The version of the APK to download. Default is "Latest".

#### `build(apk: str, revanced_files: list) -> str`

Applies ReVanced patches to the specified APK.

- `apk`: The path to the APK file.
- `revanced_files`: A list of paths to the ReVanced patch files.

#### `downloader(url: str) -> str`

Downloads a file from the specified URL and returns the local file path.

- `url`: The URL of the file to download.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [ReVanced](https://revanced.app/) for providing the patches and tools.
- [ApkPure](https://apkpure.com/) for providing access to APKs.
