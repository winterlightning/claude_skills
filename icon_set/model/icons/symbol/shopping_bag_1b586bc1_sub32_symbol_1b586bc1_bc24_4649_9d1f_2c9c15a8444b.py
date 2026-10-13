"""Independent 32px profile of shopping-bag-1b586bc1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '1b586bc1-bc24-4649-9d1f-2c9c15a8444b'
SOURCE_PATH = 'pictographic-primitives/shopping/shopping bag_1b586bc1-bc24-4649-9d1f-2c9c15a8444b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1b586bc1-bc24-4649-9d1f-2c9c15a8444b', 'pictographic-primitives/shopping/shopping bag_1b586bc1-bc24-4649-9d1f-2c9c15a8444b.svg'), ('80985b68-e4c6-544f-91e4-19b090803024', 'pictographic-primitives/accessories/batch-07/bag carry_80985b68-e4c6-544f-91e4-19b090803024.svg'), ('a00cf782-226f-44d9-baca-8f8157db6f9a', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/battery 2_a00cf782-226f-44d9-baca-8f8157db6f9a.svg'))
PROFILE_SOURCE_KEYS = ('solo/shopping-bag-1b586bc1', 'solo/shopping-bag-with-arched-handle')
SOLO_SOURCE_ICON_IDS = ('shopping-bag-1b586bc1', 'shopping-bag-with-arched-handle')
REFERENCE_EXPORT_SHA256 = '41a9f5f19bf82a9f429195d6eecc9bad2dab7033f694408c10e732d5f483fa58'

class DrawingContainerSymbol(Sub32):
    icon_id = 'shopping-bag-1b586bc1-sub32-symbol'
    related_origin_icon_id = 'shopping-bag-1b586bc1-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/shopping-bag-1b586bc1-sub32'
    counterpart_icon_id = 'shopping-bag-1b586bc1-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'shopping'
    categories = ('shopping', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (4, 30), (4, 11))
        self.add_line('p1-r1-2', (4, 11), (12, 11))
        self.add_line('p1-r1-3', (12, 11), (20, 11))
        self.add_line('p1-r1-4', (20, 11), (28, 11))
        self.add_line('p1-r1-5', (28, 11), (28, 30))
        self.add_line('p1-r1-6', (28, 30), (4, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (12, 15), (12, 11))
        self.add_line('p2-r1-2', (12, 11), (12, 6))
        self.add_arc('p2-r1-3', (12, 6), (20, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p2-r1-4', (20, 6), (20, 11))
        self.add_line('p2-r1-5', (20, 11), (20, 15))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p2-r1-4')
        self.relate('connect', 'p1-r1-3', 'p2-r1-5')
        self.relate('connect', 'p1-r1-4', 'p2-r1-4')
        self.relate('connect', 'p1-r1-4', 'p2-r1-5')
