#!/usr/bin/env python3
"""Shared path parsing, rigid transforms, SVG rendering, and sampling."""

from __future__ import annotations

import math
import re
from dataclasses import dataclass

from shape_registry import get_shape

NUMBER = r"-?\d*\.?\d+(?:e-?\d+)?"


@dataclass
class Command:
    type: str
    points: list[tuple[float, float]]
    arc: tuple[float, float, float, int, int] | None = None


def parse_path(d: str) -> list[Command]:
    commands: list[Command] = []
    for chunk in re.findall(r"[A-Za-z][^A-Za-z]*", d):
        kind = chunk[0]
        values = [float(v) for v in re.findall(NUMBER, chunk[1:], re.I)]
        if kind == "Z": commands.append(Command("Z", [])); continue
        if kind in ("M", "L"):
            for i in range(0, len(values), 2):
                commands.append(Command(kind if i == 0 else "L", [(values[i], values[i+1])]))
        elif kind == "Q":
            for i in range(0, len(values), 4):
                commands.append(Command("Q", [(values[i], values[i+1]), (values[i+2], values[i+3])]))
        elif kind == "A":
            for i in range(0, len(values), 7):
                commands.append(Command("A", [(values[i+5], values[i+6])], (values[i], values[i+1], values[i+2], int(values[i+3]), int(values[i+4]))))
        else:
            raise ValueError(f"cannot bake {kind!r}; atoms may only use M, L, Q, A, and Z")
    return commands


def primitive_commands(tag: str, attrs: dict[str, object]) -> list[Command]:
    if tag == "path": return parse_path(str(attrs["d"]))
    if tag == "ellipse":
        cx, cy, rx, ry = (float(attrs[k]) for k in ("cx", "cy", "rx", "ry"))
        return parse_path(f"M {cx} {cy-ry} A {rx} {ry} 0 1 1 {cx} {cy+ry} A {rx} {ry} 0 1 1 {cx} {cy-ry} Z")
    if tag == "rect":
        x,y,w,h = (float(attrs[k]) for k in ("x","y","width","height")); radius=min(float(attrs.get("rx",0)),w/2,h/2)
        if not radius: return parse_path(f"M {x} {y} L {x+w} {y} L {x+w} {y+h} L {x} {y+h} Z")
        r=radius
        return parse_path(f"M {x+r} {y} L {x+w-r} {y} A {r} {r} 0 0 1 {x+w} {y+r} L {x+w} {y+h-r} A {r} {r} 0 0 1 {x+w-r} {y+h} L {x+r} {y+h} A {r} {r} 0 0 1 {x} {y+h-r} L {x} {y+r} A {r} {r} 0 0 1 {x+r} {y} Z")
    raise ValueError(f"cannot bake primitive {tag!r}")


def resolve_icon(document: dict) -> list[dict]:
    instances=document.get("instances")
    if not isinstance(instances,list) or not instances: raise ValueError("icon source needs a non-empty `instances` array")
    resolved=[]
    for order, item in sorted(enumerate(instances), key=lambda pair:(pair[1].get("z",0),pair[0])):
        shape=get_shape(item["shapeId"]); tag,attrs=shape.geometry(float(item["w"]),float(item["h"])); commands=primitive_commands(tag,attrs)
        theta=math.radians(float(item.get("rotation",0))); cos,sin=math.cos(theta),math.sin(theta)
        fx=-1 if item.get("flipX") else 1; fy=-1 if item.get("flipY") else 1
        a,b,c,d=fx*cos,-fy*sin,fx*sin,fy*cos; w,h=float(item["w"]),float(item["h"]); cx=float(item["x"])+w/2; cy=float(item["y"])+h/2
        e=cx-a*w/2-b*h/2; f=cy-c*w/2-d*h/2; det=a*d-b*c
        baked=[]
        for command in commands:
            points=[(a*x+b*y+e,c*x+d*y+f) for x,y in command.points]
            arc=command.arc
            if arc:
                rx,ry,rot,large,sweep=arc; phi=math.radians(rot); ax=a*math.cos(phi)+b*math.sin(phi); ay=c*math.cos(phi)+d*math.sin(phi)
                arc=(rx,ry,(math.degrees(math.atan2(ay,ax))+360)%180,large,1-sweep if det<0 else sweep)
            baked.append(Command(command.type,points,arc))
        resolved.append({"order":order,"shapeId":item["shapeId"],"commands":baked})
    return resolved


def fmt(value: float) -> str:
    rounded=round(value,4)
    if abs(rounded)<.00005: rounded=0
    return f"{rounded:g}"


def path_data(commands: list[Command], scale: float=1) -> str:
    output=[]
    for command in commands:
        if command.type=="Z": output.append("Z"); continue
        pts=" ".join(f"{fmt(x*scale)} {fmt(y*scale)}" for x,y in command.points)
        if command.type=="A":
            rx,ry,rot,large,sweep=command.arc or (0,0,0,0,0); output.append(f"A {fmt(rx*scale)} {fmt(ry*scale)} {fmt(rot)} {large} {sweep} {pts}")
        else: output.append(f"{command.type} {pts}")
    return " ".join(output)


