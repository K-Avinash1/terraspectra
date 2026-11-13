"""Download the numbered tomato cubes from Zenodo and verify their MD5 checksums.
Safe to re-run: files that are already downloaded and verified are skipped."""
import hashlib
import json
import shutil
import urllib.request
from pathlib import Path

RECORD_ID = "15800414"
API_URL = f"https://zenodo.org/api/records/{RECORD_ID}"
DEST = Path("data/raw/tomato_hsi")
PREFIXES = ("Healthy_", "Alternaria_alternata_", "Alternaria_solani_",
            "Botrytis_cinerea_", "Fusarium_oxysporum_")


def md5_of(path):
    digest = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def download(url, target):
    request = urllib.request.Request(url, headers={"User-Agent": "terraspectra-student-project"})
    tmp = target.with_suffix(".part")
    with urllib.request.urlopen(request) as response, open(tmp, "wb") as out:
        shutil.copyfileobj(response, out, length=1024 * 1024)
    tmp.replace(target)


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    request = urllib.request.Request(API_URL, headers={"User-Agent": "terraspectra-student-project"})
    with urllib.request.urlopen(request) as response:
        record = json.load(response)
    entries = [e for e in record.get("files", [])
               if e["key"].endswith(".mat") and not e["key"].endswith("_features.mat")
               and e["key"].startswith(PREFIXES)]
    print(f"Found {len(entries)} cube files on the record")
    for entry in sorted(entries, key=lambda e: e["key"]):
        name = entry["key"]
        target = DEST / name
        expected = entry.get("checksum", "").replace("md5:", "")
        if target.exists() and expected and md5_of(target) == expected:
            print(f"{name}: already OK")
            continue
        print(f"{name}: downloading...")
        download(f"https://zenodo.org/records/{RECORD_ID}/files/{name}?download=1", target)
        if expected:
            status = "OK" if md5_of(target) == expected else "MISMATCH (delete and re-run)"
        else:
            status = "downloaded (no checksum available to verify)"
        print(f"{name}: {status}")


if __name__ == "__main__":
    main()
