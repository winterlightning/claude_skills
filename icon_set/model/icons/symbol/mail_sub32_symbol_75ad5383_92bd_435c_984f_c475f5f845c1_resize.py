"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '75ad5383-92bd-435c-984f-c475f5f845c1'
SOURCE_PATH = 'icon_set/model/icons/symbol/mail_sub32_symbol_75ad5383_92bd_435c_984f_c475f5f845c1.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '57018b8fc274b29c6b06c6d7f4d143b8fd8ab7a2e091c98cce1838e3c1e575b6'
SOURCE_REFERENCES = (('75ad5383-92bd-435c-984f-c475f5f845c1', 'pictographic-primitives/symbol/mail_75ad5383-92bd-435c-984f-c475f5f845c1.svg'), ('19aca772-9076-4cc0-8470-0cdffef95def', 'pictographic-primitives/symbol/e mail_19aca772-9076-4cc0-8470-0cdffef95def.svg'), ('a6d5c36b-5f72-4bbf-a205-b2d56aaf29a5', 'pictographic-primitives/symbol/mail_a6d5c36b-5f72-4bbf-a205-b2d56aaf29a5.svg'), ('2a98051e-e248-4ae8-8a84-a56070dcb2ad', 'pictographic-primitives/symbol/page mail_2a98051e-e248-4ae8-8a84-a56070dcb2ad.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'mail-sub32-symbol-resize'
    variant_of = 'mail-sub32-symbol'
    variant_label = 'Resize 24 × 20'
    canvas_width = 24
    canvas_height = 20
    category = 'symbol'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (4, 2), (20, 2))
        self.add_arc('p1-r1-2', (20, 2), (22, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (22, 4), (22, 16))
        self.add_arc('p1-r1-4', (22, 16), (20, 18), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (20, 18), (4, 18))
        self.add_arc('p1-r1-6', (4, 18), (2, 16), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (2, 16), (2, 4))
        self.add_arc('p1-r1-8', (2, 4), (4, 2), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p2-r1-1', (2, 4), (12, 10))
        self.add_line('p2-r1-2', (12, 10), (22, 4))
        self.add_line('p3-r1-1', (2, 16), (12, 10))
        self.add_line('p3-r1-2', (12, 10), (22, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p3-r1-2')
        self.relate('connect', 'p1-r1-4', 'p3-r1-2')
        self.relate('connect', 'p1-r1-6', 'p3-r1-1')
        self.relate('connect', 'p1-r1-7', 'p2-r1-1')
        self.relate('connect', 'p1-r1-7', 'p3-r1-1')
        self.relate('connect', 'p1-r1-8', 'p2-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-2')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-2')
