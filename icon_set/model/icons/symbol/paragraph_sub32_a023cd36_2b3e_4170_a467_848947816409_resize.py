"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'a023cd36-2b3e-4170-a467-848947816409'
SOURCE_PATH = 'icon_set/model/icons/symbol/paragraph_sub32_a023cd36_2b3e_4170_a467_848947816409.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '2451bdbbd3e03a7275a381c76eef3d1fcfe3455375f0158cea2951504a23470d'
SOURCE_REFERENCES = (('a023cd36-2b3e-4170-a467-848947816409', 'pictographic-primitives/interface-essential/paragraph_a023cd36-2b3e-4170-a467-848947816409.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'paragraph-sub32-resize'
    variant_of = 'paragraph-sub32'
    variant_label = 'Resize 24 × 20'
    canvas_width = 24
    canvas_height = 20
    category = 'interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (22, 2))
        self.add_line('p2-r1-1', (2, 18), (22, 18))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
