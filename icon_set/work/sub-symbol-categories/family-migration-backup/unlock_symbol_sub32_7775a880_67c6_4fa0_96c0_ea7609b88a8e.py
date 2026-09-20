"""Independent 32px profile of unlock-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '7775a880-67c6-4fa0-96c0-ea7609b88a8e'
SOURCE_PATH = 'pictographic-primitives/symbol/unlock_7775a880-67c6-4fa0-96c0-ea7609b88a8e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7775a880-67c6-4fa0-96c0-ea7609b88a8e', 'pictographic-primitives/symbol/unlock_7775a880-67c6-4fa0-96c0-ea7609b88a8e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/unlock-symbol',)
SOLO_SOURCE_ICON_IDS = ('unlock-symbol',)
REFERENCE_EXPORT_SHA256 = '80473f0093dc6a85a381df374e983e659e345d64c9c25a54aeef0128088cb012'

class Drawing(Sub32):
    icon_id = 'unlock-symbol-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (13, 15), (24, 15))
        self.add_arc('p1-r1-2', (24, 15), (27, 17), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (27, 17), (27, 27))
        self.add_arc('p1-r1-4', (27, 27), (24, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (24, 30), (13, 30))
        self.add_arc('p1-r1-6', (13, 30), (10, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (10, 27), (10, 17))
        self.add_arc('p1-r1-8', (10, 17), (13, 15), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (5, 12), (5, 9))
        self.add_arc('p2-r1-2', (5, 9), (19, 9), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (19, 9), (19, 15))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
