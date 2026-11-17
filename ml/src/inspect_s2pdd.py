"""Inspect unpacked S2-PDD files: folder layout, one NPZ tile, label statistics."""
import sys
from collections import Counter
from pathlib import Path

import numpy as np

root = Path(sys.argv[1] if len(sys.argv) > 1 else "data/raw/s2pdd")

for sub in sorted(p for p in root.iterdir() if p.is_dir()):
    files = [f for f in sub.rglob("*") if f.is_file()]
    print(f"{sub.name}: {len(files)} files, e.g. {[f.name for f in files[:3]]}")

npz_files = sorted(root.rglob("*.npz"))
if npz_files:
    print(f"\nFirst tile: {npz_files[0]}")
    with np.load(npz_files[0]) as data:
        for key in data.files:
            arr = data[key]
            print(f"  {key}: shape={arr.shape} dtype={arr.dtype} min={arr.min():.4g} max={arr.max():.4g}")

counts = Counter()
boxes = 0
txt_files = sorted((root / "labels").rglob("*.txt"))
for file in txt_files:
    for line in file.read_text().splitlines():
        if line.strip():
            counts[line.split()[0]] += 1
            boxes += 1
print(f"\nLabel files: {len(txt_files)}, total boxes: {boxes}, per class_id: {dict(counts)}")
