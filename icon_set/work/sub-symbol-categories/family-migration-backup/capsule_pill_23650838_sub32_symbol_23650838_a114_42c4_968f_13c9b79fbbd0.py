# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of capsule-pill-23650838.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '23650838-a114-42c4-968f-13c9b79fbbd0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/pill_23650838-a114-42c4-968f-13c9b79fbbd0.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('23650838-a114-42c4-968f-13c9b79fbbd0', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/pill_23650838-a114-42c4-968f-13c9b79fbbd0.svg'), ('57704ac1-8756-4a8f-8e7c-b9a940937812', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/pill_57704ac1-8756-4a8f-8e7c-b9a940937812.svg'), ('6cb102ae-38d0-4d2c-a4ad-c70db66b2436', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/pill_6cb102ae-38d0-4d2c-a4ad-c70db66b2436.svg'), ('fc8e0c39-0672-4642-808f-efcc29625d76', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/pill_fc8e0c39-0672-4642-808f-efcc29625d76.svg'))
PROFILE_SOURCE_KEYS = ('solo/capsule-pill-23650838', 'solo/capsule-pill-57704ac1', 'solo/capsule-pill-6cb102ae', 'solo/capsule-pill-fc8e0c39')
SOLO_SOURCE_ICON_IDS = ('capsule-pill-23650838', 'capsule-pill-57704ac1', 'capsule-pill-6cb102ae', 'capsule-pill-fc8e0c39')
REFERENCE_EXPORT_SHA256 = '35597d143a33f7e0c756a93c2dd31ce4fd85f4014124c365ff2434b910a5b190'

class DrawingContainerSymbol(Sub32):
    icon_id = 'capsule-pill-23650838-sub32-symbol'
    variant_of = 'capsule-pill-23650838-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/capsule-pill-23650838-sub32'
    counterpart_icon_id = 'capsule-pill-23650838-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/health'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (16, 5), ((19, 2), (21, 2), (24, 2)))
        self.add_bezier('p1-r1-2', (24, 2), ((24, 2), (24, 2), (24, 2)))
        self.add_bezier('p1-r1-3', (24, 2), ((28, 2), (30, 5), (30, 10)))
        self.add_bezier('p1-r1-4', (30, 10), ((30, 13), (28, 14), (27, 16)))
        self.add_line('p1-r1-5', (27, 16), (21, 21))
        self.add_line('p1-r1-6', (21, 21), (16, 27))
        self.add_bezier('p1-r1-7', (16, 27), ((13, 30), (11, 30), (8, 30)))
        self.add_bezier('p1-r1-8', (8, 30), ((4, 30), (2, 27), (2, 22)))
        self.add_bezier('p1-r1-9', (2, 22), ((2, 19), (4, 18), (5, 16)))
        self.add_line('p1-r1-10', (5, 16), (11, 11))
        self.add_line('p1-r1-11', (11, 11), (16, 5))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', closed=False)
        self.add_line('p2-r1-1', (11, 11), (21, 21))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
        self.relate('connect', 'p1-r1-10', 'p2-r1-1')
        self.relate('connect', 'p1-r1-11', 'p2-r1-1')
