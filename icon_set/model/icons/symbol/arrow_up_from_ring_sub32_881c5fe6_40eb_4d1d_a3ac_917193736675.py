"""Independent 32px profile of arrow-up-from-ring.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '881c5fe6-40eb-4d1d-a3ac-917193736675'
SOURCE_PATH = 'pictographic-primitives/symbol/ups with small circle and lines_881c5fe6-40eb-4d1d-a3ac-917193736675.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('881c5fe6-40eb-4d1d-a3ac-917193736675', 'pictographic-primitives/symbol/ups with small circle and lines_881c5fe6-40eb-4d1d-a3ac-917193736675.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrow-up-from-ring',)
SOLO_SOURCE_ICON_IDS = ('arrow-up-from-ring',)
REFERENCE_EXPORT_SHA256 = 'a983573273b91f08bcc564f5c357b2e0a3840400ca8457732aaa88d09b9d53d9'

class Drawing(Sub32):
    icon_id = 'arrow-up-from-ring-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Arrow rising from a dot on the ground line, every gap 4 units.
        self.add_arc('ring-1', (14, 20), (18, 20), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('ring-2', (18, 20), (14, 20), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('ring', 'ring-1', 'ring-2', closed=True)
        self.add_line('stem', (16, 2), (16, 18))
        self.add_polyline('head', (12, 6), (16, 2), (20, 6))
        self.add_line('ground', (2, 30), (30, 30))
        self.relate('connect', 'ring', 'stem')
        self.relate('connect', 'stem', 'head')
