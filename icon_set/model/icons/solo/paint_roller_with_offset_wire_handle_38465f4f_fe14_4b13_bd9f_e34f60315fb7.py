"""Paint Roller Brush.
Plan: Horizontal roller, offset bent arm and centered lower capsule grip. Centerline extremes (6,6)-(42,42).
Construction: Lucide paint-roller: rounded roller and orthogonal return arm.
Reduction: Extraction irregularities removed; identifying parts retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '38465f4f-fe14-4b13-bd9f-e34f60315fb7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/rolling brush_38465f4f-fe14-4b13-bd9f-e34f60315fb7.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/rolling brush_38465f4f-fe14-4b13-bd9f-e34f60315fb7.svg'

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
    icon_id = 'paint-roller-with-offset-wire-handle'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/design'
    aliases = ()
    keywords = ('paint', 'roller', 'brush')

    def build(self):
        _box(self,'roller',6,6,34,18,4)
        self.add_line('arm-top',(34,12),(38,12))
        self.add_arc('arm-corner',(38,12),(42,16),radius_x=4)
        self.add_line('arm-side',(42,16),(42,22))
        self.add_arc('arm-turn',(42,22),(38,26),radius_x=4)
        self.add_line('arm-lower',(38,26),(28,26))
        self.add_arc('arm-neck',(28,26),(24,30),radius_x=4,sweep=False)
        self.add_contour('arm','arm-top','arm-corner','arm-side','arm-turn','arm-lower','arm-neck')
        _box(self,'grip',20,30,28,42,4)
        self.relate('connect','arm','roller');self.relate('connect','arm','grip')
