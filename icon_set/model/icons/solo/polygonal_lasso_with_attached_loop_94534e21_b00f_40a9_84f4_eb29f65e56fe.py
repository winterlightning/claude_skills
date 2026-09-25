"""Polygonal Lasso Selection Tool.
Plan: Irregular polygon joined at two explicit nodes to a 16 by 12 oval loop, with a curved tail. Centerline extremes (6,6)-(42,42).
Construction: Lucide lasso: joined loop and tail.
Reduction: Polygon retains its deliberate irregularity; loop regularized.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '94534e21-b00f-40a9-84f4-eb29f65e56fe'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/polygon lasso_94534e21-b00f-40a9-84f4-eb29f65e56fe.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/polygon lasso_94534e21-b00f-40a9-84f4-eb29f65e56fe.svg'

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
    icon_id = 'polygonal-lasso-with-attached-loop'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('polygonal', 'lasso', 'selection', 'tool')

    def build(self):
        self.add_polyline('selection',(12,34),(6,6),(28,12),(42,6),(40,26),(28,34))
        self.add_arc('loop-top',(12,34),(28,34),radius_x=8,radius_y=6)
        self.add_arc('loop-bottom',(28,34),(12,34),radius_x=8,radius_y=6)
        self.add_contour('loop','loop-top','loop-bottom',closed=True)
        self.relate('connect','loop','selection')
        self.add_arc('tail',(28,34),(36,42),radius_x=8,radius_y=8);self.relate('connect','tail','loop');self.relate('connect','tail','selection')
