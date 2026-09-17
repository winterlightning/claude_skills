"""Isometric Cube With Connected Nodes.
Plan: Central three-face cube with three small linked terminal rings. Centerline extremes (6,6)-(42,42).
Construction: Lucide box: three visible faces and exact Y junction.
Reduction: Hexagonal node outlines simplified to small terminal rings; full hexagons cannot coexist with three readable cube faces at the required spacing.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3be3c4f1-7eff-4665-918c-5125daa70608'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/scale 3d_3be3c4f1-7eff-4665-918c-5125daa70608.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/scale 3d_3be3c4f1-7eff-4665-918c-5125daa70608.svg'

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
    icon_id = 'isometric-cube-with-three-linked-hexagons'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/design'
    aliases = ()
    keywords = ('isometric', 'cube', 'with', 'connected', 'nodes')

    def build(self):
        axis=24
        self.add_polyline('cube',(24,18),(32,23),(32,33),(24,38),(16,33),(16,23),closed=True)
        self.add_polyline('faces',(16,23),(24,28),(32,23))
        self.add_line('upright',(24,28),(24,38))
        for a,b in [('cube','faces'),('cube','upright'),('faces','upright')]:self.relate('connect',a,b)
        for name,cx,cy in [('top',axis,8),('left',8,40),('right',40,40)]:
            points=[(cx,cy-2),(cx+2,cy),(cx,cy+2),(cx-2,cy),(cx,cy-2)]
            for i,(a,b) in enumerate(zip(points,points[1:])):self.add_arc(name+f'-{i}',a,b,radius_x=2)
            self.add_contour(name,*[name+f'-{i}' for i in range(4)],closed=True)
        for name,a,b in [('top',(24,10),(24,18)),('left',(16,33),(10,40)),('right',(32,33),(38,40))]:
            self.add_line(name+'-stem',a,b)
            self.relate('connect',name+'-stem','cube')
            self.relate('connect',name+'-stem',name)
