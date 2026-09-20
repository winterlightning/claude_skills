# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of trash.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '2501b9fd-9e68-4968-a930-e114d61b1fc2'
SOURCE_PATH = 'pictographic-primitives/state/trash_2501b9fd-9e68-4968-a930-e114d61b1fc2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2501b9fd-9e68-4968-a930-e114d61b1fc2', 'pictographic-primitives/state/trash_2501b9fd-9e68-4968-a930-e114d61b1fc2.svg'), ('809378b8-e0d0-4cfb-9e28-6f64d31ac4f8', 'pictographic-primitives/symbol/trash_809378b8-e0d0-4cfb-9e28-6f64d31ac4f8.svg'), ('5e0c6d19-547e-46f0-8ec6-c837972fb3f0', 'pictographic-primitives/state/trash_5e0c6d19-547e-46f0-8ec6-c837972fb3f0.svg'))
PROFILE_SOURCE_KEYS = ('solo/trash', 'solo/trash-809378b8', 'solo/trash-state')
SOLO_SOURCE_ICON_IDS = ('trash', 'trash-809378b8', 'trash-state')
REFERENCE_EXPORT_SHA256 = 'ed23ae1a3b6974bca427a959faf7c6b37679d30c452424990e72e5b4fb6dd1f3'

class DrawingContainerSymbol(Sub32):
    icon_id = 'trash-sub32-symbol'
    variant_of = 'trash-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/trash-sub32'
    counterpart_icon_id = 'trash-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (6, 9), (6, 26))
        self.add_arc('p1-r1-2', (6, 26), (10, 30), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p1-r1-3', (10, 30), (22, 30))
        self.add_arc('p1-r1-4', (22, 30), (26, 26), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p1-r1-5', (26, 26), (26, 9))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (5, 9), (6, 9))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (6, 9), (16, 9))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (16, 9), (26, 9))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (26, 9), (27, 9))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (16, 2), (16, 9))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-5', 'p4-r1-1')
        self.relate('connect', 'p1-r1-5', 'p5-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p6-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-1', 'p6-r1-1')
