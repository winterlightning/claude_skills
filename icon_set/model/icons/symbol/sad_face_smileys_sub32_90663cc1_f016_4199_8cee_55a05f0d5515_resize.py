"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '90663cc1-f016-4199-8cee-55a05f0d5515'
SOURCE_PATH = 'icon_set/model/icons/symbol/sad_face_smileys_sub32_90663cc1_f016_4199_8cee_55a05f0d5515.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'bf9b336bd0d767d353adfc81f75c83c4d08e67ae46e7ce6739cab8ba86b9f25c'
SOURCE_REFERENCES = (('90663cc1-f016-4199-8cee-55a05f0d5515', 'pictographic-primitives/smileys/sad face_90663cc1-f016-4199-8cee-55a05f0d5515.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'sad-face-smileys-sub32-resize'
    variant_of = 'sad-face-smileys-sub32'
    variant_label = 'Resize 40 × 32'
    canvas_width = 40
    canvas_height = 32
    category = 'smileys'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (6, 2), (6, 8))
        self.add_arc('p2-r1-1', (2, 30), (20, 19), radius_x=19, radius_y=19, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (20, 19), (38, 30), radius_x=19, radius_y=19, large_arc=False, sweep=True)
        self.add_line('p3-r1-1', (34, 2), (34, 8))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
