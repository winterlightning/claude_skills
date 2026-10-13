"""Independent 32px profile of snowmobile-angled.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'b75710e7-8d86-43e7-8398-5efed8f7194b'
SOURCE_PATH = 'pictographic-primitives/symbol/snow scooter_b75710e7-8d86-43e7-8398-5efed8f7194b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b75710e7-8d86-43e7-8398-5efed8f7194b', 'pictographic-primitives/symbol/snow scooter_b75710e7-8d86-43e7-8398-5efed8f7194b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/snowmobile-angled',)
SOLO_SOURCE_ICON_IDS = ('snowmobile-angled',)
REFERENCE_EXPORT_SHA256 = '85dca3d6a7e4ca3cc548e35034ccfb39175b24574985faf0cd31c91085beedcc'

class Drawing(Sub32):
    icon_id = 'snowmobile-angled-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Snowmobile: body with a raised windshield, a strut down to the ski with an upturned tip.
        self.add_polyline('body', (2, 20), (2, 12), (10, 10), (14, 4), (18, 4), (22, 14), (22, 20), closed=True)
        self.add_line('strut', (18, 20), (18, 28))
        self.add_line('ski', (2, 28), (24, 28))
        self.add_arc('tip', (24, 28), (30, 22), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_contour('ski-all', 'ski', 'tip')
        self.relate('connect', 'body', 'strut')
        self.relate('connect', 'strut', 'ski-all')
