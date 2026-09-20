"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'cd5f7537-8a7a-4054-b479-eedbb6a2ed1e'
SOURCE_PATH = 'icon_set/model/icons/symbol/slender_pear_shaped_vase_sub32_cd5f7537_8a7a_4054_b479_eedbb6a2ed1e.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '65584588eb666282d818c692e1515919f90259f7a96111784a8a3d9ab31c6399'
SOURCE_REFERENCES = (('cd5f7537-8a7a-4054-b479-eedbb6a2ed1e', 'pictographic-primitives/decoration/batch-01/bottle_cd5f7537-8a7a-4054-b479-eedbb6a2ed1e.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'slender-pear-shaped-vase-sub32-resize'
    variant_of = 'slender-pear-shaped-vase-sub32'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'objects/decoration'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (6, 2), (14, 2))
        self.add_bezier('p1-r1-2', (14, 2), ((14, 3), (14, 5), (14, 6)))
        self.add_bezier('p1-r1-3', (14, 6), ((14, 7), (14, 8), (14, 9)))
        self.add_bezier('p1-r1-4', (14, 9), ((15, 11), (18, 11), (18, 16)))
        self.add_bezier('p1-r1-5', (18, 16), ((18, 19), (14, 22), (10, 22)))
        self.add_bezier('p1-r1-6', (10, 22), ((6, 22), (2, 19), (2, 16)))
        self.add_bezier('p1-r1-7', (2, 16), ((2, 11), (5, 11), (6, 9)))
        self.add_bezier('p1-r1-8', (6, 9), ((6, 8), (6, 7), (6, 6)))
        self.add_bezier('p1-r1-9', (6, 6), ((6, 5), (6, 3), (6, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', closed=False)
