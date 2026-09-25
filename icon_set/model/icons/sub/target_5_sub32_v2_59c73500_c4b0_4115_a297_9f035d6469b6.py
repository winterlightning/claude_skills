# Variant of target-5-sub32; parent file remains unchanged.
"""Independent 32px profile of target-5.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '59c73500-c4b0-4115-a297-9f035d6469b6'
SOURCE_PATH = 'pictographic-primitives/state/target 5_59c73500-c4b0-4115-a297-9f035d6469b6.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('59c73500-c4b0-4115-a297-9f035d6469b6', 'pictographic-primitives/state/target 5_59c73500-c4b0-4115-a297-9f035d6469b6.svg'),)
PROFILE_SOURCE_KEYS = ('solo/target-5',)
SOLO_SOURCE_ICON_IDS = ('target-5',)
REFERENCE_EXPORT_SHA256 = '75996b71a3ceace08c079387e72892a3fbb7bc21490973638f61dfe577cb34c1'

class DrawingVariant2(Sub32):
    icon_id = 'target-5-sub32-v2'
    variant_label = 'Record the actual joined strokes; preserve reviewed artwork'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 16), (30, 16))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (16, 2), (16, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (5, 16), (27, 16), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (27, 16), (5, 16), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate('connect', 'path-1-1', 'path-3-1')
