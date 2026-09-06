#!/usr/bin/env python3
"""Regenerate every example icon from assets/icons JSON compositions."""
from __future__ import annotations
import subprocess,sys
from pathlib import Path
def main()->int:
    root=Path(__file__).resolve().parent.parent; icon_dir=root/"assets"/"icons"; files=sorted(icon_dir.glob("*.json"))
    if not files: print("No icon JSON compositions found in assets/icons/.",file=sys.stderr); return 1
    renderer=root/"core"/"render_icon.py"
    for source in files: subprocess.run([sys.executable,str(renderer),str(source),str(icon_dir/f"{source.stem}.svg")],check=True)
    print(f"Regenerated {len(files)} example icons."); return 0
if __name__=="__main__": raise SystemExit(main())
