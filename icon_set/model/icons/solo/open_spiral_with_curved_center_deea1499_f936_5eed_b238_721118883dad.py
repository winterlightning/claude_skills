"""Hypnotic Swirl Symbol.
Plan: One clockwise spiral; tangent quarter circles with decreasing radii own the winding and central hook. Centerline extremes (6,6)-(42,42).
Construction: Lucide orbit: coherent circular arcs; no exact spiral match.
Reduction: Fewer broad turns preserve the open coil and hook with legal separation.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'deea1499-f936-5eed-b238-721118883dad'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/spiral shape_deea1499-f936-5eed-b238-721118883dad.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/spiral shape_deea1499-f936-5eed-b238-721118883dad.svg'

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
    icon_id = 'open-spiral-with-curved-center'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('hypnotic', 'swirl', 'symbol')

    def build(self):
        points=[(24,6),(42,24),(24,42),(6,24),(16,14),(26,24),(22,28),(18,24)]
        radii=[18,18,18,10,10,4,4]
        for i,(a,c,r) in enumerate(zip(points,points[1:],radii)):
         self.add_arc(f'coil-{i}',a,c,radius_x=r)
        self.add_contour('spiral',*[f'coil-{i}' for i in range(len(radii))])
