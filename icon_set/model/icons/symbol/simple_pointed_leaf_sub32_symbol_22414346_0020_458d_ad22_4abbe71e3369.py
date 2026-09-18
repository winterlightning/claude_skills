"""Independent 32px profile of simple-pointed-leaf.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '22414346-0020-458d-ad22-4abbe71e3369'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/hubbard squash_22414346-0020-458d-ad22-4abbe71e3369.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('22414346-0020-458d-ad22-4abbe71e3369', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/hubbard squash_22414346-0020-458d-ad22-4abbe71e3369.svg'), ('1157517b-90dd-480d-990d-dd252676e00e', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/leaf right_1157517b-90dd-480d-990d-dd252676e00e.svg'))
PROFILE_SOURCE_KEYS = ('solo/simple-pointed-leaf',)
SOLO_SOURCE_ICON_IDS = ('simple-pointed-leaf',)
REFERENCE_EXPORT_SHA256 = 'b22afb178b2f1f738ac4533f54c4f865158d21e320588e440c9cb78b773c5219'

class DrawingContainerSymbol(Sub32):
    icon_id = 'simple-pointed-leaf-sub32-symbol'
    related_origin_icon_id = 'simple-pointed-leaf-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/simple-pointed-leaf-sub32'
    counterpart_icon_id = 'simple-pointed-leaf-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'food'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (2, 30), ((2, 22), (2, 15), (5, 11)))
        self.add_bezier('p1-r1-2', (5, 11), ((9, 7), (14, 4), (20, 4)))
        self.add_bezier('p1-r1-3', (20, 4), ((22, 4), (23, 4), (25, 5)))
        self.add_bezier('p1-r1-4', (25, 5), ((27, 7), (28, 10), (28, 13)))
        self.add_bezier('p1-r1-5', (28, 13), ((28, 16), (27, 19), (25, 22)))
        self.add_bezier('p1-r1-6', (25, 22), ((19, 30), (9, 30), (2, 30)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_bezier('p2-r1-1', (2, 30), ((8, 17), (18, 11), (25, 5)))
        self.add_bezier('p2-r1-2', (25, 5), ((28, 5), (29, 4), (30, 2)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-2')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-2')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
