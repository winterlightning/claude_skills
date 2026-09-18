"""Independent 32px profile of shopping-bag-1b586bc1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '1b586bc1-bc24-4649-9d1f-2c9c15a8444b'
SOURCE_PATH = 'pictographic-primitives/shopping/shopping bag_1b586bc1-bc24-4649-9d1f-2c9c15a8444b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1b586bc1-bc24-4649-9d1f-2c9c15a8444b', 'pictographic-primitives/shopping/shopping bag_1b586bc1-bc24-4649-9d1f-2c9c15a8444b.svg'), ('80985b68-e4c6-544f-91e4-19b090803024', 'pictographic-primitives/accessories/batch-07/bag carry_80985b68-e4c6-544f-91e4-19b090803024.svg'), ('a00cf782-226f-44d9-baca-8f8157db6f9a', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/battery 2_a00cf782-226f-44d9-baca-8f8157db6f9a.svg'))
PROFILE_SOURCE_KEYS = ('solo/shopping-bag-1b586bc1', 'solo/shopping-bag-with-arched-handle')
SOLO_SOURCE_ICON_IDS = ('shopping-bag-1b586bc1', 'shopping-bag-with-arched-handle')
REFERENCE_EXPORT_SHA256 = '41a9f5f19bf82a9f429195d6eecc9bad2dab7033f694408c10e732d5f483fa58'

class Drawing(Sub32):
    icon_id = 'shopping-bag-1b586bc1-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'shopping'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 30), (5, 11))
        self.add_line('p1-r1-2', (5, 11), (11, 11))
        self.add_line('p1-r1-3', (11, 11), (21, 11))
        self.add_line('p1-r1-4', (21, 11), (27, 11))
        self.add_line('p1-r1-5', (27, 11), (27, 30))
        self.add_line('p1-r1-6', (27, 30), (5, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (11, 15), (11, 11))
        self.add_line('p2-r1-2', (11, 11), (11, 7))
        self.add_arc('p2-r1-3', (11, 7), (21, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p2-r1-4', (21, 7), (21, 11))
        self.add_line('p2-r1-5', (21, 11), (21, 15))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-2')
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-2')
        self.relate("connect", 'p1-r1-3', 'p2-r1-4')
        self.relate("connect", 'p1-r1-3', 'p2-r1-5')
        self.relate("connect", 'p1-r1-4', 'p2-r1-4')
        self.relate("connect", 'p1-r1-4', 'p2-r1-5')
