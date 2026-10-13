"""Independent 32px profile of fish-outline.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'ef113d95-603a-4326-bef0-b182c1dd8c4f'
SOURCE_PATH = 'pictographic-primitives/symbol/fish with two small circle_ef113d95-603a-4326-bef0-b182c1dd8c4f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ef113d95-603a-4326-bef0-b182c1dd8c4f', 'pictographic-primitives/symbol/fish with two small circle_ef113d95-603a-4326-bef0-b182c1dd8c4f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/fish-outline',)
SOLO_SOURCE_ICON_IDS = ('fish-outline',)
REFERENCE_EXPORT_SHA256 = '282cb86edd60880d8b70509e61bfd98da69c019099d9fa4202a80fd2b3bc6d1c'

class Drawing(Sub32):
    icon_id = 'fish-outline-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Fish: oval body, triangle tail touching it at one point, eye dot 4 units clear.
        self.add_arc('body-top', (10, 16), (30, 16), radius_x=10, radius_y=12, large_arc=False, sweep=True)
        self.add_arc('body-bottom', (30, 16), (10, 16), radius_x=10, radius_y=12, large_arc=False, sweep=True)
        self.add_contour('body', 'body-top', 'body-bottom', closed=True)
        self.add_polyline('tail', (10, 16), (2, 6), (2, 26), closed=True)
        self.add_dot('eye', (21, 15))
        self.relate('connect', 'body', 'tail')
