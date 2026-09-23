"""Gift box with two-loop bow and centered heart on its front."""
from ._tall_base import SourceFaithfulSideSub
from ...keyshapes import Keyshape
from ._compact_reference_helpers import rounded_rect
SOURCE_ICON_ID = '15e4830e-dce1-452c-9f05-87646ea11df9'
SOURCE_PATH = 'pictographic-primitives/romance/love gift box heart_15e4830e-dce1-452c-9f05-87646ea11df9.svg'
AUTHOR = 'gpt-6'
SOURCE_PARTS = ('gift box', 'two bow loops and knot', 'heart')

class DrawingVariant2(SourceFaithfulSideSub):
    canvas_width = 60
    canvas_height = 60
    icon_id = 'heart-gift-box-v2'
    variant_of = 'heart-gift-box'
    variant_label = 'Complete source on a proportionate canvas'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/symbol'
    aliases = ('love-gift',)
    keywords = ('heart', 'gift', 'box', 'present', 'romance')

    def build(self):
        rounded_rect(self, 'box', 2, 22, 58, 58, 5)
        self.add_bezier('bow-left-outer', (30, 14), ((22, 14), (12, 13), (12, 8)), ((12, 4), (14, 2), (18, 2)))
        self.add_bezier('bow-left-inner', (18, 2), ((24, 2), (27, 8), (30, 14)))
        self.add_contour('bow-left', 'bow-left-outer', 'bow-left-inner', closed=True)
        self.add_bezier('bow-right-inner', (30, 14), ((33, 8), (36, 2), (42, 2)))
        self.add_bezier('bow-right-outer', (42, 2), ((46, 2), (48, 4), (48, 8)), ((48, 13), (38, 14), (30, 14)))
        self.add_contour('bow-right', 'bow-right-inner', 'bow-right-outer', closed=True)
        self.add_line('knot', (30, 14), (30, 22))
        self.relate('connect', 'bow-left', 'bow-right')
        self.relate('connect', 'bow-left', 'knot')
        self.relate('connect', 'bow-right', 'knot')
        self.relate('connect', 'box', 'knot')
        self.add_bezier('heart', (30, 50), ((18, 42), (18, 32), (26, 32)), ((28, 32), (30, 36), (30, 36)), ((30, 36), (32, 32), (36, 32)), ((44, 32), (42, 42), (30, 50)))
        self.add_contour('heart-shape', 'heart', closed=True)
