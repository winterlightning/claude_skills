"""Independent 32px profile of half-circle.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'ecc2f033-f9eb-4a2f-9a8d-470f5361b748'
SOURCE_PATH = 'pictographic-primitives/symbol/half circle_ecc2f033-f9eb-4a2f-9a8d-470f5361b748.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ecc2f033-f9eb-4a2f-9a8d-470f5361b748', 'pictographic-primitives/symbol/half circle_ecc2f033-f9eb-4a2f-9a8d-470f5361b748.svg'),)
PROFILE_SOURCE_KEYS = ('solo/half-circle',)
SOLO_SOURCE_ICON_IDS = ('half-circle',)
REFERENCE_EXPORT_SHA256 = 'de82201bcb2cae5869517ca5ef61484bf7deb337ab8d4e360170e3b14b0bc818'

class Drawing(Sub32):
    icon_id = 'half-circle-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 28), (2, 18))
        self.add_arc('p1-r1-2', (2, 18), (30, 18), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (30, 18), (30, 28))
        self.add_line('p1-r1-4', (30, 28), (22, 28))
        self.add_line('p1-r1-5', (22, 28), (22, 18))
        self.add_arc('p1-r1-6', (22, 18), (10, 18), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('p1-r1-7', (10, 18), (10, 28))
        self.add_line('p1-r1-8', (10, 28), (2, 28))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
