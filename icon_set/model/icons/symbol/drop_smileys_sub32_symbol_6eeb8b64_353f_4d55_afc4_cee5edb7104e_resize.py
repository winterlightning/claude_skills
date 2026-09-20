"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '6eeb8b64-353f-4d55-afc4-cee5edb7104e'
SOURCE_PATH = 'icon_set/model/icons/symbol/drop_smileys_sub32_symbol_6eeb8b64_353f_4d55_afc4_cee5edb7104e.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'f22ec43e24b0d48371c0fd6ae0a6042e0fd50c951ed901392cceb26bb901980d'
SOURCE_REFERENCES = (('6eeb8b64-353f-4d55-afc4-cee5edb7104e', 'pictographic-primitives/smileys/drop_6eeb8b64-353f-4d55-afc4-cee5edb7104e.svg'), ('a1bd3645-c186-44d1-a3a2-2ec8e3d10a1b', 'pictographic-primitives/smileys/drop_a1bd3645-c186-44d1-a3a2-2ec8e3d10a1b.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'drop-smileys-sub32-symbol-resize'
    variant_of = 'drop-smileys-sub32-symbol'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'smileys'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (10, 2), ((7, 6), (2, 11), (2, 14)))
        self.add_bezier('p1-r1-2', (2, 14), ((2, 18), (6, 22), (10, 22)))
        self.add_bezier('p1-r1-3', (10, 22), ((14, 22), (18, 18), (18, 14)))
        self.add_bezier('p1-r1-4', (18, 14), ((18, 11), (13, 6), (10, 2)))
        self.add_arc('p2-r1-1', (10, 17), (13, 14), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
