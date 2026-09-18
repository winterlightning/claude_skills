"""Independent 32px profile of circles-three-trefoil.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '35f09f7d-689b-4b3c-944a-4e852904bb48'
SOURCE_PATH = 'pictographic-primitives/symbol/three circles_35f09f7d-689b-4b3c-944a-4e852904bb48.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('35f09f7d-689b-4b3c-944a-4e852904bb48', 'pictographic-primitives/symbol/three circles_35f09f7d-689b-4b3c-944a-4e852904bb48.svg'),)
PROFILE_SOURCE_KEYS = ('solo/circles-three-trefoil',)
SOLO_SOURCE_ICON_IDS = ('circles-three-trefoil',)
REFERENCE_EXPORT_SHA256 = '9dfca71b04c9158a59f2cd57ae4fb855ac7a8074d06ab21738e1722f604ad89a'

class Drawing(Sub32):
    icon_id = 'circles-three-trefoil-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (7, 11), (25, 11), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (25, 11), (7, 11), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (2, 21), (21, 21), radius_x=9.5, radius_y=9.5, large_arc=False, sweep=True)
        self.add_bezier('p2-r1-2', (21, 21), ((21, 26), (16, 30), (11, 30)))
        self.add_bezier('p2-r1-3', (11, 30), ((6, 30), (2, 26), (2, 21)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_arc('p3-r1-1', (11, 21), (30, 21), radius_x=9.5, radius_y=9.5, large_arc=False, sweep=True)
        self.add_bezier('p3-r1-2', (30, 21), ((30, 26), (26, 30), (21, 30)))
        self.add_bezier('p3-r1-3', (21, 30), ((16, 30), (11, 26), (11, 21)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