def svg(paths: list[dict], canvas: int, stroke: int, scale: float=1) -> str:
    body="\n".join(f'  <path d="{path_data(p["commands"],scale)}"/>' for p in paths)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {canvas} {canvas}"\n     fill="none" stroke="currentColor" stroke-width="{stroke}"\n     stroke-linecap="round" stroke-linejoin="round">\n{body}\n</svg>\n'


def sample(commands: list[Command], density: int=4) -> tuple[list[tuple[float,float]],list[tuple[tuple[float,float],tuple[float,float]]]]:
    points=[]; segments=[]; cursor=None; start=None
    def line(a,b):
        segments.append((a,b)); steps=max(2,math.ceil(math.dist(a,b)*density)); points.extend((a[0]+(b[0]-a[0])*i/steps,a[1]+(b[1]-a[1])*i/steps) for i in range(1,steps+1))
    for cmd in commands:
        if cmd.type=="M": cursor=start=cmd.points[0]; points.append(cursor)
        elif cmd.type=="L": line(cursor,cmd.points[0]); cursor=cmd.points[0]
        elif cmd.type=="Q":
            control,end=cmd.points; steps=max(8,math.ceil(math.dist(cursor,end)*density))
            fractions=[i/steps for i in range(1,steps+1)]
            # Same reason as the arc branch: a quadratic's own axis extremes rarely
            # land on a sample step, and a bound the apex is meant to touch would
            # then read as a near miss. Merged in parametric order.
            for axis in (0,1):
                denominator=cursor[axis]-2*control[axis]+end[axis]
                if abs(denominator)<1e-12: continue
                extreme=(cursor[axis]-control[axis])/denominator
                if 0<extreme<1: fractions.append(extreme)
            fractions.sort()
            for t in fractions:
                u=1-t; points.append((u*u*cursor[0]+2*u*t*control[0]+t*t*end[0],u*u*cursor[1]+2*u*t*control[1]+t*t*end[1]))
            cursor=end
        elif cmd.type=="A":
            # Reliable SVG arc sampling using the endpoint-to-centre conversion.
            end=cmd.points[0]; rx,ry,rotation,large,sweep=cmd.arc or (0,0,0,0,0)
            if not rx or not ry: points.append(end); cursor=end; continue
            phi=math.radians(rotation); cp,sp=math.cos(phi),math.sin(phi); dx=(cursor[0]-end[0])/2; dy=(cursor[1]-end[1])/2
            x1=cp*dx+sp*dy; y1=-sp*dx+cp*dy; rx,ry=abs(rx),abs(ry); lam=x1*x1/(rx*rx)+y1*y1/(ry*ry)
            if lam>1: factor=math.sqrt(lam); rx*=factor; ry*=factor
            sign=-1 if large==sweep else 1; numerator=max(0,rx*rx*ry*ry-rx*rx*y1*y1-ry*ry*x1*x1); denominator=rx*rx*y1*y1+ry*ry*x1*x1 or 1
            factor=sign*math.sqrt(numerator/denominator); cxp=factor*rx*y1/ry; cyp=-factor*ry*x1/rx; cx=cp*cxp-sp*cyp+(cursor[0]+end[0])/2; cy=sp*cxp+cp*cyp+(cursor[1]+end[1])/2
            def angle(u,v): return math.atan2(u[0]*v[1]-u[1]*v[0],u[0]*v[0]+u[1]*v[1])
            u=((x1-cxp)/rx,(y1-cyp)/ry); v=((-x1-cxp)/rx,(-y1-cyp)/ry); theta=angle((1,0),u); delta=angle(u,v)
            if not sweep and delta>0: delta-=2*math.pi
            if sweep and delta<0: delta+=2*math.pi
            steps=max(8,math.ceil(abs(delta)*max(rx,ry)*density))
            parameters=[theta+delta*i/steps for i in range(1,steps+1)]
            # An arc's own axis extremes almost never land on a sample step, so add
            # them exactly: without them a half-arc's apex is measured short and a
            # keyshape bound the apex is supposed to touch reads as a near miss.
            # They are merged in parametric order, because callers rely on sampled
            # points following the path.
            for numerator,denominator in ((-ry*sp,rx*cp),(ry*cp,rx*sp)):
                if abs(numerator)<1e-12 and abs(denominator)<1e-12: continue
                base=math.atan2(numerator,denominator)
                parameters.extend(base+turn*math.pi for turn in (-2,-1,0,1,2)
                                  if 0<(base+turn*math.pi-theta)/delta<1)
            parameters.sort(reverse=delta<0)
            for t in parameters:
                px=rx*math.cos(t); py=ry*math.sin(t); points.append((cp*px-sp*py+cx,sp*px+cp*py+cy))
            cursor=end
        elif cmd.type=="Z" and cursor and start: line(cursor,start); cursor=start
    return points,segments
