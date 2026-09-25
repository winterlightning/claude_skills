"""Uniform 4px complete-composition repair candidate; strict findings are retained."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = 'e23fb9d7-ed54-45f6-9142-77054c14c7bc'
SOURCE_PATH = 'pictographic-primitives/other/rectangle ad text_e23fb9d7-ed54-45f6-9142-77054c14c7bc.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('rounded square frame', 'uppercase A', 'uppercase D')

class Drawing(Sub32):
    exception = {'reason': 'User-approved complete reference composition; accept remaining visual/grid/spacing findings while preserving 32x32 and uniform 4px strokes.', 'approved_by': 'user', 'approved_on': '2026-09-24', 'svg_sha256': '468a24ccd7ab03f77c5c483968256fa687033feae9fffd77104c04fc073c805e'}
    icon_id = 'square-advertisement-sub32-v2-clean'
    variant_of = 'square-advertisement-sub32-v2'
    variant_label = 'Complete 4px cleanup'
    REPAIR_PLAN = {'concept': 'Square Advertisement Icon', 'core_parts': ('rounded square frame', 'uppercase A', 'uppercase D'), 'flexible_parts': 'Coordinates and proportions only; no original elements removed.', 'repair': 'Rebalance the complete reused A and D with smooth glyph curves, retaining the frame and both letter counters.'}
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    TYPEFACE_GLYPH_IDS = ('letter-a-uppercase', 'letter-d-uppercase')

    def build(self):
        self.box('frame', 2, 2, 30, 30, 2)
        self.add_line('text-A-0-0-0-0', (7.0, 24.0), (9.678571, 8.64))
        self.primitives.append(Bezier('text-A-0-0-1-0', Point(*(9.678571, 8.64)), Point(*(10.321429, 8.64)), (((9.892857, 7.786667), (10.107143, 7.786667), (10.321429, 8.64)),)))
        self.add_line('text-A-0-0-1-1', (10.321429, 8.64), (13.0, 24.0))
        self.add_contour('glyph-A-0-0-1', *['text-A-0-0-1-0', 'text-A-0-0-1-1'], closed=False)
        self.add_line('text-A-0-1-0-0', (8.178571, 17.173333), (11.821429, 17.173333))
        self.add_line('text-D-1-0-0-0', (19.0, 8.0), (21.4, 8.0))
        self.primitives.append(Bezier('text-D-1-0-0-1', Point(*(21.4, 8.0)), Point(*(21.4, 24.0)), (((26.2, 8.0), (26.2, 24.0), (21.4, 24.0)),)))
        self.add_contour('glyph-D-1-0-0', *['text-D-1-0-0-0', 'text-D-1-0-0-1'], closed=False)
        self.add_line('text-D-1-0-1-0', (21.4, 24.0), (19.0, 24.0))
        self.add_line('text-D-1-0-1-1', (19.0, 24.0), (19.0, 8.0))
        self.add_contour('glyph-D-1-0-1', *['text-D-1-0-1-0', 'text-D-1-0-1-1'], closed=False)

    def box(self, name, left, top, right, bottom, r):
        points = [(left + r, top), (right - r, top), (right, top + r), (right, bottom - r), (right - r, bottom), (left + r, bottom), (left, bottom - r), (left, top + r)]
        for i, a in enumerate(points):
            b = points[(i + 1) % 8]
            if i % 2:
                self.add_arc(f'{name}-{i}', a, b, radius_x=r)
            else:
                self.add_line(f'{name}-{i}', a, b)
        self.add_contour(name, *[f'{name}-{i}' for i in range(8)], closed=True)
