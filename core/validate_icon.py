#!/usr/bin/env python3
"""Validate profile, keyshape, spacing, container clearance, and SVG parity."""
from __future__ import annotations
import argparse,json,math
from collections import defaultdict
from pathlib import Path
from icon_geometry import finite_number,resolve_icon,sample,spacing_pair,svg
from icon_profiles import document_icon_type,get_profile,validate_container_slot,validate_document_profile
from keyfit import assign,circle_overflow,describe,matches,max_box,token_box,token_named,validate_optical_bounds

def minimum_distance(a,b): return min(math.dist(p,q) for p in a for q in b)

def _point_rect_distance(point,bounds):
    x,y=point; left,top,right,bottom=bounds
    dx=max(left-x,0,x-right); dy=max(top-y,0,y-bottom)
    return math.hypot(dx,dy)

def container_paint_overlap(points,slot,stroke_width,tolerance=1e-3):
    """Return sampled centerline points whose stroke enters the clear square."""
    radius=stroke_width/2
    bounds=slot["protectedBounds"]
    return [point for point in points if _point_rect_distance(point,bounds) < radius-tolerance]

def main() -> int:
    parser=argparse.ArgumentParser(); parser.add_argument("input",type=Path); parser.add_argument("--dir",type=Path); args=parser.parse_args()
    doc=json.loads(args.input.read_text()); name=doc.get("name",args.input.stem); failures=[]; notes=[]
    icon_type=document_icon_type(doc); profile=get_profile(icon_type)
    try: validate_document_profile(doc)
    except ValueError as error: failures.append(str(error))
    if (doc.get("sourceAnalysis") or {}).get("incomplete") is True: failures.append("sourceAnalysis is marked incomplete; populate the source mappings before shipping")
    paths=resolve_icon(doc)
    sampled=[]
    for p in paths:
        pts,segs=sample(p["commands"]); sampled.append({**p,"points":pts,"segments":segs})
    all_points=[p for item in sampled for p in item["points"]]; minx=min(x for x,y in all_points); maxx=max(x for x,y in all_points); miny=min(y for x,y in all_points); maxy=max(y for x,y in all_points)
    radius=profile["designStroke"]/2; absolute=max_box(icon_type); centerline=(absolute[0]+radius,absolute[1]+radius,absolute[2]-radius,absolute[3]-radius)
    if minx<centerline[0]-1e-6 or maxx>centerline[2]+1e-6: failures.append(f"centerline x extent {minx:.4g}..{maxx:.4g} exceeds the {icon_type} circle-cardinal range {centerline[0]:g}..{centerline[2]:g}")
    if miny<centerline[1]-1e-6 or maxy>centerline[3]+1e-6: failures.append(f"centerline y extent {miny:.4g}..{maxy:.4g} exceeds the {icon_type} circle-cardinal range {centerline[1]:g}..{centerline[3]:g}")
    painted=(minx-radius,maxx+radius,miny-radius,maxy+radius); notes.append(f"painted extent x {painted[0]:.4g}..{painted[1]:.4g}, y {painted[2]:.4g}..{painted[3]:.4g}")
    width,height=painted[1]-painted[0],painted[3]-painted[2]
    painted_box=(painted[0],painted[2],painted[1],painted[3])
    keyfit_check=doc.get("keyfitCheck") or {}; expected_name=keyfit_check.get("targetToken")
    fit_mode=keyfit_check.get("mode","exact")
    if fit_mode not in ("exact","optical"): failures.append(f"unknown keyfitCheck.mode {fit_mode!r}")
    if fit_mode=="optical" and doc.get("schemaVersion")!=2: failures.append("optical keyshape fit requires schemaVersion: 2")
    if fit_mode=="optical" and not expected_name: failures.append("optical keyshape fit requires an explicit targetToken")
    if expected_name:
        expected=token_named(expected_name,icon_type)
        if not expected:
            assigned=None; failures.append(f"unknown declared keyshape target {expected_name!r}")
        else:
            box=token_box(expected["width"],expected["height"],icon_type)
            if fit_mode=="optical":
                failures.extend(validate_optical_bounds(keyfit_check,box,painted_box))
                assigned={**expected,"bounds":list(box)}
                notes.append(f"optical fit within {expected_name}; inspect the declared proportions at true size")
            else:
                assigned={**expected,"bounds":list(box)} if matches(box,painted_box,1e-3) else None
                if not assigned: failures.append(f"painted bounds {painted_box} do not exactly match declared {expected_name} bounds {box}")
    else:
        assigned=assign(painted_box,1e-3,icon_type=icon_type)
        if not assigned: failures.append(f"painted bounds {width:.4g}x{height:.4g} do not exactly match a {icon_type} keyshape ({describe(icon_type)})")
    if assigned and assigned["shape"]=="circle":
        overflow=circle_overflow(all_points,profile["designStroke"],icon_type)
        if overflow>1e-3: failures.append(f"painted geometry exceeds the {assigned['name']} boundary by {overflow:.4g}u")
    if icon_type=="container":
        try:
            slot=validate_container_slot(doc,profile); notes.append(f"protected container clearance {slot['minimumClearSquare']:g}x{slot['minimumClearSquare']:g} at {slot['protectedBounds']}")
            overlap=container_paint_overlap(all_points,slot,profile["designStroke"])
            if overlap: failures.append(f"container paint enters the protected {slot['minimumClearSquare']:g}x{slot['minimumClearSquare']:g} clearance near {overlap[0][0]:.4g},{overlap[0][1]:.4g}")
        except ValueError as error:
            if str(error) not in failures: failures.append(str(error))
    by_order=defaultdict(list)
    for item in sampled: by_order[item["order"]].extend(item["points"])
    measured={}; orders=sorted(by_order)
    for i,left in enumerate(orders):
        for right in orders[i+1:]: measured[(left,right)]=minimum_distance(by_order[left],by_order[right])
    checks=[]
    for check in doc.get("sourceAnalysis",{}).get("spacingChecks",[]):
        try: checks.append((spacing_pair(check,paths),check))
        except ValueError as error: failures.append(str(error))
    connected={pair for pair,check in checks if check.get("relation") in ("connected","intentional-overlap")}
    labels={item["order"]:item["elementId"] for item in paths}
    collision_floor=float(profile["minimumDistinctCenterlineDistance"])
    for pair,distance in measured.items():
        if pair in connected and distance<=.25: continue
        if 1e-6<distance<collision_floor-1e-3 or (doc.get("schemaVersion")==2 and distance<=1e-6): failures.append(f"elements {labels[pair[0]]} and {labels[pair[1]]} are {distance:.4g}u apart on centerlines, under the {collision_floor:g}u {icon_type} collision floor")
    for pair,check in checks:
        actual=measured[pair]; declared=check.get("centerlineDistance")
        if declared is not None:
            try:
                declared=finite_number(declared,"spacing centerlineDistance")
                if abs(actual-declared)>.02: failures.append(f"spacing check {pair} is stale: records {declared:.4g}u but geometry measures {actual:.4g}u")
            except ValueError as error: failures.append(str(error))
        if check.get("relation")=="visual-opening":
            try:
                minimum=finite_number(check["minimumCenterline"],"minimumCenterline") if "minimumCenterline" in check else profile["designStroke"]+finite_number(check.get("minimum",3),"minimum opening")
                if minimum<=0: raise ValueError("visual-opening minimum must be positive")
            except ValueError as error: failures.append(str(error)); continue
            if actual<minimum-1e-6:
                failures.append(f"visual opening {pair} is {actual:.4g}u apart on centerlines, under its {minimum:.4g}u minimum")
    out=args.dir or args.input.parent; design=out/f"{name}-design.svg"; ship=out/f"{name}.svg"
    scale=profile["shipCanvas"]/profile["designCanvas"]
    canonical={
        design:svg(paths,profile["designCanvas"],profile["designStroke"]),
        ship:svg(paths,profile["shipCanvas"],profile["shipStroke"],scale),
    }
    for path,canvas,stroke in ((design,profile["designCanvas"],profile["designStroke"]),(ship,profile["shipCanvas"],profile["shipStroke"])):
        if not path.exists(): failures.append(f"missing emitted file {path.name} — run core/emit_icon.py first"); continue
        text=path.read_text()
        if f'viewBox="0 0 {canvas} {canvas}"' not in text: failures.append(f"{path.name} has the wrong canvas")
        if f'stroke-width="{stroke}"' not in text: failures.append(f"{path.name} has the wrong stroke")
        if text!=canonical[path]: failures.append(f"{path.name} does not match canonical core/emit_icon.py output; re-emit both SVG sizes")
    print(f"{name} — {len(paths)} geometry elements"); [print(f"  · {n}") for n in notes]
    if failures:
        [print(f"  FAIL {f}") for f in failures]; return 1
    print(f"  OK — numeric, keyshape, and SVG checks passed. Inspect the true {profile['shipCanvas']:g}px output before shipping."); return 0
if __name__=="__main__": raise SystemExit(main())
