# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of e-mail-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'fa55b384-86b5-4031-918e-f08dbf65aec7'
SOURCE_PATH = 'pictographic-primitives/symbol/e mail_fa55b384-86b5-4031-918e-f08dbf65aec7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('fa55b384-86b5-4031-918e-f08dbf65aec7', 'pictographic-primitives/symbol/e mail_fa55b384-86b5-4031-918e-f08dbf65aec7.svg'),)
PROFILE_SOURCE_KEYS = ('solo/e-mail-symbol',)
SOLO_SOURCE_ICON_IDS = ('e-mail-symbol',)
REFERENCE_EXPORT_SHA256 = 'f69ae2d00a398809a257e89a569439f828a3647e23318e490856f84cc2a87106'

class DrawingContainerSymbol(Sub32):
    icon_id = 'e-mail-symbol-sub32-symbol'
    variant_of = 'e-mail-symbol-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/e-mail-symbol-sub32'
    counterpart_icon_id = 'e-mail-symbol-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 5), (27, 5))
        self.add_arc('p1-r1-2', (27, 5), (30, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (30, 8), (30, 10))
        self.add_line('p1-r1-4', (30, 10), (30, 24))
        self.add_arc('p1-r1-5', (30, 24), (27, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (27, 27), (5, 27))
        self.add_arc('p1-r1-7', (5, 27), (2, 24), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (2, 24), (2, 10))
        self.add_line('p1-r1-9', (2, 10), (2, 8))
        self.add_arc('p1-r1-10', (2, 8), (5, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_bezier('p2-r1-1', (2, 10), ((2, 13), (3, 16), (6, 18)))
        self.add_bezier('p2-r1-2', (6, 18), ((9, 20), (12, 22), (16, 22)))
        self.add_bezier('p2-r1-3', (16, 22), ((20, 22), (23, 20), (26, 18)))
        self.add_bezier('p2-r1-4', (26, 18), ((29, 16), (30, 13), (30, 10)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-4')
        self.relate('connect', 'p1-r1-4', 'p2-r1-4')
        self.relate('connect', 'p1-r1-8', 'p2-r1-1')
        self.relate('connect', 'p1-r1-9', 'p2-r1-1')
