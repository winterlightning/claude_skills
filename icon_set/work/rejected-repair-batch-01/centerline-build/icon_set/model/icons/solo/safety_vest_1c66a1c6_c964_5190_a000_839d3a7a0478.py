'A sleeveless safety vest is shown from the front with a deep V neckline and curved armholes. Two horizontal bands cross the waist, and a central opening divides the rounded lower panels.\n\nConstruction: Sleeveless vest with deep V neck, central opening and one reflective band. Bounds (8,4)-(40,44).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1c66a1c6-c964-5190-a000-839d3a7a0478'
SOURCE_PATH = 'pictographic-primitives/wayfinding/safety vest_1c66a1c6-c964-5190-a000-839d3a7a0478.svg'
AUTHOR = 'gpt-6'

class SafetyVest(Solo48):
    icon_id = 'safety-vest'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('vest', 'safety', 'clothing', 'reflective', 'workwear', 'garment')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('outline-1', (8, 4), (16, 4))
        self.add_line('outline-2', (16, 4), (24, 20))
        self.add_line('outline-3', (24, 20), (32, 4))
        self.add_line('outline-4', (32, 4), (40, 4))
        self.add_line('outline-5-joint-1', (40, 4), (40, 32))
        self.add_line('outline-5-joint-2', (40, 32), (40, 44))
        self.add_line('outline-6', (40, 44), (24, 44))
        self.add_line('outline-7', (24, 44), (8, 44))
        self.add_line('outline-8-joint-1', (8, 44), (8, 32))
        self.add_line('outline-8-joint-2', (8, 32), (8, 4))
        self.add_line('opening-joint-1', (24, 20), (24, 32))
        self.add_line('opening-joint-2', (24, 32), (24, 44))
        self.add_line('reflective-band-1', (8, 32), (24, 32))
        self.add_line('reflective-band-2', (24, 32), (40, 32))
        self.add_contour('outline', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5-joint-1', 'outline-5-joint-2', 'outline-6', 'outline-7', 'outline-8-joint-1', 'outline-8-joint-2', closed=True)
        self.add_contour('reflective-band', 'reflective-band-1', 'reflective-band-2', closed=False)
        self.add_contour('opening', 'opening-joint-1', 'opening-joint-2', closed=False)
        self.relate('connect', 'opening', 'outline')
        self.relate('connect', 'reflective-band', 'outline')
        self.relate('connect', 'reflective-band', 'opening')
