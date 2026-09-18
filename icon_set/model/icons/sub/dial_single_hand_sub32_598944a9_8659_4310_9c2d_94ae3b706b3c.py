"""Independent 32px profile of dial-single-hand.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '598944a9-8659-4310-9c2d-94ae3b706b3c'
SOURCE_PATH = 'pictographic-primitives/symbol/disc_598944a9-8659-4310-9c2d-94ae3b706b3c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('598944a9-8659-4310-9c2d-94ae3b706b3c', 'pictographic-primitives/symbol/disc_598944a9-8659-4310-9c2d-94ae3b706b3c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/dial-single-hand',)
SOLO_SOURCE_ICON_IDS = ('dial-single-hand',)
REFERENCE_EXPORT_SHA256 = '624f6a91b1d34b7cbbc5fcd43063c6c2b7c03a23ddb0f5a9927775a3e32c2650'

class Drawing(Sub32):
    icon_id = 'dial-single-hand-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbols/standalone'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (16, 2), (16, 30), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (16, 30), (16, 2), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (15, 15), (16, 17))
        self.add_line('p2-r1-2', (16, 17), (22, 11))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
