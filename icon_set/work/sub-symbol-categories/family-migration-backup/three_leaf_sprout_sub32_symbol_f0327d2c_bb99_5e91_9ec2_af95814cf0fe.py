# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of three-leaf-sprout.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'f0327d2c-bb99-5e91-9ec2-af95814cf0fe'
SOURCE_PATH = 'pictographic-primitives/nature/plant_f0327d2c-bb99-5e91-9ec2-af95814cf0fe.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f0327d2c-bb99-5e91-9ec2-af95814cf0fe', 'pictographic-primitives/nature/plant_f0327d2c-bb99-5e91-9ec2-af95814cf0fe.svg'), ('4a47df00-a455-41d9-84a4-6416eb861ee6', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/leaf_4a47df00-a455-41d9-84a4-6416eb861ee6.svg'))
PROFILE_SOURCE_KEYS = ('solo/three-leaf-sprout',)
SOLO_SOURCE_ICON_IDS = ('three-leaf-sprout',)
REFERENCE_EXPORT_SHA256 = 'bfc02d96844395296df394aab25c07ed978e4bd958a79482b856d9d39470a98a'

class DrawingContainerSymbol(Sub32):
    icon_id = 'three-leaf-sprout-sub32-symbol'
    variant_of = 'three-leaf-sprout-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/three-leaf-sprout-sub32'
    counterpart_icon_id = 'three-leaf-sprout-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'nature/batch-02'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (16, 2), (16, 13), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (16, 13), (16, 2), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (16, 13), (16, 27))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 27), (16, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_arc('p4-r1-1', (5, 17), (16, 27), radius_x=11, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p4-r1-2', (16, 27), (5, 17), radius_x=11, radius_y=10, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_arc('p5-r1-1', (27, 17), (16, 27), radius_x=11, radius_y=10, large_arc=False, sweep=False)
        self.add_arc('p5-r1-2', (16, 27), (27, 17), radius_x=11, radius_y=10, large_arc=False, sweep=False)
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-2')
        self.relate('connect', 'p2-r1-1', 'p5-r1-1')
        self.relate('connect', 'p2-r1-1', 'p5-r1-2')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-2')
        self.relate('connect', 'p3-r1-1', 'p5-r1-1')
        self.relate('connect', 'p3-r1-1', 'p5-r1-2')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-2')
        self.relate('connect', 'p4-r1-2', 'p5-r1-1')
        self.relate('connect', 'p4-r1-2', 'p5-r1-2')
