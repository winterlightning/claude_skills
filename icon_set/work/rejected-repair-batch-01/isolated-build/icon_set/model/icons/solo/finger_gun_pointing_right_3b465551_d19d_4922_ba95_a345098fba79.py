'A hand forms a finger gun pointing right, with the index finger extended horizontally and the thumb raised diagonally. Three curled fingers stack beneath the extended finger along the palm.\n\nConstruction: Right-pointing index finger with raised thumb and compact fist. Bounds (4,8)-(44,40).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3b465551-d19d-4922-ba95-a345098fba79'
SOURCE_PATH = 'pictographic-primitives/wayfinding/finger gun two_3b465551-d19d-4922-ba95-a345098fba79.svg'
AUTHOR = 'gpt-6'

class FingerGunPointingRight(Solo48):
    icon_id = 'finger-gun-pointing-right'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('hand', 'finger', 'gun', 'pointing', 'right', 'gesture')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('thumb-1', (4, 24), (16, 8))
        self.add_line('thumb-2', (16, 8), (24, 8))
        self.add_line('thumb-3', (24, 8), (20, 20))
        self.add_line('thumb-4', (20, 20), (40, 20))
        self.add_arc('index-tip', (40, 20), (40, 28), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('palm-lower-1', (40, 28), (24, 28))
        self.add_line('palm-lower-2', (24, 28), (24, 40))
        self.add_line('palm-lower-3', (24, 40), (12, 40))
        self.add_arc('palm-left', (12, 40), (4, 32), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('palm-close', (4, 32), (4, 24))
        self.add_line('fold', (24, 28), (12, 28))
        self.add_contour('outline', 'thumb-1', 'thumb-2', 'thumb-3', 'thumb-4', 'index-tip', 'palm-lower-1', 'palm-lower-2', 'palm-lower-3', 'palm-left', 'palm-close', closed=True)
        self.relate('connect', 'fold', 'outline')
