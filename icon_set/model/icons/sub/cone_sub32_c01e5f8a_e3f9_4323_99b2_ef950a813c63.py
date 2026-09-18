"""Independent 32px profile of cone.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'c01e5f8a-e3f9-4323-99b2-ef950a813c63'
SOURCE_PATH = 'pictographic-primitives/symbol/cone_c01e5f8a-e3f9-4323-99b2-ef950a813c63.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c01e5f8a-e3f9-4323-99b2-ef950a813c63', 'pictographic-primitives/symbol/cone_c01e5f8a-e3f9-4323-99b2-ef950a813c63.svg'),)
PROFILE_SOURCE_KEYS = ('solo/cone',)
SOLO_SOURCE_ICON_IDS = ('cone',)
REFERENCE_EXPORT_SHA256 = 'fce9ada3965adcfe8ee4ec234f7b4cfc9acf1915f7ef24bf2d868d3d726a5d6d'

class Drawing(Sub32):
    icon_id = 'cone-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 2), (27, 26))
        self.add_bezier('p1-r1-2', (27, 26), ((24, 29), (20, 30), (16, 30)))
        self.add_bezier('p1-r1-3', (16, 30), ((12, 30), (8, 29), (5, 26)))
        self.add_line('p1-r1-4', (5, 26), (16, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
