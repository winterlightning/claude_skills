"""Independent 32px profile of puzzle-piece.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'daa95c47-3220-4ba6-8dc5-aca5e1866078'
SOURCE_PATH = 'pictographic-primitives/symbol/puzzle piece_daa95c47-3220-4ba6-8dc5-aca5e1866078.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('daa95c47-3220-4ba6-8dc5-aca5e1866078', 'pictographic-primitives/symbol/puzzle piece_daa95c47-3220-4ba6-8dc5-aca5e1866078.svg'),)
PROFILE_SOURCE_KEYS = ('solo/puzzle-piece',)
SOLO_SOURCE_ICON_IDS = ('puzzle-piece',)
REFERENCE_EXPORT_SHA256 = '69bb0742c20688dfc2cb2726d56da61a0bfb102e3c45bc787f4a18a4046c689c'

class Drawing(Sub32):
    icon_id = 'puzzle-piece-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 16), (5, 9))
        self.add_line('p1-r1-2', (5, 9), (12, 9))
        self.add_bezier('p1-r1-3', (12, 9), ((12, 8), (11, 7), (11, 6)))
        self.add_bezier('p1-r1-4', (11, 6), ((11, 5), (12, 4), (13, 3)))
        self.add_bezier('p1-r1-5', (13, 3), ((14, 2), (15, 2), (16, 2)))
        self.add_bezier('p1-r1-6', (16, 2), ((16, 2), (16, 2), (16, 2)))
        self.add_bezier('p1-r1-7', (16, 2), ((16, 2), (16, 2), (16, 2)))
        self.add_bezier('p1-r1-8', (16, 2), ((19, 2), (21, 4), (21, 6)))
        self.add_bezier('p1-r1-9', (21, 6), ((21, 6), (21, 7), (21, 7)))
        self.add_bezier('p1-r1-10', (21, 7), ((21, 8), (21, 8), (21, 9)))
        self.add_line('p1-r1-11', (21, 9), (27, 9))
        self.add_line('p1-r1-12', (27, 9), (27, 16))
        self.add_bezier('p1-r1-13', (27, 16), ((27, 16), (26, 16), (26, 16)))
        self.add_bezier('p1-r1-14', (26, 16), ((25, 16), (25, 16), (24, 16)))
        self.add_bezier('p1-r1-15', (24, 16), ((22, 17), (22, 18), (22, 20)))
        self.add_bezier('p1-r1-16', (22, 20), ((22, 22), (23, 23), (25, 24)))
        self.add_bezier('p1-r1-17', (25, 24), ((25, 24), (25, 24), (26, 24)))
        self.add_bezier('p1-r1-18', (26, 24), ((26, 24), (27, 24), (27, 24)))
        self.add_line('p1-r1-19', (27, 24), (27, 30))
        self.add_line('p1-r1-20', (27, 30), (5, 30))
        self.add_line('p1-r1-21', (5, 30), (5, 23))
        self.add_bezier('p1-r1-22', (5, 23), ((5, 23), (6, 23), (7, 23)))
        self.add_bezier('p1-r1-23', (7, 23), ((7, 23), (7, 23), (7, 23)))
        self.add_bezier('p1-r1-24', (7, 23), ((10, 23), (11, 21), (11, 19)))
        self.add_bezier('p1-r1-25', (11, 19), ((11, 17), (9, 15), (7, 15)))
        self.add_bezier('p1-r1-26', (7, 15), ((7, 15), (7, 15), (7, 15)))
        self.add_bezier('p1-r1-27', (7, 15), ((6, 15), (6, 16), (5, 16)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', 'p1-r1-16', 'p1-r1-17', 'p1-r1-18', 'p1-r1-19', 'p1-r1-20', 'p1-r1-21', 'p1-r1-22', 'p1-r1-23', 'p1-r1-24', 'p1-r1-25', 'p1-r1-26', 'p1-r1-27', closed=False)
