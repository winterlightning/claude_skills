"""Uniform 4px complete-composition repair candidate; strict findings are retained."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = '5ac31eb3-78ef-42f3-9c6f-1d635c38c923'
SOURCE_PATH = 'pictographic-primitives/state/warning with 500 error_5ac31eb3-78ef-42f3-9c6f-1d635c38c923.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('outlined warning triangle', 'exclamation stem and dot', '500 on the lower row')

class Drawing(Sub32):
    exception = {'reason': 'User-approved complete reference composition; accept remaining visual/grid/spacing findings while preserving 32x32 and uniform 4px strokes.', 'approved_by': 'user', 'approved_on': '2026-09-24', 'svg_sha256': '8618b5220e0f60b47f76fc5729d6898dbf5d872b71137261cd907f59f0c97091'}
    icon_id = 'server-500-warning-sub32-clean'
    variant_of = 'server-500-warning-sub32'
    variant_label = 'Complete 4px cleanup'
    REPAIR_PLAN = {'concept': 'Internal Server Error Warning', 'core_parts': ('outlined warning triangle', 'exclamation stem and dot', '500 on the lower row'), 'flexible_parts': 'Coordinates and proportions only; no original elements removed.', 'repair': 'Shorten the warning triangle and give the lower digits more height while preserving smooth reused glyph curves, exclamation stem and dot.'}
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    TYPEFACE_GLYPH_IDS = ('digit-5', 'digit-0', 'digit-0')

    def build(self):
        self.add_polyline('triangle', (16, 2), (28, 17), (4, 17), closed=True)
        self.add_line('warning-stem', (16, 7), (16, 8))
        self.add_dot('warning-dot', (16, 12))
        self.add_line('text-5-0-0-0-0', (7.3645, 23.0), (2.252387, 23.0))
        self.primitives.append(Bezier('text-5-0-0-1-0', Point(*(2.252387, 23.0)), Point(*(2.0, 23.204217)), (((2.112999, 23.0), (2.0, 23.091432), (2.0, 23.204217)),)))
        self.add_line('text-5-0-0-1-1', (2.0, 23.204217), (2.0, 25.714773))
        self.add_contour('glyph-5-0-0-1', *['text-5-0-0-1-0', 'text-5-0-0-1-1'], closed=False)
        self.primitives.append(Bezier('text-5-0-0-2-0', Point(*(2.0, 25.714773)), Point(*(2.252387, 25.91899)), (((2.0, 25.827558), (2.112999, 25.91899), (2.252387, 25.91899)),)))
        self.add_line('text-5-0-0-3-0', (2.252387, 25.91899), (5.473155, 25.91899))
        self.primitives.append(Bezier('text-5-0-0-4-0', Point(*(5.473155, 25.91899)), Point(*(7.289043, 29.37541)), (((7.697417, 25.91899), (8.832462, 28.079457), (7.289043, 29.37541)),)))
        self.primitives.append(Bezier('text-5-0-0-5-0', Point(*(7.289043, 29.37541)), Point(*(5.473155, 30.0)), (((6.813704, 29.774518), (6.158172, 30.0), (5.473155, 30.0)),)))
        self.add_line('text-5-0-0-6-0', (5.473155, 30.0), (2.280282, 30.0))
        self.primitives.append(Bezier('text-0-1-0-0-0', Point(*(13.0, 24.998607)), Point(*(19.0, 24.998607)), (((13.0, 24.468747), (13.316286, 23.960046), (13.87868, 23.585379)), ((14.441073, 23.210711), (15.204656, 23.0), (16.0, 23.0)), ((16.795344, 23.0), (17.558927, 23.210711), (18.12132, 23.585379)), ((18.683714, 23.960046), (19.0, 24.468747), (19.0, 24.998607)))))
        self.add_line('text-0-1-0-0-1', (19.0, 24.998607), (19.0, 28.001393))
        self.primitives.append(Bezier('text-0-1-0-0-2', Point(*(19.0, 28.001393)), Point(*(13.0, 28.001393)), (((19.0, 28.531253), (18.683714, 29.039954), (18.12132, 29.414621)), ((17.558927, 29.789289), (16.795344, 30.0), (16.0, 30.0)), ((15.204656, 30.0), (14.441073, 29.789289), (13.87868, 29.414621)), ((13.316286, 29.039954), (13.0, 28.531253), (13.0, 28.001393)))))
        self.add_line('text-0-1-0-0-3', (13.0, 28.001393), (13.0, 24.998607))
        self.add_contour('glyph-0-1-0-0', *['text-0-1-0-0-0', 'text-0-1-0-0-1', 'text-0-1-0-0-2', 'text-0-1-0-0-3'], closed=True)
        self.primitives.append(Bezier('text-0-2-0-0-0', Point(*(24.0, 24.998607)), Point(*(30.0, 24.998607)), (((24.0, 24.468747), (24.316286, 23.960046), (24.87868, 23.585379)), ((25.441073, 23.210711), (26.204656, 23.0), (27.0, 23.0)), ((27.795344, 23.0), (28.558927, 23.210711), (29.12132, 23.585379)), ((29.683714, 23.960046), (30.0, 24.468747), (30.0, 24.998607)))))
        self.add_line('text-0-2-0-0-1', (30.0, 24.998607), (30.0, 28.001393))
        self.primitives.append(Bezier('text-0-2-0-0-2', Point(*(30.0, 28.001393)), Point(*(24.0, 28.001393)), (((30.0, 28.531253), (29.683714, 29.039954), (29.12132, 29.414621)), ((28.558927, 29.789289), (27.795344, 30.0), (27.0, 30.0)), ((26.204656, 30.0), (25.441073, 29.789289), (24.87868, 29.414621)), ((24.316286, 29.039954), (24.0, 28.531253), (24.0, 28.001393)))))
        self.add_line('text-0-2-0-0-3', (24.0, 28.001393), (24.0, 24.998607))
        self.add_contour('glyph-0-2-0-0', *['text-0-2-0-0-0', 'text-0-2-0-0-1', 'text-0-2-0-0-2', 'text-0-2-0-0-3'], closed=True)
