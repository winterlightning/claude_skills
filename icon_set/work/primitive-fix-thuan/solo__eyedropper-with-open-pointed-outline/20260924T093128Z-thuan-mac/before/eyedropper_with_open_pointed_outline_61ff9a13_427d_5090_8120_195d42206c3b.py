"""Eyedropper Color Picker Tool.
Plan: Short diagonal pipette above the unresolved rounded open outline. Centerline extremes (6,6)-(42,42).
Construction: Lucide pipette; simple rounded bulb.
Reduction: No heart or liquid identity invented; open contour preserved, tool details simplified.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '61ff9a13-427d-5090-8120-195d42206c3b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/color picker 1_61ff9a13-427d-5090-8120-195d42206c3b.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/color picker 1_61ff9a13-427d-5090-8120-195d42206c3b.svg'

def _run(icon, name, *points):
    for i,(a,b) in enumerate(zip(points,points[1:]),1):
        icon.add_line(f'{name}-{i}',a,b)

def _circle(icon, name, cx, cy, radius):
    a,b=(cx-radius,cy),(cx+radius,cy)
    icon.add_arc(name+'-a',a,b,radius_x=radius)
    icon.add_arc(name+'-b',b,a,radius_x=radius)
    icon.add_contour(name,name+'-a',name+'-b',closed=True)


class Drawing(Solo48):
    icon_id = 'eyedropper-with-open-pointed-outline'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/design'
    aliases = ()
    keywords = ('eyedropper', 'color', 'picker', 'tool')

    def build(self):
        self.add_arc('bulb',(32,6),(42,16),radius_x=10)
        _run(self,'tool',(42,16),(28,30),(22,30),(20,24),(26,18),(26,12),(32,6))
        self.add_contour('pipette','bulb','tool-1','tool-2','tool-3','tool-4','tool-5','tool-6',closed=True)
        self.add_polyline('collar',(22,8),(26,12),(32,18),(36,22))
        self.relate('connect','pipette','collar')
        self.add_arc('open-left',(12,22),(6,28),radius_x=6,sweep=False)
        _run(self,'open-bottom',(6,28),(16,42),(22,40))
        self.add_contour('open-outline','open-left','open-bottom-1','open-bottom-2')
