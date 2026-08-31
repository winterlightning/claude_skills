#!/usr/bin/env python3
"""Render expanded-stroke envelope panels for declared spacing checks."""
from __future__ import annotations
import argparse,html,json
from pathlib import Path
from icon_geometry import path_data,resolve_icon
ENVELOPES={"ordinary-distinct":4,"connected":4,"intentional-overlap":4,"visual-opening":8}
def main()->int:
    p=argparse.ArgumentParser(); p.add_argument("input",type=Path); p.add_argument("output",type=Path,nargs="?"); a=p.parse_args(); doc=json.loads(a.input.read_text()); name=doc.get("name",a.input.stem); paths=resolve_icon(doc); by={x["order"]:path_data(x["commands"]) for x in paths}; panels=[]
    for check in doc.get("sourceAnalysis",{}).get("spacingChecks",[]):
        pair=check.get("instances");
        if not isinstance(pair,list) or len(pair)!=2 or any(i not in by for i in pair): continue
        relation=check.get("relation","ordinary-distinct"); width=check.get("envelopeWidth",ENVELOPES.get(relation,4)); offset=len(panels)*52; label=html.escape(" / ".join(check.get("pair",[])))
        context="\n".join(f'<path d="{d}" stroke="#d1d5db" stroke-width="4"/>' for i,d in by.items() if i not in pair)
        colors=("#ef4444","#2563eb"); selected="\n".join(f'<path d="{by[i]}" stroke="{colors[k]}" stroke-width="{width}" opacity=".5"/>' for k,i in enumerate(pair))
        panels.append(f'<g transform="translate({offset} 0)">{context}{selected}<text x="1" y="51.4" font-family="sans-serif" font-size="2.4" fill="#111827" stroke="none">{label} · {relation} · {width}u</text></g>')
    if not panels: print(f"{name}: no two-instance spacing checks — nothing to audit"); return 1
    width=len(panels)*52-4; out=a.output or a.input.parent/f"{name}-overlap-audit.svg"; out.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} 53" fill="none" stroke-linecap="round" stroke-linejoin="round"><rect width="100%" height="100%" fill="#fff"/>{"".join(panels)}</svg>\n'); print(f"{name} — {len(panels)} envelope panels written to {out}"); return 0
if __name__=="__main__": raise SystemExit(main())
