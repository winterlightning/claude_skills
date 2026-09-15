"""Shared SOLO48 construction: coherent curves, equal radii, actual junctions.

Geometry helpers only; the individual icon module owns subject/layout choices.
"""
from dataclasses import replace
from ...primitives import Line, Point


def path(icon, name, start, *commands, closed=False):
    members=[]; cursor=start
    for i, command in enumerate(commands):
        kind,*args=command; end=args[-1]; eid=f'{name}-{i+1}'
        if kind=='L': icon.add_line(eid,cursor,end)
        elif kind=='C': icon.add_bezier(eid,cursor,tuple(args))
        elif kind=='A': icon.add_arc(eid,cursor,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
        else: raise ValueError(kind)
        members.append(eid);cursor=end
    icon.add_contour(name,*members,closed=closed)


def ellipse(icon,name,cx,cy,rx,ry=None):
    ry=rx if ry is None else ry
    path(icon,name,(cx-rx,cy),('A',rx,ry,True,(cx,cy-ry)),
         ('A',rx,ry,True,(cx+rx,cy)),('A',rx,ry,True,(cx,cy+ry)),
         ('A',rx,ry,True,(cx-rx,cy)),closed=True)


def box(icon,name,l,t,r,b,radius=4,*,xs=(),ys=()):
    """Rounded rectangle with optional exact edge attachment nodes."""
    q=radius; commands=[]
    for x in sorted(set(xs)):
        if l+q<x<r-q: commands.append(('L',(x,t)))
    commands.extend([('L',(r-q,t)),('A',q,q,True,(r,t+q))])
    for y in sorted(set(ys)):
        if t+q<y<b-q: commands.append(('L',(r,y)))
    commands.extend([('L',(r,b-q)),('A',q,q,True,(r-q,b))])
    for x in sorted(set(xs),reverse=True):
        if l+q<x<r-q: commands.append(('L',(x,b)))
    commands.extend([('L',(l+q,b)),('A',q,q,True,(l,b-q))])
    for y in sorted(set(ys),reverse=True):
        if t+q<y<b-q: commands.append(('L',(l,y)))
    commands.extend([('L',(l,t+q)),('A',q,q,True,(l+q,t))])
    path(icon,name,(l+q,t),*commands,closed=True)


def line(icon,name,a,b): icon.add_line(name,a,b)


def poly(icon,name,*points,closed=False): icon.add_polyline(name,*points,closed=closed)


def contacts(icon):
    """Declare only paths with an actually shared authored endpoint."""
    # Split receiving straight walls where an authored part terminates. This
    # preserves the line exactly and exposes its real attachment to validation.
    endpoints={point.as_tuple() for p in icon.primitives for point in (p.start,p.end)}
    replacements={}; primitives=[]
    for p in icon.primitives:
        if not isinstance(p,Line) or p.start==p.end:
            primitives.append(p);continue
        a=p.start.as_tuple();b=p.end.as_tuple();dx=b[0]-a[0];dy=b[1]-a[1]
        inside=[q for q in endpoints if (q[0]-a[0])*dy==(q[1]-a[1])*dx
                and 0<(q[0]-a[0])*dx+(q[1]-a[1])*dy<dx*dx+dy*dy]
        if not inside:
            primitives.append(p);continue
        points=[a]+sorted(inside,key=lambda q:(q[0]-a[0])*dx+(q[1]-a[1])*dy)+[b]
        pieces=[Line(f'{p.element_id}-part-{i+1}',Point(*u),Point(*v)) for i,(u,v) in enumerate(zip(points,points[1:]))]
        replacements[p.element_id]=tuple(piece.element_id for piece in pieces);primitives.extend(pieces)
    icon.primitives=primitives
    icon.contours=[replace(c,members=tuple(member for old in c.members for member in replacements.get(old,(old,)))) for c in icon.contours]
    drawing=icon.draw();by_id=drawing.by_id();claimed=set();paths=[]
    for contour in drawing.contours:
        points=set()
        for member in contour.members:
            p=by_id[member];points.update((p.start.as_tuple(),p.end.as_tuple()));claimed.add(member)
        paths.append((contour.contour_id,points))
    for p in drawing.primitives:
        if p.element_id not in claimed: paths.append((p.element_id,{p.start.as_tuple(),p.end.as_tuple()}))
    for i,(name,points) in enumerate(paths):
        for other,other_points in paths[i+1:]:
            if points & other_points: icon.relate('connect',name,other)
