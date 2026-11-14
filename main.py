"""news-image-01 entry: copy the repo-held image to the output directory.

The image (entry.png) sums up the world's news of Friday 13 November 2026
in one editorial front page: six illustrated stories plus an "Also today"
strip. This is the post-opening rebuild: all six panels were generated
fresh after the competition opened, and all wording was overlaid afterwards
so every label is spelled correctly and legible.

The program only copies bytes, so both runs write identical output.
"""
import hashlib
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def _sha256(path):
    """Return the hex SHA-256 digest of a file, read in fixed-size chunks."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    """Copy the repo-held image to the output directory (byte for byte)."""
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    dest = OUT_DIR / "entry.png"
    shutil.copyfile(SRC, dest)
    if _sha256(SRC) != _sha256(dest):
        raise SystemExit("entry.png copy failed integrity check: hashes differ")


if __name__ == "__main__":
    main()
