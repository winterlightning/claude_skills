"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '3e543cdc-214f-483d-bf63-44eeef6a18ba'
SOURCE_PATH = 'icon_set/model/icons/symbol/microphone_sub32_v2_symbol_3e543cdc_214f_483d_bf63_44eeef6a18ba.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '54764a4f06c67341c527f3092bbc8f4b6bd49a3e23ec0c99cdd192ecbaaab782'
SOURCE_REFERENCES = (('3e543cdc-214f-483d-bf63-44eeef6a18ba', 'pictographic-primitives/audio/microphone_3e543cdc-214f-483d-bf63-44eeef6a18ba.svg'), ('88610259-450b-43f2-85da-95879335b5f2', 'pictographic-primitives/audio/microphone_88610259-450b-43f2-85da-95879335b5f2.svg'), ('b72da6ab-adc1-4364-be21-8572894c8a90', 'pictographic-primitives/audio/microphone_b72da6ab-adc1-4364-be21-8572894c8a90.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'microphone-sub32-v2-symbol-resize'
    variant_of = 'microphone-sub32-v2-symbol'
    variant_label = 'Resize 21 × 24'
    canvas_width = 21
    canvas_height = 24
    category = 'audio'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (10, 2), (10, 2))
        self.add_bezier('p1-r1-2', (10, 2), ((10, 2), (11, 2), (11, 2)), ((12, 2), (12, 3), (12, 3)), ((12, 3), (13, 3), (13, 4)), ((13, 4), (13, 5), (13, 5)))
        self.add_line('p1-r1-3', (13, 5), (13, 11))
        self.add_bezier('p1-r1-4', (13, 11), ((13, 11), (13, 12), (13, 12)), ((13, 13), (12, 13), (12, 13)), ((12, 13), (12, 14), (11, 14)), ((11, 14), (10, 14), (10, 14)))
        self.add_line('p1-r1-5', (10, 14), (10, 14))
        self.add_bezier('p1-r1-6', (10, 14), ((10, 14), (9, 14), (9, 14)), ((9, 13), (9, 13), (8, 13)), ((8, 13), (8, 12), (8, 12)), ((8, 12), (8, 11), (8, 11)), ((8, 11), (8, 11), (8, 11)))
        self.add_line('p1-r1-7', (8, 11), (8, 5))
        self.add_bezier('p1-r1-8', (8, 5), ((8, 5), (8, 5), (8, 5)), ((8, 5), (8, 4), (8, 4)), ((8, 4), (8, 3), (8, 3)), ((9, 3), (9, 3), (9, 2)), ((9, 2), (10, 2), (10, 2)))
        self.add_line('p2-r1-1', (2, 13), (2, 14))
        self.add_bezier('p2-r1-2', (2, 14), ((2, 15), (2, 16), (3, 16)), ((3, 17), (4, 18), (4, 18)), ((5, 19), (6, 19), (7, 20)), ((8, 20), (9, 20), (10, 20)))
        self.add_bezier('p2-r1-3', (10, 20), ((10, 20), (11, 20), (11, 20)), ((12, 20), (13, 20), (13, 20)), ((14, 20), (15, 19), (16, 19)), ((17, 18), (18, 17), (18, 16)), ((19, 16), (19, 15), (19, 14)), ((19, 14), (19, 14), (19, 14)))
        self.add_line('p2-r1-4', (19, 14), (19, 13))
        self.add_line('p3-r1-1', (10, 20), (10, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-3', 'p3-r1-1')
