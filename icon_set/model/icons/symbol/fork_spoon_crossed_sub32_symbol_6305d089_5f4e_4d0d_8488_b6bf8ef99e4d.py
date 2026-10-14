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
        # Crossed fork and spoon: fork head (crossbar + two tines) top-left, spoon bowl top-right, handles crossing.
        self.add_line('fork-handle', (30, 30), (9, 9))
        self.add_line('fork-bar', (6, 12), (12, 6))
        self.add_line('fork-tine-1', (6, 12), (2, 8))
        self.add_line('fork-tine-2', (12, 6), (8, 2))
        self.add_line('spoon-handle', (2, 30), (23, 9))
        self.add_arc('bowl-1', (22, 6), (30, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('bowl-2', (30, 6), (22, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('bowl', 'bowl-1', 'bowl-2', closed=True)
        for a, b in (('fork-handle', 'fork-bar'), ('fork-bar', 'fork-tine-1'), ('fork-bar', 'fork-tine-2'),
                     ('fork-handle', 'spoon-handle'), ('spoon-handle', 'bowl')):
            self.relate('connect', a, b)
