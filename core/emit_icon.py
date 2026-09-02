#!/usr/bin/env python3
"""Emit exact design and shipping SVGs from profiled icon JSON."""
from __future__ import annotations
import argparse,json,re
from pathlib import Path
from icon_geometry import resolve_icon,svg
from icon_profiles import validate_document_profile

def main() -> int:
    parser=argparse.ArgumentParser(); parser.add_argument("input",type=Path); parser.add_argument("--out-dir",type=Path); args=parser.parse_args()
    document=json.loads(args.input.read_text()); name=document.get("name",args.input.stem)
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*",name): raise ValueError(f"icon name {name!r} must be kebab-case")
    icon_type,profile=validate_document_profile(document)
    paths=resolve_icon(document); out=args.out_dir or args.input.parent; out.mkdir(parents=True,exist_ok=True)
    design=out/f"{name}-design.svg"; ship=out/f"{name}.svg"
    scale=profile["shipCanvas"]/profile["designCanvas"]
    design.write_text(svg(paths,profile["designCanvas"],profile["designStroke"])); ship.write_text(svg(paths,profile["shipCanvas"],profile["shipStroke"],scale))
    print(f"Emitted {len(paths)} {icon_type} instances to {design} and {ship}"); return 0
if __name__=="__main__": raise SystemExit(main())
