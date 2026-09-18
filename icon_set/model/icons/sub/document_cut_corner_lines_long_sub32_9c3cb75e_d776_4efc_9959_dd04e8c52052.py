"""Independent 32px profile of document-cut-corner-lines-long.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '9c3cb75e-d776-4efc-9959-dd04e8c52052'
SOURCE_PATH = 'pictographic-primitives/symbol/text file_9c3cb75e-d776-4efc-9959-dd04e8c52052.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9c3cb75e-d776-4efc-9959-dd04e8c52052', 'pictographic-primitives/symbol/text file_9c3cb75e-d776-4efc-9959-dd04e8c52052.svg'),)
PROFILE_SOURCE_KEYS = ('solo/document-cut-corner-lines-long',)
SOLO_SOURCE_ICON_IDS = ('document-cut-corner-lines-long',)
REFERENCE_EXPORT_SHA256 = '03dfa3386ea87fbe394118cf50a1713093725dc553f5625f77d08f242ce53976'

class Drawing(Sub32):
    icon_id = 'document-cut-corner-lines-long-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (9, 2), (19, 2))
        self.add_line('p1-r1-2', (19, 2), (27, 10))
        self.add_line('p1-r1-3', (27, 10), (27, 26))
        self.add_arc('p1-r1-4', (27, 26), (23, 30), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (23, 30), (9, 30))
        self.add_arc('p1-r1-6', (9, 30), (5, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (5, 26), (5, 6))
        self.add_arc('p1-r1-8', (5, 6), (9, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (12, 15), (20, 15))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (12, 22), (20, 22))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
