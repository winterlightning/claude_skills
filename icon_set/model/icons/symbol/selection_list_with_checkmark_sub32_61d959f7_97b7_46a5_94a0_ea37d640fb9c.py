"""Independent 32px profile of selection-list-with-checkmark.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '61d959f7-97b7-46a5-94a0-ea37d640fb9c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/mark check_61d959f7-97b7-46a5-94a0-ea37d640fb9c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('61d959f7-97b7-46a5-94a0-ea37d640fb9c', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/mark check_61d959f7-97b7-46a5-94a0-ea37d640fb9c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/selection-list-with-checkmark',)
SOLO_SOURCE_ICON_IDS = ('selection-list-with-checkmark',)
REFERENCE_EXPORT_SHA256 = 'c5f3742556b4dbd99bbd02e82868cd77d1c7f593795fe7b650b8be7a12b18119'

class Drawing(Sub32):
    icon_id = 'selection-list-with-checkmark-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/container-components'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 5), (2, 5))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (10, 5), (10, 5))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 27), (2, 27))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (10, 27), (10, 27))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (19, 27), (19, 27))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (20, 11), (24, 15))
        self.add_line('p6-r1-2', (24, 15), (30, 5))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
        self.add_line('p7-r1-1', (30, 27), (30, 27))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
