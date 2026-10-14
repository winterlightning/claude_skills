"""Independent 32px profile of hang-glider-rider.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '3bc58e49-3bd9-4b80-9381-7be53c19633b'
SOURCE_PATH = 'pictographic-primitives/symbol/paragliding_3bc58e49-3bd9-4b80-9381-7be53c19633b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3bc58e49-3bd9-4b80-9381-7be53c19633b', 'pictographic-primitives/symbol/paragliding_3bc58e49-3bd9-4b80-9381-7be53c19633b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/hang-glider-rider',)
SOLO_SOURCE_ICON_IDS = ('hang-glider-rider',)
REFERENCE_EXPORT_SHA256 = 'b99858b30b85ab2548d6820740644165b32a23c754f92671152e031082a8dc37'

class Drawing(Sub32):
    icon_id = 'hang-glider-rider-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Hang glider: triangular wing, a strap down to the rider lying flat, head dot in front.
        self.add_polyline('wing', (2, 4), (30, 4), (16, 14), closed=True)
        self.add_line('strap', (16, 14), (16, 26))
        self.add_line('body', (6, 26), (24, 26))
        self.add_arc('head-1', (24, 26), (28, 26), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('head-2', (28, 26), (24, 26), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', closed=True)
        self.relate('connect', 'wing', 'strap')
        self.relate('connect', 'strap', 'body')
        self.relate('connect', 'body', 'head')
