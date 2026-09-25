"""Independent 32px profile of arrow-up-with-dashed-tail.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '042844f7-9e69-44c7-91bb-6be3830d4b9b'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow dash up_042844f7-9e69-44c7-91bb-6be3830d4b9b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('042844f7-9e69-44c7-91bb-6be3830d4b9b', 'pictographic-primitives/arrows/arrow dash up_042844f7-9e69-44c7-91bb-6be3830d4b9b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrow-up-with-dashed-tail',)
SOLO_SOURCE_ICON_IDS = ('arrow-up-with-dashed-tail',)
REFERENCE_EXPORT_SHA256 = 'cf858dd452d2e3009ea1a3e0be753576621283d7e85ea80505b7f3b36ebf5c00'

class Drawing(Sub32):
    icon_id = 'arrow-up-with-dashed-tail-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (12, 22), (12, 13))
        self.add_line('p1-r1-2', (12, 13), (5, 13))
        self.add_line('p1-r1-3', (5, 13), (16, 2))
        self.add_line('p1-r1-4', (16, 2), (27, 13))
        self.add_line('p1-r1-5', (27, 13), (20, 13))
        self.add_line('p1-r1-6', (20, 13), (20, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (12, 27), (12, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (20, 27), (20, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
