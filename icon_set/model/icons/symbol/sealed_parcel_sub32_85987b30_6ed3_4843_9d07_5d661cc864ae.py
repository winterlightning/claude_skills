"""Independent 32px profile of sealed-parcel.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '85987b30-6ed3-4843-9d07-5d661cc864ae'
SOURCE_PATH = 'pictographic-primitives/shipping/box_85987b30-6ed3-4843-9d07-5d661cc864ae.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('85987b30-6ed3-4843-9d07-5d661cc864ae', 'pictographic-primitives/shipping/box_85987b30-6ed3-4843-9d07-5d661cc864ae.svg'),)
PROFILE_SOURCE_KEYS = ('solo/sealed-parcel',)
SOLO_SOURCE_ICON_IDS = ('sealed-parcel',)
REFERENCE_EXPORT_SHA256 = 'c0633ab32c9a8d2e01b0cd2fd68c91b809cfab1e256b0b53c52c39f46fd5fd0e'

class Drawing(Sub32):
    icon_id = 'sealed-parcel-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'shipping'
    categories = ('primitives', 'shipping')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 2), (10, 2))
        self.add_line('p1-r1-2', (10, 2), (22, 2))
        self.add_line('p1-r1-3', (22, 2), (27, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_arc('p2-r1-1', (27, 2), (30, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-2', (30, 5), (30, 27))
        self.add_arc('p2-r1-3', (30, 27), (27, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-4', (27, 30), (5, 30))
        self.add_arc('p2-r1-5', (5, 30), (2, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-6', (2, 27), (2, 5))
        self.add_arc('p2-r1-7', (2, 5), (5, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', closed=False)
        self.add_line('p3-r1-1', (10, 2), (10, 15))
        self.add_line('p3-r1-2', (10, 15), (16, 11))
        self.add_line('p3-r1-3', (16, 11), (22, 15))
        self.add_line('p3-r1-4', (22, 15), (22, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (19, 23), (23, 23))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-7')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-4')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-4')
