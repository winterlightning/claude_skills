"""Wave (wayfinding), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9145ab9c-f67d-46a0-8b7c-a4f1ef3fa11c'
SOURCE_PATH = 'pictographic-primitives/wayfinding/wave_9145ab9c-f67d-46a0-8b7c-a4f1ef3fa11c.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class WaveWayfinding(Solo48):
    icon_id = 'wave-wayfinding'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    aliases = ()
    keywords = ('wave', 'wayfinding')

    def build(self):
        self.add_line('e0', (4, 26), (12, 26))
        self.add_line('e1', (12, 26), (19, 8))
        self.add_line('e2', (19, 8), (27, 40))
        self.add_line('e3', (27, 40), (33, 23))
        self.add_line('e4', (33, 23), (44, 23))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4')
