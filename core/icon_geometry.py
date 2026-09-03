#!/usr/bin/env python3
"""Geometry-first icon sources, legacy placement baking, rendering, and sampling.

Version 2 sources own their contours directly. The registry is only imported on
the legacy ``instances`` branch; new icons do not need a registered silhouette.
"""

from __future__ import annotations

import math
import re
from dataclasses import dataclass

NUMBER = r"[-+]?(?:\d*\.\d+|\d+\.?)(?:[eE][-+]?\d+)?"
NUMBER_RE = re.compile(NUMBER)
PARAMS = {"M":2,"L":2,"H":1,"V":1,"C":6,"S":4,"Q":4,"T":2,"A":7}
ELEMENT_ATTRS = {
    "path": {"d"}, "line": {"x1","y1","x2","y2"},
    "circle": {"cx","cy","r"}, "ellipse": {"cx","cy","rx","ry"},
    "rect": {"x","y","width","height","rx","ry"},
    "polyline": {"points"}, "polygon": {"points"},
}
ELEMENT_ID = re.compile(r"[A-Za-z][A-Za-z0-9_.:-]*")


def finite_number(value: object, label: str = "coordinate") -> float:
    """Accept JSON numbers or SVG numeric strings, never units/bools/NaN/Inf."""
    if isinstance(value,bool) or not isinstance(value,(int,float,str)):
        raise ValueError(f"{label} must be a finite number")
    if isinstance(value,str) and not NUMBER_RE.fullmatch(value.strip()):
        raise ValueError(f"{label} must be a finite unitless number")
    try: number=float(value)
    except (ValueError,OverflowError) as error:
        raise ValueError(f"{label} must be a finite number") from error
    if not math.isfinite(number): raise ValueError(f"{label} must be a finite number")
    return number


class _Numbers:
    """Context-aware scanner, including SVG's adjacent single-digit arc flags."""
    def __init__(self,text: str): self.text=text; self.pos=0
    def whitespace(self):
        while self.pos<len(self.text) and self.text[self.pos] in " \t\r\n": self.pos+=1
    def number(self, *, comma: bool=True, flag: bool=False) -> float:
        self.whitespace()
        if comma and self.pos<len(self.text) and self.text[self.pos]==",":
            self.pos+=1; self.whitespace()
        if flag:
            if self.pos>=len(self.text) or self.text[self.pos] not in "01":
                raise ValueError(f"arc flag at offset {self.pos} must be 0 or 1")
            value=float(self.text[self.pos]); self.pos+=1; return value
        match=NUMBER_RE.match(self.text,self.pos)
        if not match: raise ValueError(f"expected SVG number at offset {self.pos}")
        self.pos=match.end(); return finite_number(match.group(),"path/points coordinate")


@dataclass
class Command:
    type: str
    points: list[tuple[float, float]]
    arc: tuple[float, float, float, int, int] | None = None


