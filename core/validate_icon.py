#!/usr/bin/env python3
"""Validate canvas, keyshape containment, angles, spacing, and SVG parity."""
from __future__ import annotations
import argparse,json,math,re
from pathlib import Path
from icon_geometry import resolve_icon,sample
from keyfit import assign,circle_overflow,matches,token_box,token_named

def minimum_distance(a,b): return min(math.dist(p,q) for p in a for q in b)
def main() -> int:
    parser=argparse.ArgumentParser(); parser.add_argument("input",type=Path); parser.add_argument("--dir",type=Path); args=parser.parse_args()
    doc=json.loads(args.input.read_text()); name=doc.get("name",args.input.stem); failures=[]; notes=[]; paths=resolve_icon(doc)
    sampled=[]
    for p in paths:
        pts,segs=sample(p["commands"]); sampled.append({**p,"points":pts,"segments":segs})
    all_points=[p for item in sampled for p in item["points"]]; minx=min(x for x,y in all_points); maxx=max(x for x,y in all_points); miny=min(y for x,y in all_points); maxy=max(y for x,y in all_points)
    if minx<4-1e-6 or maxx>44+1e-6: failures.append(f"centerline x extent {minx:.4g}..{maxx:.4g} exceeds the absolute circle-cardinal range 4..44")
    if miny<4-1e-6 or maxy>44+1e-6: failures.append(f"centerline y extent {miny:.4g}..{maxy:.4g} exceeds the absolute circle-cardinal range 4..44")
    painted=(minx-2,maxx+2,miny-2,maxy+2); notes.append(f"painted extent x {painted[0]:.4g}..{painted[1]:.4g}, y {painted[2]:.4g}..{painted[3]:.4g}")
    width,height=painted[1]-painted[0],painted[3]-painted[2]
    painted_box=(painted[0],painted[2],painted[1],painted[3])
    expected_name=(doc.get("keyfitCheck") or {}).get("targetToken")
    if expected_name:
        expected=token_named(expected_name)
        if not expected:
            assigned=None; failures.append(f"unknown declared keyshape target {expected_name!r}")
        else:
            box=token_box(expected["width"],expected["height"])
            assigned={**expected,"bounds":list(box)} if matches(box,painted_box,1e-3) else None
            if not assigned: failures.append(f"painted bounds {painted_box} do not exactly match declared {expected_name} bounds {box}")
    else:
        assigned=assign(painted_box,1e-3)
        if not assigned: failures.append(f"painted bounds {width:.4g}x{height:.4g} do not exactly match circle-44, square-40, portrait-36x44, or landscape-44x36")
    if assigned and assigned["shape"]=="circle":
        overflow=circle_overflow(all_points,4)
        if overflow>1e-3: failures.append(f"painted geometry exceeds the circle-44 boundary by {overflow:.4g}u")
    for item in sampled:
        for a,b in item["segments"]:
            if math.dist(a,b)<1e-6: continue
            angle=(math.degrees(math.atan2(b[1]-a[1],b[0]-a[0]))+360)%180
            if abs(angle-round(angle/15)*15)>.01: failures.append(f'instances[{item["order"]}] ({item["shapeId"]}) has a straight segment at {angle:.4g} degrees')
    measured={}
    for i in range(len(sampled)):
        for j in range(i+1,len(sampled)): measured[(sampled[i]["order"],sampled[j]["order"])]=minimum_distance(sampled[i]["points"],sampled[j]["points"])
    connected={tuple(sorted(c.get("instances",[]))) for c in doc.get("sourceAnalysis",{}).get("spacingChecks",[]) if c.get("relation") in ("connected","intentional-overlap")}
    for pair,distance in measured.items():
        if pair in connected and distance<=.25: continue
        if 1e-6<distance<3.999: failures.append(f"instances {pair[0]} and {pair[1]} are {distance:.4g}u apart on centerlines, under the 4u collision floor")
    out=args.dir or args.input.parent; design=out/f"{name}-design.svg"; ship=out/f"{name}.svg"
    for path,canvas,stroke in ((design,48,4),(ship,24,2)):
        if not path.exists(): failures.append(f"missing emitted file {path.name} — run core/emit_icon.py first"); continue
        text=path.read_text()
        if f'viewBox="0 0 {canvas} {canvas}"' not in text: failures.append(f"{path.name} has the wrong canvas")
        if f'stroke-width="{stroke}"' not in text: failures.append(f"{path.name} has the wrong stroke")
        if re.search(r"[Cc](?=[\s\-0-9.])",text.replace("currentColor","")): failures.append(f"{path.name} contains a cubic command")
    print(f"{name} — {len(paths)} instances"); [print(f"  · {n}") for n in notes]
    if failures:
        [print(f"  FAIL {f}") for f in failures]; return 1
    print("  OK — numeric, keyshape, and SVG checks passed. Inspect the true 24px output before shipping."); return 0
if __name__=="__main__": raise SystemExit(main())
