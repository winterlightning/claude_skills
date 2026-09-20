"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'a2029a15-66fa-482d-a28c-001d915dd91d'
SOURCE_PATH = 'icon_set/model/icons/symbol/account_profile_card_sub32_a2029a15_66fa_482d_a28c_001d915dd91d.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '6380cd22fdc92aaa0c1f2bfb2a570a97f7efff59a9adb734595d1a3dbdbd555a'
SOURCE_REFERENCES = (('a2029a15-66fa-482d-a28c-001d915dd91d', 'pictographic-primitives/symbol/account page_a2029a15-66fa-482d-a28c-001d915dd91d.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'account-profile-card-sub32-resize'
    variant_of = 'account-profile-card-sub32'
    variant_label = 'Resize 40 × 32'
    canvas_width = 40
    canvas_height = 32
    category = 'symbols/standalone'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (11, 2), (11, 12), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (11, 12), (11, 2), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p2-r1-1', (2, 30), (11, 20), radius_x=9, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (11, 20), (20, 30), radius_x=9, radius_y=10, large_arc=False, sweep=True)
        self.add_line('p3-r1-1', (29, 3), (38, 3))
        self.add_line('p3-r1-2', (38, 3), (38, 15))
        self.add_line('p3-r1-3', (38, 15), (29, 15))
        self.add_line('p3-r1-4', (29, 15), (29, 3))
        self.add_line('p4-r1-1', (29, 25), (38, 25))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
