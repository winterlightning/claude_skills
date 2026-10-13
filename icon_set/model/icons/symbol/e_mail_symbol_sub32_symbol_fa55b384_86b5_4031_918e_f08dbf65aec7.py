"""Independent 32px profile of e-mail-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'fa55b384-86b5-4031-918e-f08dbf65aec7'
SOURCE_PATH = 'pictographic-primitives/symbol/e mail_fa55b384-86b5-4031-918e-f08dbf65aec7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('fa55b384-86b5-4031-918e-f08dbf65aec7', 'pictographic-primitives/symbol/e mail_fa55b384-86b5-4031-918e-f08dbf65aec7.svg'),)
PROFILE_SOURCE_KEYS = ('solo/e-mail-symbol',)
SOLO_SOURCE_ICON_IDS = ('e-mail-symbol',)
REFERENCE_EXPORT_SHA256 = 'f69ae2d00a398809a257e89a569439f828a3647e23318e490856f84cc2a87106'

class DrawingContainerSymbol(Sub32):
    icon_id = 'e-mail-symbol-sub32-symbol'
    related_origin_icon_id = 'e-mail-symbol-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/e-mail-symbol-sub32'
    counterpart_icon_id = 'e-mail-symbol-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 4), (27, 4))
        self.add_arc('p1-r1-2', (27, 4), (30, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (30, 7), (30, 25))
        self.add_arc('p1-r1-4', (30, 25), (27, 28), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (27, 28), (5, 28))
        self.add_arc('p1-r1-6', (5, 28), (2, 25), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (2, 25), (2, 7))
        self.add_arc('p1-r1-8', (2, 7), (5, 4), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=True)
        self.add_line('p2-r1-1', (2, 7), (16, 18))
        self.add_line('p2-r1-2', (16, 18), (30, 7))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p2-r1-2')
        self.relate('connect', 'p1-r1-7', 'p2-r1-1')
        self.relate('connect', 'p1-r1-8', 'p2-r1-1')
