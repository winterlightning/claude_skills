"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'dafb63e7-5f8a-47d0-a53c-945b0a5d235d'
SOURCE_PATH = 'icon_set/model/icons/symbol/angry_person_sub32_dafb63e7_5f8a_47d0_a53c_945b0a5d235d.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'dcbbc609aa0377609425c9be7b360185d73fcf58c54bf208658b03623987312e'
SOURCE_REFERENCES = (('dafb63e7-5f8a-47d0-a53c-945b0a5d235d', 'pictographic-primitives/symbol/angry person_dafb63e7-5f8a-47d0-a53c-945b0a5d235d.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'angry-person-sub32-resize'
    variant_of = 'angry-person-sub32'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'symbols/standalone'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (2, 10), (18, 10), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (18, 10), (2, 10), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_bezier('p2-r1-1', (2, 22), ((4, 19), (7, 18), (10, 18)))
        self.add_bezier('p2-r1-2', (10, 18), ((13, 18), (16, 19), (18, 22)))
        self.add_line('p3-r1-1', (7, 8), (8, 8))
        self.add_line('p4-r1-1', (12, 8), (13, 8))
        self.add_arc('p5-r1-1', (9, 13), (11, 13), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
