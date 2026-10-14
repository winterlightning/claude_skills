"""Independent 32px profile of seated-electric-scooter.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '5812f1f1-7907-4e3b-bee2-99b5ee6eb24b'
SOURCE_PATH = 'pictographic-primitives/transportation/scooter_5812f1f1-7907-4e3b-bee2-99b5ee6eb24b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5812f1f1-7907-4e3b-bee2-99b5ee6eb24b', 'pictographic-primitives/transportation/scooter_5812f1f1-7907-4e3b-bee2-99b5ee6eb24b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/seated-electric-scooter',)
SOLO_SOURCE_ICON_IDS = ('seated-electric-scooter',)
REFERENCE_EXPORT_SHA256 = '6d9e39f55b062cd667d346f1fd91bafc3e674d4168b6f5979154ec0d22408440'

class DrawingContainerSymbol(Sub32):
    icon_id = 'seated-electric-scooter-sub32-symbol'
    related_origin_icon_id = 'seated-electric-scooter-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/seated-electric-scooter-sub32'
    counterpart_icon_id = 'seated-electric-scooter-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Seated electric scooter: two wheels joined by the deck, seat over the rear wheel, steering post and bar.
        self.add_arc('w0-1', (2, 24), (10, 24), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('w0-2', (10, 24), (2, 24), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('wheel-r', 'w0-1', 'w0-2', closed=True)
        self.add_arc('w1-1', (22, 24), (30, 24), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('w1-2', (30, 24), (22, 24), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('wheel-f', 'w1-1', 'w1-2', closed=True)
        self.add_line('deck', (10, 24), (22, 24))
        self.add_line('seat-post', (6, 20), (6, 12))
        self.add_line('seat', (2, 12), (10, 12))
        self.add_line('steer', (26, 20), (24, 4))
        self.add_line('bar', (20, 4), (24, 4))
        self.relate('connect', 'wheel-r', 'deck')
        self.relate('connect', 'wheel-f', 'deck')
        self.relate('connect', 'wheel-r', 'seat-post')
        self.relate('connect', 'seat-post', 'seat')
        self.relate('connect', 'wheel-f', 'steer')
        self.relate('connect', 'steer', 'bar')
