# Variant of lines-sub32-v2; parent file remains unchanged.
"""Independent 32px profile of lines.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '70edbe92-e5a7-4163-82c3-c5891c1950fd'
SOURCE_PATH = 'pictographic-primitives/symbol/lines_70edbe92-e5a7-4163-82c3-c5891c1950fd.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('70edbe92-e5a7-4163-82c3-c5891c1950fd', 'pictographic-primitives/symbol/lines_70edbe92-e5a7-4163-82c3-c5891c1950fd.svg'),)
PROFILE_SOURCE_KEYS = ('solo/lines',)
SOLO_SOURCE_ICON_IDS = ('lines',)
REFERENCE_EXPORT_SHA256 = '291e1867663e7bfaa7272952faa75a50328447a7bca1b4037b97e74378de7a3e'

class DrawingVariant3(Sub32):
    icon_id = 'lines-sub32-v3'
    variant_of = 'lines-sub32-v2'
    variant_label = 'Redraw proportions and source features'
    keyshape = Keyshape.HRECT_S
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Shallow connector with a straight diagonal and two tangent shoulders; avoid an S-curve kink.
        self.add_line('left',(2,10),(9,10))
        self.add_bezier('left-shoulder',(9,10),((10,10),(11,11),(12,12)))
        self.add_line('diagonal',(12,12),(20,20))
        self.add_bezier('right-shoulder',(20,20),((21,21),(22,22),(23,22)))
        self.add_line('right',(23,22),(30,22))
        self.add_contour('connector','left','left-shoulder','diagonal','right-shoulder','right')
