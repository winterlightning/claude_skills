"""Independent 32px profile of won.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ._tall_base import SourceFaithfulSideSub
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '18f047b9-f81e-571a-a3ea-2c4af962bcb7'
SOURCE_PATH = 'pictographic-primitives/money/won_18f047b9-f81e-571a-a3ea-2c4af962bcb7.svg'
AUTHOR = 'gpt-6'
SOURCE_PARTS = ('W strokes', 'horizontal bar')
SOURCE_REFERENCES = (('18f047b9-f81e-571a-a3ea-2c4af962bcb7', 'pictographic-primitives/money/won_18f047b9-f81e-571a-a3ea-2c4af962bcb7.svg'),)
PROFILE_SOURCE_KEYS = ('solo/won',)
SOLO_SOURCE_ICON_IDS = ('won',)
REFERENCE_EXPORT_SHA256 = 'de0fbfba3c299a969fc32ad65dc01421b6802e8876ad59f63f4e61aaf4b08c9c'

class DrawingVariant2(SourceFaithfulSideSub):
    canvas_width = 60
    canvas_height = 52
    icon_id = 'won-sub32-v2'
    variant_of = 'won-sub32'
    variant_label = 'Complete source on a proportionate canvas'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'money'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (58, 2), (46, 50))
        self.add_line('p1-r1-2', (46, 50), (30, 2))
        self.add_line('p1-r1-3', (30, 2), (14, 46))
        self.add_line('p1-r1-4', (14, 46), (2, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (58, 24), (2, 24))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
