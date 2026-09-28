"""Eyedropper Color Selection Tool.
Plan: Broad diagonal pipette with a softly squared bulb and crossbar. Centerline extremes (6,6)-(42,42).
Construction: Lucide pipette; collar and body joins.
Reduction: Fine nozzle irregularities replaced with a rounded tip.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8ba14a04-c8da-5278-9772-abe74358faf2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/color picker_8ba14a04-c8da-5278-9772-abe74358faf2.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/color picker_8ba14a04-c8da-5278-9772-abe74358faf2.svg'

def _run(icon, name, *points):
    for i,(a,b) in enumerate(zip(points,points[1:]),1):
        icon.add_line(f'{name}-{i}',a,b)

def _circle(icon, name, cx, cy, radius):
    a,b=(cx-radius,cy),(cx+radius,cy)
    icon.add_arc(name+'-a',a,b,radius_x=radius)
    icon.add_arc(name+'-b',b,a,radius_x=radius)
    icon.add_contour(name,name+'-a',name+'-b',closed=True)


class Drawing(Solo48):
    icon_id = 'broad-diagonal-eyedropper-with-crossbar'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/design'
    aliases = ()
    keywords = ('eyedropper', 'color', 'selection', 'tool')

    def build(self):
        # Upper-right bulb uses a cardinal quarter-circle; lower body follows the diagonal.
        self.add_line('bulb-start',(24,14),(32,6))
        self.add_arc('bulb-round',(32,6),(42,16),radius_x=10)
        self.add_line('bulb-end',(42,16),(36,24))
        self.add_contour('bulb','bulb-start','bulb-round','bulb-end')
        _run(self,'body-a',(24,14),(8,30),(6,36))
        self.add_arc('nozzle-round',(6,36),(12,42),radius_x=6,sweep=False)
        _run(self,'body-b',(12,42),(18,40),(36,24))
        self.add_contour('body','body-a-1','body-a-2','nozzle-round','body-b-1','body-b-2')
        self.add_polyline('collar',(20,10),(24,14),(36,24),(38,28))
        for a,c in [('bulb','body'),('bulb','collar'),('body','collar')]: self.relate('connect',a,c)
