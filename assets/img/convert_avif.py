#!/usr/bin/env python3
"""
convert_images.py – Bulk-convert images to .webp
────────────────────────────────────────────────
# default: shrink-only if >1024 px
python convert_images.py

# project preset: fill to 1024×682, then crop (because we use -p -c)
python convert_images.py --project --crop     

# custom resize, fill & (optionally) crop
python convert_images.py -s 800x600^ --crop   # fill-and-crop to 800×600
python convert_images.py -s 1400>             # shrink-only to 1400 px
"""
import argparse, pathlib, re, shlex, subprocess, sys

# ────── CLI ──────
p = argparse.ArgumentParser(description="Convert images to WebP")
g = p.add_mutually_exclusive_group()
g.add_argument("-p", "--project", action="store_true",
               help="Preset resize to 1024x682^")
g.add_argument("-s", "--size", metavar="GEOMETRY",
               help="Custom geometry for -resize (e.g. 800x600^, 1400>)")
p.add_argument("-c", "--crop", action="store_true",
               help="After a ^-resize, center-crop to the same WxH")

args = p.parse_args()

# ────── choose geometry & extra ops ──────
if args.size:
    resize_arg = args.size
elif args.project:
    resize_arg = "1024x682^"
else:
    resize_arg = "1024>"

extra_ops = ""
crop_needed = args.crop and "^" in resize_arg

if crop_needed:
    # pull out W and H before the caret
    m = re.match(r"(\d+)x(\d+)", resize_arg)
    if m:
        w, h = m.groups()
        extra_ops = f"-gravity center -crop {w}x{h}+0+0 +repage"
    else:
        print("[WARN] --crop ignored: can’t parse WxH from", resize_arg, file=sys.stderr)

# ────── convert ──────
TARGET_SUFFIX = ".webp"
IMAGE_EXTS = {".jpg", ".jpeg", ".JPG", ".png"}

for path in pathlib.Path(".").rglob("*"):
    if path.suffix in IMAGE_EXTS and path.is_file():
        out_path = path.with_suffix(TARGET_SUFFIX)
        if out_path.exists():
            continue
        cmd = (
            f"magick {shlex.quote(str(path))} "
            f"-resize {shlex.quote(resize_arg)} {extra_ops} "
            f"{shlex.quote(str(out_path))}"
        )
        print(f"Converting {path} → {out_path}")
        if subprocess.run(cmd, shell=True).returncode:
            print(f"[ERROR] Failed on {path}", file=sys.stderr)
