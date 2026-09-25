"""Overlapping Transparent Squares.
Plan: Two equal offset squares and one diagonal hatch through their shared area; crossings use common nodes. Centerline extremes (6,6)-(42,42).
Construction: Lucide shapes: equal geometric outlines.
Reduction: Hatching reduced to one clear diagonal; selected outline breaks closed for legibility.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cc7d5e55-b157-42d9-bbde-a090d43002ca'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/transparent 1_cc7d5e55-b157-42d9-bbde-a090d43002ca.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/transparent 1_cc7d5e55-b157-42d9-bbde-a090d43002ca.svg'

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
    icon_id = 'overlapping-squares-with-diagonal-hatching'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('overlapping', 'transparent', 'squares')

    def build(self):
        self.add_polyline('rear',(6,6),(30,6),(30,18),(30,30),(18,30),(6,30),closed=True)
        self.add_polyline('front',(18,18),(30,18),(42,18),(42,42),(18,42),(18,30),closed=True)
        self.relate('connect','rear','front')
        self.add_line('hatch',(18,18),(30,30))
        self.relate('connect','hatch','rear');self.relate('connect','hatch','front')
