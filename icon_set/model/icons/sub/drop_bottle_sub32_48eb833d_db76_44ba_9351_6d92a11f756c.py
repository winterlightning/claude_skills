"""Independent 32px profile of drop-bottle.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '48eb833d-db76-44ba-9351-6d92a11f756c'
SOURCE_PATH = 'pictographic-primitives/symbol/drop bottle_48eb833d-db76-44ba-9351-6d92a11f756c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('48eb833d-db76-44ba-9351-6d92a11f756c', 'pictographic-primitives/symbol/drop bottle_48eb833d-db76-44ba-9351-6d92a11f756c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/drop-bottle',)
SOLO_SOURCE_ICON_IDS = ('drop-bottle',)
REFERENCE_EXPORT_SHA256 = 'd8dbcc733c8c0f8aa0944a5bcb2205ad7b927eafd7af1202d73a348c48b36f96'

class Drawing(Sub32):
    icon_id = 'drop-bottle-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (13, 2), (20, 2))
        self.add_line('p1-r1-2', (20, 2), (20, 8))
        self.add_bezier('p1-r1-3', (20, 8), ((20, 11), (27, 11), (27, 16)))
        self.add_line('p1-r1-4', (27, 16), (27, 26))
        self.add_arc('p1-r1-5', (27, 26), (24, 30), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (24, 30), (8, 30))
        self.add_arc('p1-r1-7', (8, 30), (5, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (5, 26), (5, 16))
        self.add_bezier('p1-r1-9', (5, 16), ((5, 11), (13, 11), (13, 8)))
        self.add_line('p1-r1-10', (13, 8), (13, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
