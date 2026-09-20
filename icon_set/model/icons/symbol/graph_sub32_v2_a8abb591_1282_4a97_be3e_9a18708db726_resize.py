"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'a8abb591-1282-4a97-be3e-9a18708db726'
SOURCE_PATH = 'icon_set/model/icons/symbol/graph_sub32_v2_a8abb591_1282_4a97_be3e_9a18708db726.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '0c9a18c40509a352faf29f3004816afa507e1bf3edd3292e4a814ecca0e466ea'
SOURCE_REFERENCES = (('a8abb591-1282-4a97-be3e-9a18708db726', 'pictographic-primitives/arrows/graph_a8abb591-1282-4a97-be3e-9a18708db726.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'graph-sub32-v2-resize'
    variant_of = 'graph-sub32-v2'
    variant_label = 'Resize 24 × 21'
    canvas_width = 24
    canvas_height = 21
    category = 'arrows'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (18, 2), (22, 2))
        self.add_line('p1-r1-2', (22, 2), (13, 14))
        self.add_line('p1-r1-3', (13, 14), (9, 10))
        self.add_line('p1-r1-4', (9, 10), (2, 19))
        self.add_line('p2-r1-1', (22, 2), (22, 6))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
