"""Round new convex black corners after composition; never round Sharp outputs."""
import xml.etree.ElementTree as ET
import math
from shapely import set_precision
from shapely.geometry import Point
from shapely.ops import unary_union
from .corner_helpers import rounded_ring
from .geometry import NS, clean, topology, read_export, fu, serialize


def round_sampled_corners(geometry, records, radius, corner_records=None):
    """Round curve/line junctions independently of adaptive sample edge length.

    A rolling disk opening acts on the affected connected component without a
    clipped patch seam. Reduce the disk until at least 97% of its area remains.
    Loss beyond a .01-unit contour tolerance outside detected corner neighborhoods
    must stay below .001 square units: a topology check alone misses a thin leg becoming a bead on a neck.
    Never add material or delete a component/hole.
    """
    result=geometry; audits=[]
    original_pieces=fu.to_polys(geometry)
    allowed_corners=[r for r in (corner_records or records) if r.get('material_side','convex_black')=='convex_black']
    for record in records:
        point=Point(record['point'])
        if result.distance(point)>.00001:
            audits.append(dict(record,action='round',method='shared_fillet_neighborhood',
                               radius=None,removed_area=0,corner_clearance=result.distance(point)))
            continue
        pieces=fu.to_polys(result)
        index=min(range(len(pieces)),key=lambda i:pieces[i].distance(point))
        component=pieces[index]
        original_index=min(range(len(original_pieces)),key=lambda i:original_pieces[i].distance(point))
        component_records=[r for r in allowed_corners if min(range(len(original_pieces)),
            key=lambda i:original_pieces[i].distance(Point(r['point'])))==original_index]
        # Operate on the connected component, without a circular clip seam.
        # Thin semantic islands retain at least 97% of their material.
        for attempt in range(12):
            used=radius/(2**attempt)
            opened=component.buffer(-used,quad_segs=64).buffer(used,quad_segs=64).intersection(component)
            opened=clean(set_precision(opened,.000001))
            neighborhoods=[]
            for corner in component_records:
                factor=max(.02,math.tan(math.radians((180-abs(corner['tangent_jump_degrees']))/2)))
                neighborhoods.append(Point(corner['point']).buffer(radius/factor+radius,quad_segs=64))
            # Validate the un-clipped opening. Clipping its subtraction to these
            # masks would introduce seams/new sharp corners at the mask boundary.
            allowed=unary_union(neighborhoods)
            protected_loss=component.difference(opened).difference(allowed).area
            # Buffer booleans can shave sub-.01-unit strips off long straight
            # edges. Measure displacement as well as area so numerical strips
            # do not force asymmetric radii, while damaged legs still fail.
            displaced_loss=component.difference(opened.buffer(.01,quad_segs=64)).difference(allowed).area
            if (not opened.is_empty and topology(opened)==topology(component)
                and opened.area>=component.area*.97 and opened.distance(point)>.00001
                and displaced_loss<.001):
                pieces[index]=opened;candidate=clean(unary_union(pieces))
                if topology(candidate)!=topology(result):continue
                removed_area=component.area-opened.area
                result=candidate
                audits.append(dict(record,action='round',method='component_rolling_disk',radius=used,
                                   removed_area=removed_area,protected_contour_loss_area=protected_loss,
                                   contour_tolerance=.01,protected_displaced_loss_area=displaced_loss,
                                   corner_clearance=opened.distance(point)))
                break
        else:raise ValueError('Cannot fit a topology-preserving curved-corner fillet')

    return result,audits


def round_export(geometry, destination, radius=2):
    if radius <= 0:
        raise ValueError('Round radius must be positive')
    geometry = clean(set_precision(geometry, .000001)).simplify(.00001, preserve_topology=True)
    before = topology(geometry)
    for attempt in range(5):
        paths, decisions = [], []
        for pi, polygon in enumerate(fu.to_polys(geometry)):
            for ri, ring in enumerate([polygon.exterior, *polygon.interiors]):
                # Avoid consuming a small positive semantic island with a full-size fillet.
                local_radius=min(radius/(2**attempt), math.sqrt(polygon.area)*.15)
                path, rows = rounded_ring(ring, 'exterior' if ri == 0 else 'hole', local_radius)
                paths.append(path.d())
                decisions.extend(dict(row, component=pi, ring=ri) for row in rows)
        root = ET.Element(NS+'svg', viewBox='0 0 48 48', width='48', height='48', fill='currentColor', stroke='none')
        ET.SubElement(root, NS+'path', {'d': ' '.join(paths), 'fill-rule': 'evenodd'})
        ET.ElementTree(root).write(destination, encoding='unicode')
        actual = read_export(destination)
        added = actual.difference(geometry).area
        if actual.is_valid and not actual.is_empty and topology(actual) == before and added < .005:
            unresolved = [r for r in decisions if r['action'] == 'unresolved']
            if unresolved:
                actual,repaired=round_sampled_corners(actual,unresolved,radius/(2**attempt),corner_records=decisions)
                destination.write_text(serialize(actual))
                actual=read_export(destination)
                if topology(actual)!=before or actual.difference(geometry).area>=.005:
                    raise ValueError(f'Final curved-corner export changed topology {before} -> {topology(actual)} or added material {actual.difference(geometry).area}')
                decisions=[r for r in decisions if r['action']!='unresolved']+repaired
            return actual, {'desired_radius': radius, 'applied_radius': radius/(2**attempt),
                            'topology_preserved': True, 'added_area': added,
                            'rounded_count': sum(r['action'] == 'round' for r in decisions),
                            'decisions': decisions}
    raise ValueError('Round treatment changed topology or added material')
