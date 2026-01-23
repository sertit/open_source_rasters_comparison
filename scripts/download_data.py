import requests
import zipfile
from pathlib import Path

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

URL="https://seafile.unistra.fr/f/64a60dc6200744d99aef/?dl=1"
ZIP_PATH = DATA_DIR / "geodata.zip"

print("Downloading data from Seafile...")
r = requests.get(URL, stream=True)
r.raise_for_status()

with open(ZIP_PATH, "wb") as f:
    for chunk in r.iter_content(chunk_size=8192):
        f.write(chunk)

print("Unzipping folders...")
with zipfile.ZipFile(ZIP_PATH, "r") as z:
    z.extractall(DATA_DIR)

ZIP_PATH.unlink()

print("Data ready to be used!")