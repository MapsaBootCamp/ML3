import zipfile
import requests
import sys
from pathlib import Path

url = "https://s3.amazonaws.com/keras-datasets/jena_climate_2009_2016.csv.zip"
save_path = "jena_climate_2009_2016.csv.zip"


def download_url(url, save_path, chunk_size=512):
    print(f"Downloading to {save_path}....")
    response = requests.get(url, stream=True)
    total_length = int(response.headers.get('content-length'))
    dl = 0
    with open(Path("data") / save_path, 'wb') as fd:
        for chunk in response.iter_content(chunk_size=chunk_size):
            if chunk:
                fd.write(chunk)
                dl += len(chunk)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)))
                sys.stdout.flush()
    print("\n download completed :)\n")


def unzip(path_to_zip, directory_to_extract):
    print("start extracting....")
    with zipfile.ZipFile(path_to_zip, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract)

    print("extracted!")


if not Path("data").is_dir():
    Path("data").mkdir(parents=True, exist_ok=True)

path = Path("data") / save_path

if not path.is_file():
    download_url(url, save_path)
    unzip(path, Path("data"))
else:
    print("data exist!")
