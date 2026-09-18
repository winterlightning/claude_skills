"""Independent 32px profile of irregular-potato-three-eyes.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '4e67f929-3e9f-4fd3-aaec-bcd922b880c6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/painting_4e67f929-3e9f-4fd3-aaec-bcd922b880c6.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4e67f929-3e9f-4fd3-aaec-bcd922b880c6', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/painting_4e67f929-3e9f-4fd3-aaec-bcd922b880c6.svg'),)
PROFILE_SOURCE_KEYS = ('solo/irregular-potato-three-eyes',)
SOLO_SOURCE_ICON_IDS = ('irregular-potato-three-eyes',)
REFERENCE_EXPORT_SHA256 = 'b2df8746807fb8d4b539a5b91aa89af378558cdc03489a6d18bc80fd95a97c19'

class Drawing(Sub32):
    icon_id = 'irregular-potato-three-eyes-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'food'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (16, 2), ((24, 2), (30, 5), (30, 10)))
        self.add_bezier('p1-r1-2', (30, 10), ((30, 14), (25, 15), (25, 18)))
        self.add_bezier('p1-r1-3', (25, 18), ((25, 20), (26, 22), (26, 23)))
        self.add_bezier('p1-r1-4', (26, 23), ((26, 25), (25, 26), (24, 27)))
        self.add_bezier('p1-r1-5', (24, 27), ((21, 29), (18, 30), (14, 30)))
        self.add_bezier('p1-r1-6', (14, 30), ((7, 30), (2, 25), (2, 19)))
        self.add_bezier('p1-r1-7', (2, 19), ((2, 10), (8, 2), (16, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (11, 11), (11, 11))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (21, 11), (21, 11))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (13, 22), (13, 22))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
