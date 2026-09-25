"""Liquid Glue Bottle.
Plan: Symmetric round bottle, tall pointed nozzle and three-sided front label. Centerline extremes (10,4)-(38,44).
Construction: Lucide milk: rounded bottle and centered neck.
Reduction: Extra collar seam omitted to retain a readable label and tall nozzle.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '40ae207b-f64d-5dde-8b1a-535ab6ebc92e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/design tool glue_40ae207b-f64d-5dde-8b1a-535ab6ebc92e.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/design tool glue_40ae207b-f64d-5dde-8b1a-535ab6ebc92e.svg'

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
    icon_id = 'rounded-glue-bottle-with-open-label'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('liquid', 'glue', 'bottle')

    def build(self):
        axis=24
        _box(self,'body',10,18,38,44,4,top_nodes=(18,30))
        self.add_polyline('nozzle',(axis-6,18),(axis,4),(axis+6,18))
        self.relate('connect','nozzle','body')
        self.add_polyline('label',(28,27),(20,27),(20,35),(28,35))
