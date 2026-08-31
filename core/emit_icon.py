#!/usr/bin/env python3
"""Emit exact 48-unit design and 24-pixel shipping SVGs from icon JSON."""
from __future__ import annotations
import argparse,json,re
from pathlib import Path
from icon_geometry import resolve_icon,svg

def main() -> int:
    parser=argparse.ArgumentParser(); parser.add_argument("input",type=Path); parser.add_argument("--out-dir",type=Path); args=parser.parse_args()
    document=json.loads(args.input.read_text()); name=document.get("name",args.input.stem)
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*",name): raise ValueError(f"icon name {name!r} must be kebab-case")
    if document.get("canvas",48)!=48: raise ValueError("the design canvas is fixed at 48")
    if document.get("strokeWidth",4)!=4: raise ValueError("the Regular design stroke is fixed at 4u")
    paths=resolve_icon(document); out=args.out_dir or args.input.parent; out.mkdir(parents=True,exist_ok=True)
    design=out/f"{name}-design.svg"; ship=out/f"{name}.svg"; design.write_text(svg(paths,48,4)); ship.write_text(svg(paths,24,2,.5))
    print(f"Emitted {len(paths)} instances to {design} and {ship}"); return 0
if __name__=="__main__": raise SystemExit(main())
