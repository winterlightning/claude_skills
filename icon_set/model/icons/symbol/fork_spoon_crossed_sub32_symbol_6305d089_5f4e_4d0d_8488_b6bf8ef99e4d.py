"""Independent 32px profile of fork-spoon-crossed.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '6305d089-5f4e-4d0d-8488-b6bf8ef99e4d'
SOURCE_PATH = 'pictographic-primitives/symbol/spoon and fork_6305d089-5f4e-4d0d-8488-b6bf8ef99e4d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6305d089-5f4e-4d0d-8488-b6bf8ef99e4d', 'pictographic-primitives/symbol/spoon and fork_6305d089-5f4e-4d0d-8488-b6bf8ef99e4d.svg'),)
PROFILE_SOURCE_KEYS = ('solo/fork-spoon-crossed',)
SOLO_SOURCE_ICON_IDS = ('fork-spoon-crossed',)
REFERENCE_EXPORT_SHA256 = '2cbd63fe3602bc94254dadb0413e42262156d6210aef458e617a00c036f6dcb9'

class DrawingContainerSymbol(Sub32):
    icon_id = 'fork-spoon-crossed-sub32-symbol'
    related_origin_icon_id = 'fork-spoon-crossed-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/fork-spoon-crossed-sub32'
    counterpart_icon_id = 'fork-spoon-crossed-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 11), (7, 16))
        self.add_line('p1-r1-2', (7, 16), (11, 16))
        self.add_line('p1-r1-3', (11, 16), (16, 11))
        self.add_line('p1-r1-4', (16, 11), (16, 7))
        self.add_line('p1-r1-5', (16, 7), (11, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (2, 2), (14, 14))
        self.add_line('p2-r1-2', (14, 14), (18, 18))
        self.add_line('p2-r1-3', (18, 18), (30, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (7, 30), (18, 18))
        self.add_line('p3-r1-2', (18, 18), (26, 11))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_arc('p4-r1-1', (22, 7), (30, 7), radius_x=4, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p4-r1-2', (30, 7), (22, 7), radius_x=4, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-2')
        self.relate('connect', 'p2-r1-3', 'p3-r1-1')
        self.relate('connect', 'p2-r1-3', 'p3-r1-2')
