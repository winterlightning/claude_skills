"""Uniform 4px complete-composition repair candidate; strict findings are retained."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = '029ca6a7-835a-41db-955b-051554b4b6e1'
SOURCE_PATH = 'pictographic-primitives/state/warning with 400 error_029ca6a7-835a-41db-955b-051554b4b6e1.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('outlined warning triangle', 'exclamation stem and dot', '404 on the lower row')
class Drawing(Sub32):
    icon_id = 'page-404-warning-sub32-clean'
    variant_of = 'page-404-warning-sub32'
    variant_label = 'Complete 4px cleanup'
    REPAIR_PLAN = {'concept': '404 Page Not Found Warning', 'core_parts': ('outlined warning triangle', 'exclamation stem and dot', '404 on the lower row'), 'flexible_parts': 'Coordinates and proportions only; no original elements removed.', 'repair': 'Give the lower digits more height and retain triangle, exclamation stem and dot; snap reused glyphs to the grid.'}
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    TYPEFACE_GLYPH_IDS = ('digit-4', 'digit-0', 'digit-4')
    def build(self):
        self.add_polyline('triangle',(16,2),(28,17),(4,17),closed=True)
        self.add_line('warning-stem',(16,7),(16,8))
        self.add_dot('warning-dot',(16,12))
        self.add_line('text-4-0-0-0-0',(2, 23),(2, 27))
        self.primitives.append(Bezier('text-4-0-0-0-1',Point(*(2, 27)),Point(*(2, 28)),(((2, 28), (2, 28), (2, 28)),)))
        self.add_contour('glyph-4-0-0-0',*['text-4-0-0-0-0', 'text-4-0-0-0-1'],closed=False)
        self.add_line('text-4-0-0-1-0',(2, 28),(8, 28))
        self.add_line('text-4-0-1-0-0',(7, 23),(7, 30))
        self.primitives.append(Bezier('text-0-1-0-0-0',Point(*(13, 25)),Point(*(19, 25)),(((13, 24), (13, 24), (14, 24)), ((14, 23), (15, 23), (16, 23)), ((17, 23), (18, 23), (18, 24)), ((19, 24), (19, 24), (19, 25)))))
        self.add_line('text-0-1-0-0-1',(19, 25),(19, 28))
        self.primitives.append(Bezier('text-0-1-0-0-2',Point(*(19, 28)),Point(*(13, 28)),(((19, 29), (19, 29), (18, 29)), ((18, 30), (17, 30), (16, 30)), ((15, 30), (14, 30), (14, 29)), ((13, 29), (13, 29), (13, 28)))))
        self.add_line('text-0-1-0-0-3',(13, 28),(13, 25))
        self.add_contour('glyph-0-1-0-0',*['text-0-1-0-0-0', 'text-0-1-0-0-1', 'text-0-1-0-0-2', 'text-0-1-0-0-3'],closed=True)
        self.add_line('text-4-2-0-0-0',(24, 23),(24, 27))
        self.primitives.append(Bezier('text-4-2-0-0-1',Point(*(24, 27)),Point(*(24, 28)),(((24, 28), (24, 28), (24, 28)),)))
        self.add_contour('glyph-4-2-0-0',*['text-4-2-0-0-0', 'text-4-2-0-0-1'],closed=False)
        self.add_line('text-4-2-0-1-0',(24, 28),(30, 28))
        self.add_line('text-4-2-1-0-0',(29, 23),(29, 30))

