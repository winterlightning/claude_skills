"""Independent 32px profile of hand-truck-box.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '23e62360-beb2-4bfa-84c6-4545003b32a4'
SOURCE_PATH = 'pictographic-primitives/symbol/logistic_23e62360-beb2-4bfa-84c6-4545003b32a4.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('23e62360-beb2-4bfa-84c6-4545003b32a4', 'pictographic-primitives/symbol/logistic_23e62360-beb2-4bfa-84c6-4545003b32a4.svg'),)
PROFILE_SOURCE_KEYS = ('solo/hand-truck-box',)
SOLO_SOURCE_ICON_IDS = ('hand-truck-box',)
REFERENCE_EXPORT_SHA256 = '3fc4a2044b65106ecba6e921fd7ad6e2626201746b4eee81c872d7171e5d9afb'

class Drawing(Sub32):
    icon_id = 'hand-truck-box-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Hand truck: grip and upright, wheel, base plate carrying an 8-unit box.
        self.add_polyline('upright', (4, 2), (8, 2), (8, 22))
        self.add_arc('wheel-1', (4, 26), (12, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('wheel-2', (12, 26), (4, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('wheel', 'wheel-1', 'wheel-2', closed=True)
        self.add_line('plate', (12, 26), (20, 26))
        self.add_polyline('box', (20, 26), (20, 10), (28, 10), (28, 26), closed=True)
        self.relate('connect', 'upright', 'wheel')
        self.relate('connect', 'wheel', 'plate')
        self.relate('connect', 'plate', 'box')
