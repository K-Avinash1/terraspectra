"""Find cubes that are identical (or flipped copies) under different file names."""
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy.io import loadmat, whosmat

folder = Path(sys.argv[1] if len(sys.argv) > 1 else "data/raw/tomato_hsi")
files = [f for f in sorted(folder.glob("*.mat")) if not f.name.endswith("_features.mat")]


def load(file):
    name = whosmat(file)[0][0]
    return loadmat(file, variable_names=[name])[name].astype(np.float32)


groups = defaultdict(list)
for file in files:
    cube = load(file)
    groups[(round(float(cube.max()), 3), round(float(cube.mean()), 3))].append(file)
    del cube

for members in groups.values():
    for i in range(len(members)):
        for j in range(i + 1, len(members)):
            a, b = load(members[i]), load(members[j])
            if np.array_equal(a, b):
                verdict = "IDENTICAL"
            elif (np.array_equal(a, b[::-1]) or np.array_equal(a, b[:, ::-1])
                  or np.array_equal(a, b[::-1, ::-1])):
                verdict = "FLIPPED COPY"
            else:
                verdict = f"same statistics, different data (max diff {float(np.abs(a - b).max()):.4g})"
            print(f"{members[i].stem}  vs  {members[j].stem}: {verdict}")
print("Done")
