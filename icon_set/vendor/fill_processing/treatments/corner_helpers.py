"""Pure corner helpers extracted from the reviewed fill/corner tools. See PROVENANCE.json."""
import math
import cmath
from svgpathtools import Arc, Line, Path
from shapely.geometry import Polygon, Point
EPS=1e-9
SMOOTH_TOL=2.0
CORNER_MIN_TURN=25.0

def unit(z):
    a = abs(z)
    return z / a if a > EPS else None


def tangent(seg, t):
    """Unit tangent of seg at t. Where a control point sits on its end point the derivative
    vanishes and svgpathtools falls back to one that can point BACKWARDS (a curl drawn
    ...C19.8 23 18 19.5 18 19.5); the direction the curve actually travels near t wins."""
    h = 1e-3
    a, b = (t, t + h) if t < 1 - h else (t - h, t)
    fd = unit(seg.point(b) - seg.point(a))
    try:
        u = seg.unit_tangent(t)
        if math.isfinite(u.real) and math.isfinite(u.imag) and abs(u) > 0.5:
            if fd is None or (u * fd.conjugate()).real > 0:
                return u
            return fd
    except (ValueError, ZeroDivisionError):
        pass
    if fd is not None:
        return fd
    h = 1e-4
    a, b = (t, t + h) if t < 1 - h else (t - h, t)
    return unit(seg.point(b) - seg.point(a))


def turn_deg(u, v):
    """Signed direction change (deg) going from direction u to direction v."""
    return math.degrees(cmath.phase(v / u))


def arc_between(p1, p2, r, u_in, u_out):
    cross = u_in.real * u_out.imag - u_in.imag * u_out.real
    return Arc(p1, complex(r, r), 0.0, False, cross > 0, p2)


def classify_boundary(path, ring_role='exterior'):
    """Classify one resolved simple closed contour, independently of path direction.

    For compound SVGs the caller must resolve fill-rule and nesting first and
    supply exterior/hole. Raw SVG subpath winding alone does not identify holes.
    """
    if ring_role not in {'exterior', 'hole'} or not path.isclosed():
        raise ValueError('Expected a closed contour with a resolved ring role')
    points = [s.point(k / 32) for s in path for k in range(32)]
    poly = Polygon([(z.real, z.imag) for z in points])
    if not poly.is_valid or poly.area < 1e-9:
        raise ValueError('Resolve invalid/self-intersecting contours before classifying')
    orientation = 1 if poly.exterior.is_ccw else -1
    material = 1 if ring_role == 'exterior' else -1
    result = []
    for i, b in enumerate(path):
        a = path[i-1]
        incoming, outgoing = tangent(a, 1), tangent(b, 0)
        if incoming is None or outgoing is None:
            raise ValueError('Undefined tangent requires review')
        turn = turn_deg(incoming, outgoing)
        kind = ('sharp' if abs(turn) >= CORNER_MIN_TURN else
                'kink' if abs(turn) >= SMOOTH_TOL else 'smooth')
        side = ('convex_black' if turn * orientation * material > 0 else 'concave_black')
        result.append(dict(segment=i, point=[b.start.real, b.start.imag],
                           tangent_jump_degrees=turn, kind=kind,
                           material_side=side if kind != 'smooth' else None,
                           line_line=isinstance(a, Line) and isinstance(b, Line)))
    return result


def rounded_ring(ring, role, radius, protected_boundary=None,minimum_radius=.02):
    pts=[complex(x,y) for x,y in ring.coords[:-1]]
    # Remove numerical collinearity, without flattening source curves.
    changed=True
    while changed and len(pts)>3:
        changed=False;new=[]
        for i,p in enumerate(pts):
            a=p-pts[i-1];b=pts[(i+1)%len(pts)]-p
            if abs(a)<1e-7 or abs(b)<1e-7 or (abs((a.conjugate()*b).imag)<1e-9*abs(a)*abs(b) and (a.conjugate()*b).real>0):changed=True
            else:new.append(p)
        pts=new
    path=Path(*[Line(p,pts[(i+1)%len(pts)]) for i,p in enumerate(pts)])
    records=classify_boundary(path,role)
    trims={};audits=[]
    for rec in records:
        if rec['kind']!='sharp':continue
        i=rec['segment'];row=dict(rec,ring_role=role)
        if protected_boundary is not None and protected_boundary.distance(Point(pts[i].real,pts[i].imag))<.02:
            row.update(action='keep',reason='Source detail contour explicitly protected by recipe')
        elif rec['material_side']!='convex_black':row.update(action='keep',reason='Concave black join')
        else:
            factor=math.tan(math.radians((180-abs(rec['tangent_jump_degrees']))/2))
            limit=min(path[i-1].length(),path[i].length())*.45*factor
            used=min(radius,limit)
            if used<minimum_radius:row.update(action='unresolved',reason='Available source arms too short',maximum_radius=limit)
            else:
                reach=used/factor;a=path[i-1];b=path[i]
                u=(a.end-a.start)/abs(a.end-a.start);v=(b.end-b.start)/abs(b.end-b.start)
                p1=pts[i]-reach*u;p2=pts[i]+reach*v
                trims[i]=(p1,p2,arc_between(p1,p2,used,u,v))
                row.update(action='round',radius=used,maximum_radius=limit)
        audits.append(row)
    segs=[]
    for i in range(len(pts)):
        start=trims[i][1] if i in trims else pts[i]
        j=(i+1)%len(pts);end=trims[j][0] if j in trims else pts[j]
        if abs(end-start)>1e-8:segs.append(Line(start,end))
        if j in trims:segs.append(trims[j][2])
    return Path(*segs),audits

