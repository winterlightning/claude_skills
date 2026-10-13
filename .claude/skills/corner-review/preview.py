#!/usr/bin/env python3
"""preview.py BATCH_JSON ICON OUT_PNG [--round X,Y ...] [--sharp X,Y ...]
Runs round_or_sharp.py and draws input · sharp now · proposed (256 px, then 48 px) into OUT_PNG, so the drawing can
be looked at before it is recorded. Prints round_or_sharp.py's JSON (pass its "paths" to record.py --paths)."""
import json
import os
import re
import subprocess
import sys
import tempfile
from io import BytesIO

from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", "corner_processing"))


def render(svg, size):
    png = subprocess.run(["rsvg-convert", "-w", str(size), "-h", str(size), "-b", "white"], input=svg.encode(),
                         capture_output=True, check=True).stdout
    return Image.open(BytesIO(png)).convert("RGB")


def main():
    batch, icon, out = sys.argv[1:4]
    run = subprocess.run([sys.executable, os.path.join(HERE, "round_or_sharp.py"), batch, icon, *sys.argv[4:]],
                         capture_output=True, text=True, check=True)
    res = json.loads(run.stdout)
    name = icon if icon.endswith(".svg") else icon + ".svg"
    sharp = open(os.path.join(ROOT, "outputs", "solo48", "sharp", name), encoding="utf-8").read()
    new = sharp
    for v in res["paths"].values():
        for old in (v["old"], v["old"].replace("Z", " Z")):
            if f'd="{old}"' in new:
                new = new.replace(f'd="{old}"', f'd="{v["new"]}"', 1)
                break
    plates = {"input": open(os.path.join(ROOT, "input", "solo48", "svg", name), encoding="utf-8").read(),
              "sharp now": sharp, "proposed": new}
    pad, W = 12, 256
    im = Image.new("RGB", (pad + 3 * (W + pad), 22 + W + 22 + 48 + pad), "white")
    d = ImageDraw.Draw(im)
    for i, (k, svg) in enumerate(plates.items()):
        x = pad + i * (W + pad)
        d.text((x, 4), k, fill=(0, 0, 0))
        im.paste(render(svg, W), (x, 18))
        d.rectangle([x - 1, 17, x + W, 18 + W], outline=(200, 200, 200))
        im.paste(render(svg, 48), (x + (W - 48) // 2, 18 + W + 18))
    im.save(out)
    print(json.dumps(res))


if __name__ == "__main__":
    main()
