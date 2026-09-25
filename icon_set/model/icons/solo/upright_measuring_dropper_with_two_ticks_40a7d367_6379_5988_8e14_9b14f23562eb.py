"""Medicine Eyedropper Pipette Tool.
Plan: Upright dropper with rounded bulb, two regular measuring ticks and a short lower nozzle. Centerline extremes (10,4)-(38,44).
Construction: Lucide pipette: bulb, crossbar and attached graduations.
Reduction: Extraction irregularities removed; identifying parts retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '40a7d367-6379-5988-8e14-9b14f23562eb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/picker_40a7d367-6379-5988-8e14-9b14f23562eb.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/picker_40a7d367-6379-5988-8e14-9b14f23562eb.svg'

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
    icon_id = 'upright-measuring-dropper-with-two-ticks'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('medicine', 'eyedropper', 'pipette', 'tool')

    def build(self):
        self.add_arc('bulb',(14,14),(34,14),radius_x=10)
        _run(self,'right',(34,14),(34,18),(34,34))
        self.add_arc('right-shoulder',(34,34),(28,40),radius_x=6)
        _run(self,'nozzle',(28,40),(28,44),(20,44),(20,40))
        self.add_arc('left-shoulder',(20,40),(14,34),radius_x=6)
        _run(self,'left',(14,34),(14,26),(14,18),(14,14))
        self.add_contour('body','bulb','right-1','right-2','right-shoulder','nozzle-1','nozzle-2','nozzle-3','left-shoulder','left-1','left-2','left-3',closed=True)
        self.add_polyline('collar',(10,18),(14,18),(34,18),(38,18));self.relate('connect','collar','body')
        for i in range(2):
         y=26+i*8
         self.add_line(f'tick-{i}',(14,y),(22,y));self.relate('connect',f'tick-{i}','body')
