"""Sanity-check one hyperspectral cube from the Javidan tomato dataset.

Prints basic statistics, estimates how much of the image is leaf, and saves a
figure (pseudo-RGB + mean spectra) to docs/figures/.
NOTE: the .mat file stores no wavelength vector. We assume the bands span
400-950 nm evenly (the range stated in the paper). This is an assumption.
"""
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import loadmat, whosmat

WL_START, WL_END = 400.0, 950.0


def nearest(wl, target):
    return int(np.argmin(np.abs(wl - target)))


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: python ml/src/check_cube.py <file.mat>")
    path = Path(sys.argv[1])
    name = whosmat(path)[0][0]
    cube = loadmat(path, variable_names=[name])[name].astype(np.float32)
    h, w, b = cube.shape
    wl = np.linspace(WL_START, WL_END, b)

    print(f"{path.name}: variable={name} shape={cube.shape} (assuming last axis = bands)")
    print(f"min={cube.min():.4f} max={cube.max():.4f} mean={cube.mean():.4f}")
    print(f"NaN values: {int(np.isnan(cube).sum())}")
    print(f"all-zero pixels: {(cube == 0).all(axis=2).mean():.1%}")

    red = cube[:, :, nearest(wl, 670)]
    nir = cube[:, :, nearest(wl, 800)]
    ndvi = (nir - red) / (nir + red + 1e-6)
    leaf = ndvi > 0.3
    print(f"pixels with NDVI > 0.3 (approx. leaf): {leaf.mean():.1%}")

    rgb = np.stack([cube[:, :, nearest(wl, t)] for t in (640, 550, 460)], axis=2)
    rgb = np.clip(rgb / (np.percentile(rgb, 99) + 1e-6), 0, 1)

    fig, axes = plt.subplots(1, 2, figsize=(11, 4))
    axes[0].imshow(rgb)
    axes[0].set_title("Pseudo-RGB (640/550/460 nm, assumed)")
    axes[0].axis("off")
    if leaf.any():
        axes[1].plot(wl, cube[leaf].mean(axis=0), label="leaf (NDVI>0.3)")
    if (~leaf).any():
        axes[1].plot(wl, cube[~leaf].mean(axis=0), label="other pixels")
    axes[1].set_xlabel("Wavelength (nm, assumed)")
    axes[1].set_ylabel("Mean value")
    axes[1].legend()
    fig.tight_layout()
    out = Path("docs/figures") / f"{path.stem}_check.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, dpi=120)
    print(f"Saved figure: {out}")


if __name__ == "__main__":
    main()
