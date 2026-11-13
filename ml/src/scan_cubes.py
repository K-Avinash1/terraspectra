"""Scan every numbered cube and report value ranges, saved to docs/cube_stats.csv."""
import csv
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy.io import loadmat, whosmat

folder = Path(sys.argv[1] if len(sys.argv) > 1 else "data/raw/tomato_hsi")
header = ["file", "variable", "shape", "min", "max", "mean", "share_at_max", "scale_guess"]
rows = []
for file in sorted(folder.glob("*.mat")):
    if file.name.endswith("_features.mat"):
        continue
    name = whosmat(file)[0][0]
    cube = loadmat(file, variable_names=[name])[name].astype(np.float32)
    vmax = float(cube.max())
    kind = "reflectance-like" if vmax <= 2.0 else "raw-counts-like"
    at_max = float((cube >= vmax).mean())
    row = [file.stem, name, "x".join(map(str, cube.shape)), f"{cube.min():.4f}",
           f"{vmax:.4f}", f"{cube.mean():.4f}", f"{at_max:.4%}", kind]
    rows.append(row)
    print(" | ".join(row))
    del cube

out = Path("docs/cube_stats.csv")
with open(out, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

summary = defaultdict(lambda: defaultdict(int))
for row in rows:
    summary[row[0].rsplit("_", 1)[0]][row[-1]] += 1
print("\nSummary per class:")
for cls, counts in summary.items():
    print(cls, dict(counts))
print(f"Saved: {out}")
