"""Independent 32px profile of arrow-left-button.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'a74099d0-c11f-40f0-b7ad-8f5a80bb9351'
SOURCE_PATH = 'pictographic-primitives/symbol/arrow left button_a74099d0-c11f-40f0-b7ad-8f5a80bb9351.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a74099d0-c11f-40f0-b7ad-8f5a80bb9351', 'pictographic-primitives/symbol/arrow left button_a74099d0-c11f-40f0-b7ad-8f5a80bb9351.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrow-left-button',)
SOLO_SOURCE_ICON_IDS = ('arrow-left-button',)
REFERENCE_EXPORT_SHA256 = '00cd5cd743cf4a96354b45569d24ef0479efef411e80aaadd848041195c26606'

class Drawing(Sub32):
    icon_id = 'arrow-left-button-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (18, 30), (5, 16))
        self.add_line('p1-r1-2', (5, 16), (18, 2))
        self.add_line('p1-r1-3', (18, 2), (27, 2))
        self.add_line('p1-r1-4', (27, 2), (13, 16))
        self.add_line('p1-r1-5', (13, 16), (27, 30))
        self.add_line('p1-r1-6', (27, 30), (18, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
