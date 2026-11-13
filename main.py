"""news-image-01 entry: copy the repo-held image to the output directory.

The image (entry.png) sums up the world's news of Friday 13 November 2026
in one editorial front page: six illustrated stories plus an "Also today"
strip. This is the post-opening rebuild: all six panels were generated
fresh after the competition opened, and all wording was overlaid afterwards
so every label is spelled correctly and legible.

The program only copies bytes, so both runs write identical output.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    """Copy the repo-held image to the output directory (byte for byte)."""
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, OUT_DIR / "entry.png")


if __name__ == "__main__":
    main()
