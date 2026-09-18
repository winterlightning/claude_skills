"""Independent 32px profile of lock.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '25032f12-63bc-403a-9b53-69083f3313cb'
SOURCE_PATH = 'pictographic-primitives/interface-essential/lock_25032f12-63bc-403a-9b53-69083f3313cb.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('25032f12-63bc-403a-9b53-69083f3313cb', 'pictographic-primitives/interface-essential/lock_25032f12-63bc-403a-9b53-69083f3313cb.svg'), ('e43b261d-5d07-450c-ab97-9058803311d6', 'pictographic-primitives/interface-essential/lock_e43b261d-5d07-450c-ab97-9058803311d6.svg'), ('ee9cb073-d745-4a2a-a54b-ab36b6f8efb7', 'pictographic-primitives/interface-essential/lock_ee9cb073-d745-4a2a-a54b-ab36b6f8efb7.svg'), ('386cb547-821f-4d23-a0b8-bb7f43205473', 'pictographic-primitives/interface-essential/lock_386cb547-821f-4d23-a0b8-bb7f43205473.svg'))
PROFILE_SOURCE_KEYS = ('solo/lock', 'solo/lock-e43b261d', 'solo/lock-ee9cb073', 'solo/lock-interface-essential')
SOLO_SOURCE_ICON_IDS = ('lock', 'lock-e43b261d', 'lock-ee9cb073', 'lock-interface-essential')
REFERENCE_EXPORT_SHA256 = 'c3f139e1f35a4f1b1fb13df6b653dd944c83035799d224f6acd7916e6c9b27e7'

class DrawingContainerSymbol(Sub32):
    icon_id = 'lock-sub32-symbol'
    related_origin_icon_id = 'lock-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/lock-sub32'
    counterpart_icon_id = 'lock-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 2), (15, 2))
        self.add_arc('p1-r1-2', (15, 2), (8, 9), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_line('p1-r1-3', (8, 9), (8, 13))
        self.add_line('p1-r1-4', (8, 13), (24, 13))
        self.add_line('p1-r1-5', (24, 13), (24, 9))
        self.add_arc('p1-r1-6', (24, 9), (17, 2), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_line('p1-r1-7', (17, 2), (16, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (16, 30), (8, 30))
        self.add_arc('p2-r1-2', (8, 30), (5, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (5, 26), (5, 15))
        self.add_arc('p2-r1-4', (5, 15), (8, 13), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (16, 30), (24, 30))
        self.add_arc('p3-r1-2', (24, 30), (27, 26), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p3-r1-3', (27, 26), (27, 26))
        self.add_line('p3-r1-4', (27, 26), (27, 15))
        self.add_arc('p3-r1-5', (27, 15), (24, 13), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-4')
        self.relate('connect', 'p1-r1-4', 'p2-r1-4')
        self.relate('connect', 'p1-r1-4', 'p3-r1-5')
        self.relate('connect', 'p1-r1-5', 'p3-r1-5')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
