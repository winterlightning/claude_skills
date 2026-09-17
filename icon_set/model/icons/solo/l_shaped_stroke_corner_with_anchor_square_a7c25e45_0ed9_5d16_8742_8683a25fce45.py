"""Inside Stroke Alignment.
Plan: Orthogonal L-shaped stroke with a square anchor centered on its lower-left corner; intersections are explicit nodes. Centerline extremes (6,6)-(42,42).
Construction: Lucide shapes: exact square corners and shared junctions.
Reduction: Extraction irregularities removed; identifying parts retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a7c25e45-0ed9-5d16-8742-8683a25fce45'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/align stroke to inside_a7c25e45-0ed9-5d16-8742-8683a25fce45.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/align stroke to inside_a7c25e45-0ed9-5d16-8742-8683a25fce45.svg'

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
    icon_id = 'l-shaped-stroke-corner-with-anchor-square'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/design'
    aliases = ()
    keywords = ('inside', 'stroke', 'alignment')

    def build(self):
        self.add_polyline('stroke',(14,6),(30,6),(30,18),(42,18),(42,34),(22,34),(14,34),(14,26),(14,6),closed=True)
        self.add_polyline('anchor',(6,26),(14,26),(22,26),(22,34),(22,42),(6,42),closed=True)
        self.relate('connect','stroke','anchor')
