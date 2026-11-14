#!/usr/bin/env python3
"""news-image-01 entrypoint.

Copies the repo's entry.png — a newspaper front page built from 6 panels
plus a footer — to /output/entry.png, then verifies the copy byte-for-byte
by comparing its SHA-256 digest against the expected value.

Standard library only. Deterministic: every run writes the same bytes.
"""

import hashlib
import os
import shutil
import sys

EXPECTED_SHA256 = "1f8150b52a4a9d4d205964d1b58fb96f4b0594847e8d5aa4765d5bedf141227c"
SOURCE_NAME = "entry.png"


def sha256_file(path):
    """Return the hex SHA-256 digest of the file at path."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


MAX_BYTES = 1024 * 1024
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def read_png_dimensions(path):
    """Return (width, height) parsed from the PNG IHDR chunk (stdlib only)."""
    import struct

    with open(path, "rb") as handle:
        header = handle.read(33)
    if len(header) < 33 or header[:8] != PNG_SIGNATURE:
        raise ValueError("not a PNG file")
    if header[12:16] != b"IHDR":
        raise ValueError("missing PNG IHDR chunk")
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def validate_output(path):
    """Check the written image meets the competition limits.

    Returns (size, width, height); raises OSError or ValueError on failure.
    """
    size = os.path.getsize(path)
    if size > MAX_BYTES:
        raise ValueError(f"output too large: {size} bytes (limit {MAX_BYTES})")
    width, height = read_png_dimensions(path)
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        raise ValueError(
            f"unexpected dimensions: {width}x{height} "
            f"(expected {EXPECTED_WIDTH}x{EXPECTED_HEIGHT})"
        )
    return size, width, height


def main():
    output_dir = sys.argv[1] if len(sys.argv) > 1 else "/output"
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(repo_dir, SOURCE_NAME)
    if not os.path.isfile(source):
        print(f"error: source image not found: {source}", file=sys.stderr)
        return 1
    os.makedirs(output_dir, exist_ok=True)
    destination = os.path.join(output_dir, SOURCE_NAME)
    shutil.copyfile(source, destination)
    actual = sha256_file(destination)
    if actual != EXPECTED_SHA256:
        print(
            f"error: SHA-256 mismatch for {destination}:\n"
            f"  expected: {EXPECTED_SHA256}\n"
            f"  actual:   {actual}",
            file=sys.stderr,
        )
        return 1
    try:
        size, width, height = validate_output(destination)
    except (OSError, ValueError) as exc:
        print(f"error: output validation failed: {exc}", file=sys.stderr)
        return 1
    # Second verification pass: re-read the written file and re-check its hash.
    second = sha256_file(destination)
    if second != EXPECTED_SHA256:
        print(
            f"error: second-pass SHA-256 mismatch for {destination}:\n"
            f"  expected: {EXPECTED_SHA256}\n"
            f"  actual:   {second}",
            file=sys.stderr,
        )
        return 1
    print(f"wrote {destination} ({size} bytes, {width}x{height}, sha256 ok)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
