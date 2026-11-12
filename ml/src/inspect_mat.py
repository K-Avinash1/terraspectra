"""Print the structure of a .mat file without loading it fully into RAM."""
import sys
from pathlib import Path


def inspect_scipy(path):
    from scipy.io import whosmat

    for name, shape, kind in whosmat(path):
        print(f"{name}: shape={shape} class={kind}")


def inspect_h5(path):
    import h5py

    with h5py.File(path, "r") as f:

        def visit(name, obj):
            if isinstance(obj, h5py.Dataset):
                print(f"{name}: shape={obj.shape} dtype={obj.dtype}")

        f.visititems(visit)


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: python ml/src/inspect_mat.py <file.mat>")
    path = Path(sys.argv[1])
    print(f"File: {path} ({path.stat().st_size / 1e6:.1f} MB)")
    try:
        inspect_scipy(path)
    except NotImplementedError:
        print("v7.3 (HDF5) file detected, reading structure with h5py")
        inspect_h5(path)


if __name__ == "__main__":
    main()
