"""Independent 32px profile of wind-state.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'bfffa211-4688-49bd-87eb-16a4c14d3a9b'
SOURCE_PATH = 'pictographic-primitives/state/wind_bfffa211-4688-49bd-87eb-16a4c14d3a9b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bfffa211-4688-49bd-87eb-16a4c14d3a9b', 'pictographic-primitives/state/wind_bfffa211-4688-49bd-87eb-16a4c14d3a9b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/wind-state',)
SOLO_SOURCE_ICON_IDS = ('wind-state',)
REFERENCE_EXPORT_SHA256 = 'b0c06fb6be77ede6d48dd5ed914886bba90470855351411b5d9c65dfa0691d5a'

class Drawing(Sub32):
    icon_id = 'wind-state-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (2, 7), ((5, 6), (6, 5), (9, 5)))
        self.add_bezier('p1-r1-2', (9, 5), ((15, 5), (16, 9), (23, 9)))
        self.add_bezier('p1-r1-3', (23, 9), ((26, 9), (30, 8), (30, 6)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_bezier('p2-r1-1', (2, 16), ((5, 15), (6, 14), (9, 14)))
        self.add_bezier('p2-r1-2', (9, 14), ((15, 14), (16, 18), (23, 18)))
        self.add_bezier('p2-r1-3', (23, 18), ((26, 18), (30, 17), (30, 15)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_bezier('p3-r1-1', (2, 25), ((5, 24), (6, 23), (9, 23)))
        self.add_bezier('p3-r1-2', (9, 23), ((15, 23), (16, 27), (23, 27)))
        self.add_bezier('p3-r1-3', (23, 27), ((26, 27), (30, 27), (30, 24)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
