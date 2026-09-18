"""Elevator Doors with Directional Arrows.
Symbol plan: Symmetric frame and central door seam; opposing controls convey elevator directions. Bounds (2,6)-(46,42).
Construction: Lucide battery for tangent rounded rectangles; shared human reference for people.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import rounded_rect, circle
SOURCE_ICON_ID = '3b975376-341b-48a1-92cf-f4ed4b0af1eb'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/3b975376-341b-48a1-92cf-f4ed4b0af1eb.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'elevator-direction-doors'
    keyshape = Keyshape.HRECT_L
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('elevator doors with directional arrows',)
    def build(self):
        # Direction indicators above the doors keep both arrows readable.
        rounded_rect(self,'frame',4,20,44,40,4)
        self.add_line('door-seam',(24,20),(24,40))
        self.relate('connect','frame','door-seam')
        self.add_polyline('up',(8,11),(14,8),(20,11))
        self.add_polyline('down',(28,8),(34,11),(40,8))
