"""Uniform 4px complete-composition repair candidate; strict findings are retained."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = '52524fee-82eb-4342-93ba-4c710b3efdd0'
SOURCE_PATH = 'pictographic-primitives/other/circle skull xmark_52524fee-82eb-4342-93ba-4c710b3efdd0.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('outer circle', 'skull cranium and closed jaw', 'two eye dots', 'one central jaw divider', 'four diagonal marks behind skull')

class Drawing(Sub32):
    exception = {'reason': 'User-approved complete reference composition; accept remaining visual/grid/spacing findings while preserving 32x32 and uniform 4px strokes.', 'approved_by': 'user', 'approved_on': '2026-09-24', 'svg_sha256': '555c6903e70e9a0f141ef8a8a947d3bc2f2e55f6491f5fbd65a059a1888f11b7'}
    icon_id = 'circle-skull-crossbones-sub32-v2-clean'
    variant_of = 'circle-skull-crossbones-sub32-v2'
    variant_label = 'Complete 4px cleanup'
    REPAIR_PLAN = {'concept': 'Skull and Crossbones Danger Circle', 'core_parts': ('outer circle', 'skull cranium and closed jaw', 'two eye dots', 'one central jaw divider', 'four diagonal marks behind skull'), 'flexible_parts': 'Coordinates and proportions only; no original elements removed.', 'repair': 'Retain the better-separated earlier cranium and four diagonal bones, with a shorter central jaw divider.'}
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    TYPEFACE_GLYPH_IDS = ()

    def build(self):
        self.circle('frame', 16, 16, 14)
        for name, a, b in [('bone-tl', (9, 9), (11, 11)), ('bone-tr', (23, 9), (21, 11)), ('bone-bl', (9, 23), (12, 20)), ('bone-br', (23, 23), (20, 20))]:
            self.add_line(name, a, b)
        self.skull(top=11, bottom=23)

    def circle(self, name, cx, cy, r):
        self.add_arc(name + '-top', (cx - r, cy), (cx + r, cy), radius_x=r)
        self.add_arc(name + '-bottom', (cx + r, cy), (cx - r, cy), radius_x=r)
        self.add_contour(name, name + '-top', name + '-bottom', closed=True)

    def skull(self, top=9, bottom=23, open_jaw=False):
        self.add_bezier('cranium', (12, bottom), ((12, bottom - 1), (12, bottom - 3), (11, bottom - 3)), ((8, bottom - 4), (8, top + 6), (9, top + 3)), ((10, top - 1), (14, top - 2), (16, top - 2)), ((18, top - 2), (22, top - 1), (23, top + 3)), ((24, top + 6), (24, bottom - 4), (21, bottom - 3)), ((20, bottom - 3), (20, bottom - 1), (20, bottom)))
        if not open_jaw:
            self.add_line('jaw-bottom', (20, bottom), (12, bottom))
            self.add_contour('skull', 'cranium', 'jaw-bottom', closed=True)
        self.add_dot('eye-left', (13, 15))
        self.add_dot('eye-right', (19, 15))
        self.add_line('tooth', (16, bottom - 2), (16, bottom))
        if not open_jaw:
            self.relate('connect', 'tooth', 'jaw-bottom')
