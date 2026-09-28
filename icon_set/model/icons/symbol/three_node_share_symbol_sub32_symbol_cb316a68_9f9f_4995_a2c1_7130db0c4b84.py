"""Independent 32px profile of three-node-share-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'cb316a68-9f9f-4995-a2c1-7130db0c4b84'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/share 1_cb316a68-9f9f-4995-a2c1-7130db0c4b84.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('cb316a68-9f9f-4995-a2c1-7130db0c4b84', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/share 1_cb316a68-9f9f-4995-a2c1-7130db0c4b84.svg'),)
PROFILE_SOURCE_KEYS = ('solo/three-node-share-symbol',)
SOLO_SOURCE_ICON_IDS = ('three-node-share-symbol',)
REFERENCE_EXPORT_SHA256 = '7feeb69989cec82fede7f784970d52fd20957891b6531defbaaf37465f3989e0'

class DrawingContainerSymbol(Sub32):
    icon_id = 'three-node-share-symbol-sub32-symbol'
    related_origin_icon_id = 'three-node-share-symbol-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/three-node-share-symbol-sub32'
    counterpart_icon_id = 'three-node-share-symbol-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    categories = ('interface-essential', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (16, 2), (24, 10), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (24, 10), (21, 16), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (21, 16), (16, 18), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (16, 18), (11, 16), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p1-r1-5', (11, 16), (8, 10), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p1-r1-6', (8, 10), (16, 2), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_arc('p2-r1-1', (6, 22), (8, 23), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (8, 23), (10, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p2-r1-3', (10, 26), (6, 30), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p2-r1-4', (6, 30), (2, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p2-r1-5', (2, 26), (6, 22), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (11, 16), (8, 23))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_arc('p4-r1-1', (24, 23), (26, 22), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p4-r1-2', (26, 22), (30, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p4-r1-3', (30, 26), (26, 30), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p4-r1-4', (26, 30), (22, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p4-r1-5', (22, 26), (24, 23), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', closed=False)
        self.add_line('p5-r1-1', (21, 16), (24, 23))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-2', 'p5-r1-1')
        self.relate('connect', 'p1-r1-3', 'p5-r1-1')
        self.relate('connect', 'p1-r1-4', 'p3-r1-1')
        self.relate('connect', 'p1-r1-5', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-5', 'p5-r1-1')
