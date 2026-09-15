"""Widen both rectangular straps equally from 16 to 24 units, keeping the dial centered. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6f3e245f-ff22-445c-9c0b-9969d193eb11'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-01/watch_6f3e245f-ff22-445c-9c0b-9969d193eb11.svg'
AUTHOR = 'gpt-6'

class AnalogueWristwatch(Solo48):
    icon_id = 'analogue-wristwatch'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('watch', 'wristwatch', 'time', 'clock', 'analogue', 'dial', 'strap', 'accessory')

    def build(self) -> None:
        """Symbol plan: Widen both rectangular straps equally from 16 to 24 units, keeping the dial centered. Reference: inspected current parent; no useful exact Lucide match selected."""
        cx, cy, rx, ry = (24, 24, 16, 12)
        for name, a, b in [('ne', (cx, cy - ry), (cx + rx, cy)), ('se', (cx + rx, cy), (cx, cy + ry)), ('sw', (cx, cy + ry), (cx - rx, cy)), ('nw', (cx - rx, cy), (cx, cy - ry))]:
            self.add_arc(name, a, b, radius_x=rx, radius_y=ry)
        self.add_contour('face', 'ne', 'se', 'sw', 'nw', closed=True)
        self.add_polyline('upper-strap', (24, 12), (12, 12), (12, 4), (36, 4), (36, 12), (24, 12))
        self.add_polyline('lower-strap', (24, 36), (12, 36), (12, 44), (36, 44), (36, 36), (24, 36))
        self.relate('connect', 'upper-strap', 'face')
        self.relate('connect', 'lower-strap', 'face')
        self.add_polyline('hands', (24, 21), (24, 26), (30, 26))
