"""Right Angle Corner Join.
Plan: Two orthogonal strips form a broad L; overlap is an explicit square junction. Centerline extremes (6,6)-(42,42).
Construction: Lucide ruler: broad rectilinear bands.
Reduction: Small inset notch removed; square overlap retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fdab50b0-a0e7-41c3-80ad-e3c8d99ea264'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/straight join_fdab50b0-a0e7-41c3-80ad-e3c8d99ea264.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/straight join_fdab50b0-a0e7-41c3-80ad-e3c8d99ea264.svg'

def _run(icon, name, *points):
    for i,(a,b) in enumerate(zip(points,points[1:]),1):
        icon.add_line(f'{name}-{i}',a,b)

def _circle(icon,name,cx,cy,r):
    a,b=(cx-r,cy),(cx+r,cy)
    icon.add_arc(name+'-a',a,b,radius_x=r)
    icon.add_arc(name+'-b',b,a,radius_x=r)
    icon.add_contour(name,name+'-a',name+'-b',closed=True)

def _box(icon,name,l,t,r,b,rad,top_nodes=()):
    xs=[l+rad]+sorted(x for x in top_nodes if l+rad<x<r-rad)+[r-rad]
    _run(icon,name+'-top',*[(x,t) for x in xs])
    icon.add_arc(name+'-tr',(r-rad,t),(r,t+rad),radius_x=rad)
    icon.add_line(name+'-right',(r,t+rad),(r,b-rad))
    icon.add_arc(name+'-br',(r,b-rad),(r-rad,b),radius_x=rad)
    icon.add_line(name+'-bottom',(r-rad,b),(l+rad,b))
    icon.add_arc(name+'-bl',(l+rad,b),(l,b-rad),radius_x=rad)
    icon.add_line(name+'-left',(l,b-rad),(l,t+rad))
    icon.add_arc(name+'-tl',(l,t+rad),(l+rad,t),radius_x=rad)
    icon.add_contour(name,*[name+f'-top-{i}' for i in range(1,len(xs))],*[name+'-'+s for s in ('tr','right','br','bottom','bl','left','tl')],closed=True)

class Drawing(Solo48):
    icon_id = 'right-angle-join-with-overlapping-strips'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/design'
    aliases = ()
    keywords = ('right', 'angle', 'corner', 'join')

    def build(self):
        self.add_polyline('outline',(6,6),(42,6),(42,18),(42,26),(26,26),(26,42),(18,42),(6,42),closed=True)
        self.add_polyline('seam',(42,18),(18,18),(18,42));self.relate('connect','seam','outline')
        self.add_polyline('overlap',(18,26),(26,26),(26,18));self.relate('connect','overlap','outline');self.relate('connect','overlap','seam')
