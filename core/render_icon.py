#!/usr/bin/env python3
"""Compatibility renderer for JSON compositions; emits canonical design and ship SVGs."""
from __future__ import annotations
import argparse,json,re
from pathlib import Path
from icon_geometry import resolve_icon,svg
from icon_profiles import validate_document_profile
def main()->int:
    p=argparse.ArgumentParser(); p.add_argument("input",type=Path); p.add_argument("output",type=Path,nargs="?"); p.add_argument("--distance-check",action="store_true"); a=p.parse_args(); doc=json.loads(a.input.read_text()); name=doc.get("name",a.input.stem)
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*",name): raise ValueError("name must be kebab-case")
    icon_type,profile=validate_document_profile(doc); paths=resolve_icon(doc); output=a.output or Path(f"{name}.svg"); output.parent.mkdir(parents=True,exist_ok=True); output.write_text(svg(paths,profile["designCanvas"],profile["designStroke"])); ship=output.with_name(f"{output.stem}-{profile['shipCanvas']}.svg"); ship.write_text(svg(paths,profile["shipCanvas"],profile["shipStroke"],profile["shipCanvas"]/profile["designCanvas"])); print(f"Rendered {len(paths)} {icon_type} geometry elements to {output} and {ship}"); return 0
if __name__=="__main__": raise SystemExit(main())
