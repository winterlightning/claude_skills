"""Independent 32px profile of cursor-left-horizontal.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a19d3d8c-ca4f-4084-a880-3c773e5774a7'
SOURCE_PATH = 'pictographic-primitives/state/cursor left horizontal_a19d3d8c-ca4f-4084-a880-3c773e5774a7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a19d3d8c-ca4f-4084-a880-3c773e5774a7', 'pictographic-primitives/state/cursor left horizontal_a19d3d8c-ca4f-4084-a880-3c773e5774a7.svg'),)
PROFILE_SOURCE_KEYS = ('solo/cursor-left-horizontal',)
SOLO_SOURCE_ICON_IDS = ('cursor-left-horizontal',)
REFERENCE_EXPORT_SHA256 = '4255c657daa0a84c620723a902bf730d4c3625c815b9af27862404e1aac07a82'

class Drawing(Sub32):
    icon_id = 'cursor-left-horizontal-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 15), (30, 5))
        self.add_line('p1-r1-2', (30, 5), (26, 15))
        self.add_arc('p1-r1-3', (26, 15), (26, 17), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p1-r1-4', (26, 17), (30, 27))
        self.add_line('p1-r1-5', (30, 27), (2, 15))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
