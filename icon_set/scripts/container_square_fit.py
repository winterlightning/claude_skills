"""Full unrotated square footprints inside bounded vector zones, in SVG units."""
import numpy as np
import shapely
from shapely.geometry import box


def square(center, size):
    x, y = center
    r = size/2
    return box(x-r, y-r, x+r, y+r)


def fit_center(zone, size, preferred=None):
    """Find a strictly feasible center, or None, using polygon configuration space.

    Sweeping each boundary segment by the square gives all forbidden centers.
    This includes holes and concave edges, unlike four-corner containment tests.
    A point/line-only feasible set is deliberately left for tolerance review.
    """
    minx,miny,maxx,maxy = zone.bounds
    r=size/2
    if maxx-minx <= size or maxy-miny <= size:
        return None
    for point in (preferred, (zone.centroid.x,zone.centroid.y), ((minx+maxx)/2,(miny+maxy)/2)):
        if point is not None and zone.covers(square(point,size)):
            return list(point)
    candidates = box(minx+r,miny+r,maxx-r,maxy-r).intersection(zone)
    offsets=np.array([[-r,-r],[-r,r],[r,r],[r,-r]])
    sweeps=[]
    polygons=[zone] if zone.geom_type=='Polygon' else list(zone.geoms)
    for polygon in polygons:
        for ring in [polygon.exterior,*polygon.interiors]:
            coords=np.asarray(ring.coords)
            points=np.concatenate((coords[:-1,None,:]+offsets,coords[1:,None,:]+offsets),axis=1)
            hulls=shapely.convex_hull(shapely.multipoints(points))
            sweeps.extend(hulls[shapely.intersects(hulls,candidates)])
    free=candidates.difference(shapely.union_all(sweeps))
    if free.is_empty:
        return None
    pieces=[free] if free.geom_type=='Polygon' else list(getattr(free,'geoms',[]))
    for piece in sorted(pieces,key=lambda p:p.area,reverse=True):
        if piece.area<=1e-16:
            continue
        p=piece.representative_point()
        center=[p.x,p.y]
        if zone.covers(square(center,size)):
            return center
    return None


def assess_square(inner,outer,size,preferred=None):
    center=fit_center(inner,size,preferred)
    if center is not None:
        return {'status':'fits','size_units':size,'placement_center_units':center,
                'fits_at_preferred_center':bool(preferred is not None and inner.covers(square(preferred,size)))}
    # Small outward guard avoids calling exact/borderline contacts impossible.
    possible=fit_center(outer.buffer(0.00001,quad_segs=8),size,preferred)
    return {'status':'too-small' if possible is None else 'borderline','size_units':size,
            'placement_center_units':None,'fits_at_preferred_center':False}
