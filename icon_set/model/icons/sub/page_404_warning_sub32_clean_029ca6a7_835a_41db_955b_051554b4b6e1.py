"""Uniform 4px complete-composition repair candidate; strict findings are retained."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = '029ca6a7-835a-41db-955b-051554b4b6e1'
SOURCE_PATH = 'pictographic-primitives/state/warning with 400 error_029ca6a7-835a-41db-955b-051554b4b6e1.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('outlined warning triangle', 'exclamation stem and dot', '404 on the lower row')

class Drawing(Sub32):
    exception = {'reason': 'User-approved complete reference composition; accept remaining visual/grid/spacing findings while preserving 32x32 and uniform 4px strokes.', 'approved_by': 'user', 'approved_on': '2026-09-24', 'svg_sha256': '12c9b5ade2b3791420fb2666e30ba579bc86e442a82903b843ec18099ebea90b'}
    icon_id = 'page-404-warning-sub32-clean'
    variant_of = 'page-404-warning-sub32'
    variant_label = 'Complete 4px cleanup'
    REPAIR_PLAN = {'concept': '404 Page Not Found Warning', 'core_parts': ('outlined warning triangle', 'exclamation stem and dot', '404 on the lower row'), 'flexible_parts': 'Coordinates and proportions only; no original elements removed.', 'repair': 'Shorten the warning triangle and give the lower digits more height while preserving smooth reused glyph curves, exclamation stem and dot.'}
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    TYPEFACE_GLYPH_IDS = ('digit-4', 'digit-0', 'digit-4')

    def build(self):
        self.add_polyline('triangle', (16, 2), (28, 17), (4, 17), closed=True)
        self.add_line('warning-stem', (16, 7), (16, 8))
        self.add_dot('warning-dot', (16, 12))
        self.add_line('text-4-0-0-0-0', (2.0, 23.0), (2.0, 27.393026))
        self.primitives.append(Bezier('text-4-0-0-0-1', Point(*(2.0, 27.393026)), Point(*(2.208493, 27.597986)), (((2.0, 27.506226), (2.093342, 27.597986), (2.208493, 27.597986)),)))
        self.add_contour('glyph-4-0-0-0', *['text-4-0-0-0-0', 'text-4-0-0-0-1'], closed=False)
        self.add_line('text-4-0-0-1-0', (2.208493, 27.597986), (8.0, 27.597986))
        self.add_line('text-4-0-1-0-0', (6.757593, 23.0), (6.757593, 30.0))
        self.primitives.append(Bezier('text-0-1-0-0-0', Point(*(13.0, 24.998607)), Point(*(19.0, 24.998607)), (((13.0, 24.468747), (13.316286, 23.960046), (13.87868, 23.585379)), ((14.441073, 23.210711), (15.204656, 23.0), (16.0, 23.0)), ((16.795344, 23.0), (17.558927, 23.210711), (18.12132, 23.585379)), ((18.683714, 23.960046), (19.0, 24.468747), (19.0, 24.998607)))))
        self.add_line('text-0-1-0-0-1', (19.0, 24.998607), (19.0, 28.001393))
        self.primitives.append(Bezier('text-0-1-0-0-2', Point(*(19.0, 28.001393)), Point(*(13.0, 28.001393)), (((19.0, 28.531253), (18.683714, 29.039954), (18.12132, 29.414621)), ((17.558927, 29.789289), (16.795344, 30.0), (16.0, 30.0)), ((15.204656, 30.0), (14.441073, 29.789289), (13.87868, 29.414621)), ((13.316286, 29.039954), (13.0, 28.531253), (13.0, 28.001393)))))
        self.add_line('text-0-1-0-0-3', (13.0, 28.001393), (13.0, 24.998607))
        self.add_contour('glyph-0-1-0-0', *['text-0-1-0-0-0', 'text-0-1-0-0-1', 'text-0-1-0-0-2', 'text-0-1-0-0-3'], closed=True)
        self.add_line('text-4-2-0-0-0', (24.0, 23.0), (24.0, 27.393026))
        self.primitives.append(Bezier('text-4-2-0-0-1', Point(*(24.0, 27.393026)), Point(*(24.208493, 27.597986)), (((24.0, 27.506226), (24.093342, 27.597986), (24.208493, 27.597986)),)))
        self.add_contour('glyph-4-2-0-0', *['text-4-2-0-0-0', 'text-4-2-0-0-1'], closed=False)
        self.add_line('text-4-2-0-1-0', (24.208493, 27.597986), (30.0, 27.597986))
        self.add_line('text-4-2-1-0-0', (28.757593, 23.0), (28.757593, 30.0))