def parse_path(d: str) -> list[Command]:
    """Strictly parse SVG paths and normalize shorthand/relative commands.

    Output commands are absolute M/L/Q/C/A/Z. Unknown text, incomplete groups,
    invalid arc flags/radii, and non-finite coordinates are never discarded.
    """
    if not isinstance(d,str) or not d.strip(): raise ValueError("path d must be a non-empty string")
    reader=_Numbers(d); commands=[]; active=None; cursor=(0.0,0.0); start=None
    while True:
        reader.whitespace()
        if reader.pos==len(d): break
        explicit=d[reader.pos] in "MmLlHhVvCcSsQqTtAaZz"
        if explicit:
            active=d[reader.pos]; reader.pos+=1
        elif active is None:
            raise ValueError(f"expected SVG path command at offset {reader.pos}")
        upper=active.upper()
        if not commands and upper!="M": raise ValueError("path must start with moveto M or m")
        if upper=="Z":
            commands.append(Command("Z",[])); cursor=start; active=None; continue
        values=[reader.number(comma=index>0 or not explicit,flag=upper=="A" and index in (3,4)) for index in range(PARAMS[upper])]
        relative=active.islower()
        def point(index):
            x,y=values[index:index+2]
            return (finite_number(x+cursor[0]),finite_number(y+cursor[1])) if relative else (x,y)
        if upper in ("M","L"):
            command=Command(upper,[point(0)])
        elif upper=="H": command=Command("L",[(finite_number(values[0]+cursor[0]) if relative else values[0],cursor[1])])
        elif upper=="V": command=Command("L",[(cursor[0],finite_number(values[0]+cursor[1]) if relative else values[0])])
        elif upper in ("Q","C"):
            command=Command(upper,[point(index) for index in range(0,len(values),2)])
        elif upper in ("S","T"):
            curve="C" if upper=="S" else "Q"
            previous=commands[-1] if commands else None
            last_control=previous.points[-2] if previous and previous.type==curve else cursor
            control=(finite_number(2*cursor[0]-last_control[0]),finite_number(2*cursor[1]-last_control[1]))
            command=Command(curve,[control]+[point(index) for index in range(0,len(values),2)])
        else:
            if values[0]<0 or values[1]<0: raise ValueError("arc radii must not be negative")
            command=Command("A",[point(5)],(values[0],values[1],values[2],int(values[3]),int(values[4])))
        commands.append(command); cursor=command.points[-1]
        if upper=="M": start=cursor; active="l" if relative else "L"
    return commands


def primitive_commands(tag: str, attrs: dict[str, object]) -> list[Command]:
    """Validate geometry-only primitive attributes and normalize to paths."""
    if tag not in ELEMENT_ATTRS: raise ValueError(f"unsupported geometry tag {tag!r}")
    if not isinstance(attrs,dict): raise ValueError(f"{tag} attrs must be an object")
    extra=set(attrs)-ELEMENT_ATTRS[tag]
    if extra: raise ValueError(f"{tag} contains forbidden/non-geometry attrs: {sorted(extra)}")
    if tag == "path":
        commands=parse_path(attrs.get("d"))
        cursor=None; start=None; drawable=False
        for command in commands:
            if command.type=="M": cursor=start=command.points[0]
            elif command.type=="Z": cursor=start
            else:
                drawable=drawable or command.type!="A" or command.points[-1]!=cursor
                cursor=command.points[-1]
        if not drawable: raise ValueError("path needs drawable geometry after moveto")
        return commands
    if tag in ("polyline","polygon"):
        source=attrs.get("points")
        if not isinstance(source,str) or not source.strip(): raise ValueError(f"{tag} points must be a non-empty SVG points string")
        reader=_Numbers(source); values=[]
        while True:
            reader.whitespace()
            if reader.pos==len(source): break
            values.append(reader.number(comma=bool(values)))
        minimum=6 if tag=="polygon" else 4
        if len(values)<minimum or len(values)%2: raise ValueError(f"{tag} needs at least {minimum//2} complete coordinate pairs")
        points=list(zip(values[::2],values[1::2]))
        return [Command("M" if index==0 else "L",[point]) for index,point in enumerate(points)]+([Command("Z",[])] if tag=="polygon" else [])
    values={key:finite_number(value,f"{tag}.{key}") for key,value in attrs.items()}
    def required(key,positive=False):
        if key not in values: raise ValueError(f"{tag} needs {key}")
        value=values[key]
        if positive and value<=0: raise ValueError(f"{tag}.{key} must be positive")
        return value
    if tag=="line": return [Command("M",[(values.get("x1",0),values.get("y1",0))]),Command("L",[(values.get("x2",0),values.get("y2",0))])]
    if tag in ("circle","ellipse"):
        cx,cy=values.get("cx",0),values.get("cy",0)
        rx=ry=required("r",True) if tag=="circle" else 0
        if tag=="ellipse": rx,ry=required("rx",True),required("ry",True)
        return parse_path(f"M {cx} {cy-ry} A {rx} {ry} 0 1 1 {cx} {cy+ry} A {rx} {ry} 0 1 1 {cx} {cy-ry} Z")
    if tag == "rect":
        x,y=values.get("x",0),values.get("y",0); w,h=required("width",True),required("height",True)
        rx=values.get("rx",values.get("ry",0)); ry=values.get("ry",rx)
        if rx<0 or ry<0: raise ValueError("rect rx and ry must not be negative")
        rx,ry=min(rx,w/2),min(ry,h/2)
        if not rx or not ry: return parse_path(f"M {x} {y} L {x+w} {y} L {x+w} {y+h} L {x} {y+h} Z")
        return parse_path(f"M {x+rx} {y} L {x+w-rx} {y} A {rx} {ry} 0 0 1 {x+w} {y+ry} L {x+w} {y+h-ry} A {rx} {ry} 0 0 1 {x+w-rx} {y+h} L {x+rx} {y+h} A {rx} {ry} 0 0 1 {x} {y+h-ry} L {x} {y+ry} A {rx} {ry} 0 0 1 {x+rx} {y} Z")
    raise ValueError(f"cannot bake primitive {tag!r}")


