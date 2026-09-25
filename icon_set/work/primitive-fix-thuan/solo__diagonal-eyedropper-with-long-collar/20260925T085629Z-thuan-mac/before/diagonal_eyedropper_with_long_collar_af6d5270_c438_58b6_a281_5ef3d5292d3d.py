"""Eye Dropper Pipette Tool.
Plan: Long diagonal pipette with a rounded lower nozzle and projecting collar. Centerline extremes (6,6)-(42,42).
Construction: Lucide pipette; split collar attachments.
Reduction: Fine source irregularities removed.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'af6d5270-c438-58b6-a281-5ef3d5292d3d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/color picker_af6d5270-c438-58b6-a281-5ef3d5292d3d.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/color picker_af6d5270-c438-58b6-a281-5ef3d5292d3d.svg'

def _run(icon, name, *points):
    for i,(a,b) in enumerate(zip(points,points[1:]),1):
        icon.add_line(f'{name}-{i}',a,b)

def _circle(icon, name, cx, cy, radius):
    a,b=(cx-radius,cy),(cx+radius,cy)
    icon.add_arc(name+'-a',a,b,radius_x=radius)
    icon.add_arc(name+'-b',b,a,radius_x=radius)
    icon.add_contour(name,name+'-a',name+'-b',closed=True)


class Drawing(Solo48):
    icon_id = 'diagonal-eyedropper-with-long-collar'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'state')
    aliases = ()
    keywords = ('eye', 'dropper', 'pipette', 'tool')

    def build(self):
        # Upper-right bulb uses a cardinal quarter-circle; lower body follows the diagonal.
        self.add_line('bulb-start',(26,12),(32,6))
        self.add_arc('bulb-round',(32,6),(42,16),radius_x=10)
        self.add_line('bulb-end',(42,16),(36,22))
        self.add_contour('bulb','bulb-start','bulb-round','bulb-end')
        _run(self,'body-a',(26,12),(8,30),(6,36))
        self.add_arc('nozzle-round',(6,36),(12,42),radius_x=6,sweep=False)
        _run(self,'body-b',(12,42),(18,40),(36,22))
        self.add_contour('body','body-a-1','body-a-2','nozzle-round','body-b-1','body-b-2')
        self.add_polyline('collar',(22,8),(26,12),(36,22),(40,26))
        for a,c in [('bulb','body'),('bulb','collar'),('body','collar')]: self.relate('connect',a,c)
