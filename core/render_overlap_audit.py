#!/usr/bin/env python3
"""Render expanded-stroke envelope panels for declared spacing checks."""
from __future__ import annotations
import argparse,html,json
from pathlib import Path
from icon_geometry import finite_number,path_data,resolve_icon,spacing_pair
from icon_profiles import profile_for_document
ENVELOPES={"connected":4,"intentional-overlap":4,"visual-opening":8}
def main()->int:
    p=argparse.ArgumentParser(); p.add_argument("input",type=Path); p.add_argument("output",type=Path,nargs="?"); a=p.parse_args(); doc=json.loads(a.input.read_text()); name=doc.get("name",a.input.stem); profile=profile_for_document(doc); canvas=profile["designCanvas"]; stroke=profile["designStroke"]; panel_width=canvas+4; paths=resolve_icon(doc); by={x["order"]:path_data(x["commands"]) for x in paths}; panels=[]
    for check in doc.get("sourceAnalysis",{}).get("spacingChecks",[]):
        pair=spacing_pair(check,paths)
        relation=check.get("relation","ordinary-distinct"); default_width=profile["minimumDistinctCenterlineDistance"] if relation=="ordinary-distinct" else ENVELOPES.get(relation,profile["designStroke"]); width=finite_number(check.get("envelopeWidth",default_width),"envelopeWidth"); offset=len(panels)*panel_width; label=html.escape(" / ".join(check.get("pair",check.get("elements",[str(i) for i in pair]))))
        if width<=0: raise ValueError("envelopeWidth must be positive")
        context="\n".join(f'<path d="{d}" stroke="#d1d5db" stroke-width="{stroke}"/>' for i,d in by.items() if i not in pair)
        colors=("#ef4444","#2563eb"); selected="\n".join(f'<path d="{by[i]}" stroke="{colors[k]}" stroke-width="{width:g}" opacity=".5"/>' for k,i in enumerate(pair))
        panels.append(f'<g transform="translate({offset} 0)">{context}{selected}<text x="1" y="{canvas+3.4:g}" font-family="sans-serif" font-size="2.4" fill="#111827" stroke="none">{label} · {html.escape(str(relation))} · {width:g}u</text></g>')
    if not panels: print(f"{name}: no two-element spacing checks — nothing to audit"); return 1
    width=len(panels)*panel_width-4; out=a.output or a.input.parent/f"{name}-overlap-audit.svg"; out.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width:g} {canvas+5:g}" fill="none" stroke-linecap="round" stroke-linejoin="round"><rect width="100%" height="100%" fill="#fff"/>{"".join(panels)}</svg>\n'); print(f"{name} — {len(panels)} {profile['iconType']} envelope panels written to {out}"); return 0
if __name__=="__main__": raise SystemExit(main())
