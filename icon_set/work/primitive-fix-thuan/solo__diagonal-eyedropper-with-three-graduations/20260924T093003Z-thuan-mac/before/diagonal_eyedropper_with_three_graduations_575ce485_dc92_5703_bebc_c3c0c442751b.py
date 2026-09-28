"""Liquid Measuring Eyedropper Tool.
Plan: Broad diagonal pipette with three equally spaced graduations attached to one shaft wall. Centerline extremes (6,6)-(42,42).
Construction: Lucide pipette: collar and coherent body.
Reduction: Small nozzle wiggles removed; all three graduations retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '575ce485-dc92-5703-bebc-c3c0c442751b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/picker_575ce485-dc92-5703-bebc-c3c0c442751b.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/picker_575ce485-dc92-5703-bebc-c3c0c442751b.svg'

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
    icon_id = 'diagonal-eyedropper-with-three-graduations'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/design'
    aliases = ()
    keywords = ('liquid', 'measuring', 'eyedropper', 'tool')

    def build(self):
        self.add_line('bulb-start',(26,10),(30,6))
        self.add_arc('bulb',(30,6),(42,18),radius_x=12)
        self.add_line('bulb-end',(42,18),(36,20))
        self.add_contour('upper','bulb-start','bulb','bulb-end')
        self.add_polyline('body',(26,10),(20,16),(14,22),(8,28),(6,42),(16,40),(36,20))
        self.add_polyline('collar',(22,6),(26,10),(36,20),(40,24))
        for a,c in [('upper','body'),('upper','collar'),('body','collar')]:self.relate('connect',a,c)
        for i in range(3):
         x,y=20-6*i,16+6*i
         self.add_line(f'tick-{i}',(x,y),(x+4,y+4));self.relate('connect',f'tick-{i}','body')
