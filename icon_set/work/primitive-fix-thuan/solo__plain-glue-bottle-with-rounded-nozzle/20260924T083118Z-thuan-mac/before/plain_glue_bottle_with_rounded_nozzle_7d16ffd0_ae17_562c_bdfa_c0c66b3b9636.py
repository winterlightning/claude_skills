"""Liquid Glue Bottle.
Plan: Symmetric plain squeeze bottle with a broad rounded base and a rounded tapered nozzle. Centerline extremes (10,4)-(38,44).
Construction: Lucide milk: simple rounded bottle.
Reduction: Extra collar band omitted; no label added to the plain body.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7d16ffd0-ae17-562c-bdfa-c0c66b3b9636'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/design tool paper glue_7d16ffd0-ae17-562c-bdfa-c0c66b3b9636.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/design tool paper glue_7d16ffd0-ae17-562c-bdfa-c0c66b3b9636.svg'

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
    icon_id = 'plain-glue-bottle-with-rounded-nozzle'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/design'
    aliases = ()
    keywords = ('liquid', 'glue', 'bottle')

    def build(self):
        _box(self,'body',10,18,38,44,6)
        self.add_line('nozzle-left',(16,18),(20,8))
        self.add_arc('tip',(20,8),(28,8),radius_x=4)
        self.add_line('nozzle-right',(28,8),(32,18))
        self.add_contour('nozzle','nozzle-left','tip','nozzle-right')
        self.relate('connect','nozzle','body')