def resolve_icon(document: dict) -> list[dict]:
    if not isinstance(document,dict): raise ValueError("icon source must be an object")
    if "elements" in document:
        if "instances" in document: raise ValueError("icon source cannot mix elements and legacy instances")
        if type(document.get("schemaVersion")) is not int or document["schemaVersion"]!=2: raise ValueError("elements require schemaVersion: 2")
        elements=document["elements"]
        if not isinstance(elements,list) or not elements: raise ValueError("icon source needs a non-empty elements array")
        resolved=[]; ids=set()
        for order,item in enumerate(elements):
            if not isinstance(item,dict): raise ValueError(f"element {order} must be an object")
            extra=set(item)-{"id","role","tag","attrs"}
            if extra: raise ValueError(f"element {order} contains forbidden keys: {sorted(extra)}")
            identifier=item.get("id")
            if not isinstance(identifier,str) or not ELEMENT_ID.fullmatch(identifier): raise ValueError(f"element {order} needs a stable SVG-safe id")
            if identifier in ids: raise ValueError(f"duplicate element id {identifier!r}")
            ids.add(identifier)
            if "role" in item and not isinstance(item["role"],str): raise ValueError(f"element {identifier} role must be a string")
            tag=item.get("tag")
            if not isinstance(tag,str): raise ValueError(f"element {identifier} needs a geometry tag")
            commands=primitive_commands(tag,item.get("attrs"))
            resolved.append({"order":order,"id":identifier,"elementId":identifier,"shapeId":tag,"role":item.get("role"),"commands":commands})
        return resolved
    if document.get("schemaVersion") not in (None,1): raise ValueError("schemaVersion: 2 requires an elements array")
    from shape_registry import get_shape
    instances=document.get("instances")
    if not isinstance(instances,list) or not instances: raise ValueError("icon source needs a non-empty `instances` array")
    for order,item in enumerate(instances):
        if not isinstance(item,dict): raise ValueError(f"legacy instance {order} must be an object")
        for key in ("x","y","w","h"):
            if key not in item: raise ValueError(f"legacy instance {order} needs {key}")
            finite_number(item[key],f"instance {order}.{key}")
        finite_number(item.get("rotation",0),f"instance {order}.rotation")
        finite_number(item.get("z",0),f"instance {order}.z")
        for key in ("flipX","flipY"):
            if key in item and not isinstance(item[key],bool): raise ValueError(f"instance {order}.{key} must be a boolean")
    resolved=[]
    for order, item in sorted(enumerate(instances), key=lambda pair:(finite_number(pair[1].get("z",0)),pair[0])):
        shape=get_shape(item["shapeId"]); tag,attrs=shape.geometry(finite_number(item["w"]),finite_number(item["h"])); commands=primitive_commands(tag,attrs)
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
        resolved.append({"order":order,"id":f"instance-{order}","elementId":f"instance-{order}","shapeId":item["shapeId"],"commands":baked})
    return resolved


