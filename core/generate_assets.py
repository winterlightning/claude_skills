#!/usr/bin/env python3
"""Generate standalone atomic-shape SVG assets from the Python registry."""
from __future__ import annotations
import argparse,html
from pathlib import Path
from shape_registry import SHAPES
def main()->int:
    p=argparse.ArgumentParser(); p.add_argument("--out-dir",type=Path); a=p.parse_args(); root=Path(__file__).resolve().parent.parent; out=a.out_dir or root/"assets"/"shapes"; out.mkdir(parents=True,exist_ok=True)
    for shape in SHAPES:
        w,h=shape.natural; tag,attrs=shape.geometry(w,h); attributes=" ".join(f'{k}="{html.escape(str(v),quote=True)}"' for k,v in attrs.items()); (out/f"{shape.id}.svg").write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-1 -1 {w+2:g} {h+2:g}">\n  <{tag} {attributes} fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>\n</svg>\n')
    print(f"Wrote {len(SHAPES)} shapes to {out}/"); return 0
if __name__=="__main__": raise SystemExit(main())
