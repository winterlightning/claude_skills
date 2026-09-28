"""Independent 32px profile of arrow-top-button.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'aa7a027e-2b60-4f40-9164-c2f300152780'
SOURCE_PATH = 'pictographic-primitives/symbol/arrow top button_aa7a027e-2b60-4f40-9164-c2f300152780.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('aa7a027e-2b60-4f40-9164-c2f300152780', 'pictographic-primitives/symbol/arrow top button_aa7a027e-2b60-4f40-9164-c2f300152780.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrow-top-button',)
SOLO_SOURCE_ICON_IDS = ('arrow-top-button',)
REFERENCE_EXPORT_SHA256 = '70493350015a5febacc9d2faae6449d16e80f2a39c11162a9ee6c5595f5d7433'

class Drawing(Sub32):
    icon_id = 'arrow-top-button-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 30), (17, 18))
        self.add_line('p1-r1-2', (17, 18), (27, 29))
        self.add_line('p1-r1-3', (27, 29), (27, 14))
        self.add_line('p1-r1-4', (27, 14), (16, 2))
        self.add_line('p1-r1-5', (16, 2), (5, 14))
        self.add_line('p1-r1-6', (5, 14), (5, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