def spacing_pair(check: dict, paths: list[dict]) -> tuple[int,int]:
    """Resolve a declared pair of stable element IDs or legacy source indexes."""
    if not isinstance(check,dict): raise ValueError("spacingChecks entries must be objects")
    if "elements" in check and "instances" in check: raise ValueError("spacing check cannot mix elements and instances")
    key="elements" if "elements" in check else "instances"; pair=check.get(key)
    if not isinstance(pair,list) or len(pair)!=2: raise ValueError(f"spacing check needs exactly two {key}")
    by={item["elementId"]:item["order"] for item in paths} if key=="elements" else {item["order"]:item["order"] for item in paths}
    if any(isinstance(value,bool) or not isinstance(value,str if key=="elements" else int) or value not in by for value in pair):
        raise ValueError(f"spacing check references unknown {key}: {pair!r}")
    resolved=tuple(sorted(by[value] for value in pair))
    if resolved[0]==resolved[1]: raise ValueError("spacing check must reference two different elements")
    return resolved


def fmt(value: float) -> str:
    rounded=round(finite_number(value),4)
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
    points=[]; segments=[]; cursor=None; start=None; subpath_drawn=False
    def line(a,b):
        points.append(a); segments.append((a,b)); steps=max(2,math.ceil(math.dist(a,b)*density)); points.extend((a[0]+(b[0]-a[0])*i/steps,a[1]+(b[1]-a[1])*i/steps) for i in range(1,steps+1))
    for cmd in commands:
        if cmd.type=="M": cursor=start=cmd.points[0]; subpath_drawn=False
        elif cmd.type=="L": line(cursor,cmd.points[0]); cursor=cmd.points[0]; subpath_drawn=True
        elif cmd.type=="Q":
            points.append(cursor); subpath_drawn=True
            control,end=cmd.points; steps=max(8,math.ceil((math.dist(cursor,control)+math.dist(control,end))*density))
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
        elif cmd.type=="C":
            points.append(cursor); subpath_drawn=True
            first,second,end=cmd.points
            # Use control-polygon length so a curve with coincident endpoints
            # still has adequate samples; include derivative roots exactly for
            # trustworthy keyshape and clearance bounds.
            length=math.dist(cursor,first)+math.dist(first,second)+math.dist(second,end)
            steps=max(8,math.ceil(length*density))
            fractions=[i/steps for i in range(1,steps+1)]
            for axis in (0,1):
                p0,p1,p2,p3=cursor[axis],first[axis],second[axis],end[axis]
                a=-p0+3*p1-3*p2+p3; b=2*(p0-2*p1+p2); c=p1-p0
                if abs(a)<1e-12:
                    roots=[-c/b] if abs(b)>=1e-12 else []
                else:
                    discriminant=b*b-4*a*c
                    roots=[] if discriminant<0 else [(-b-math.sqrt(discriminant))/(2*a),(-b+math.sqrt(discriminant))/(2*a)]
                fractions.extend(root for root in roots if 0<root<1)
            for t in sorted(set(fractions)):
                u=1-t
                points.append(tuple(u*u*u*cursor[axis]+3*u*u*t*first[axis]+3*u*t*t*second[axis]+t*t*t*end[axis] for axis in (0,1)))
            cursor=end
        elif cmd.type=="A":
            # Reliable SVG arc sampling using the endpoint-to-centre conversion.
            end=cmd.points[0]; rx,ry,rotation,large,sweep=cmd.arc or (0,0,0,0,0)
            if cursor==end: continue  # SVG coincident-endpoint arcs draw nothing.
            points.append(cursor); subpath_drawn=True
            if not rx or not ry: line(cursor,end); cursor=end; continue
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
        elif cmd.type=="Z" and cursor and start:
            if subpath_drawn: line(cursor,start)
            cursor=start
    return points,segments
