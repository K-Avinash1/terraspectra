"""List the variable names and shapes inside every .mat file of a folder."""
import sys
from pathlib import Path

from scipy.io import whosmat

folder = Path(sys.argv[1] if len(sys.argv) > 1 else "data/raw/tomato_hsi")
for file in sorted(folder.glob("*.mat")):
    info = whosmat(file)
    print(file.name, "->", [(name, shape) for name, shape, _ in info])
