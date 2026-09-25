"""Independent 32px profile of handbag.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '935a7339-45e1-4875-b9a1-843bb0be4549'
SOURCE_PATH = 'pictographic-primitives/symbol/purse_935a7339-45e1-4875-b9a1-843bb0be4549.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('935a7339-45e1-4875-b9a1-843bb0be4549', 'pictographic-primitives/symbol/purse_935a7339-45e1-4875-b9a1-843bb0be4549.svg'),)
PROFILE_SOURCE_KEYS = ('solo/handbag',)
SOLO_SOURCE_ICON_IDS = ('handbag',)
REFERENCE_EXPORT_SHA256 = '42fe302da0185afa91cf8cb608ca776c3c5f075a36167134f8fef77fde536cb7'

class Drawing(Sub32):
    icon_id = 'handbag-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 11), (8, 11))
        self.add_line('p1-r1-2', (8, 11), (24, 11))
        self.add_line('p1-r1-3', (24, 11), (27, 11))
        self.add_line('p1-r1-4', (27, 11), (30, 25))
        self.add_arc('p1-r1-5', (30, 25), (25, 30), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (25, 30), (7, 30))
        self.add_arc('p1-r1-7', (7, 30), (2, 25), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (2, 25), (5, 11))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (8, 11), (8, 10))
        self.add_arc('p2-r1-2', (8, 10), (24, 10), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (24, 10), (24, 11))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_arc('p3-r1-1', (5, 11), (27, 11), radius_x=11, radius_y=9, large_arc=False, sweep=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p3-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-3')
        self.relate("connect", 'p1-r1-3', 'p2-r1-3')
        self.relate("connect", 'p1-r1-3', 'p3-r1-1')
        self.relate("connect", 'p1-r1-4', 'p3-r1-1')
        self.relate("connect", 'p1-r1-8', 'p3-r1-1')
