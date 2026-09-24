"""Uniform 4px complete-composition repair candidate; strict findings are retained."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = '5ac31eb3-78ef-42f3-9c6f-1d635c38c923'
SOURCE_PATH = 'pictographic-primitives/state/warning with 500 error_5ac31eb3-78ef-42f3-9c6f-1d635c38c923.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('outlined warning triangle', 'exclamation stem and dot', '500 on the lower row')
class Drawing(Sub32):
    icon_id = 'server-500-warning-sub32-clean'
    variant_of = 'server-500-warning-sub32'
    variant_label = 'Complete 4px cleanup'
    REPAIR_PLAN = {'concept': 'Internal Server Error Warning', 'core_parts': ('outlined warning triangle', 'exclamation stem and dot', '500 on the lower row'), 'flexible_parts': 'Coordinates and proportions only; no original elements removed.', 'repair': 'Give the lower digits more height and retain triangle, exclamation stem and dot; snap reused glyphs to the grid.'}
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    TYPEFACE_GLYPH_IDS = ('digit-5', 'digit-0', 'digit-0')
    def build(self):
        self.add_polyline('triangle',(16,2),(28,17),(4,17),closed=True)
        self.add_line('warning-stem',(16,7),(16,8))
        self.add_dot('warning-dot',(16,12))
        self.add_line('text-5-0-0-0-0',(7, 23),(2, 23))
        self.primitives.append(Bezier('text-5-0-0-1-0',Point(*(2, 23)),Point(*(2, 23)),(((2, 23), (2, 23), (2, 23)),)))
        self.add_line('text-5-0-0-1-1',(2, 23),(2, 26))
        self.add_contour('glyph-5-0-0-1',*['text-5-0-0-1-0', 'text-5-0-0-1-1'],closed=False)
        self.primitives.append(Bezier('text-5-0-0-2-0',Point(*(2, 26)),Point(*(2, 26)),(((2, 26), (2, 26), (2, 26)),)))
        self.add_line('text-5-0-0-3-0',(2, 26),(5, 26))
        self.primitives.append(Bezier('text-5-0-0-4-0',Point(*(5, 26)),Point(*(7, 29)),(((8, 26), (9, 28), (7, 29)),)))
        self.primitives.append(Bezier('text-5-0-0-5-0',Point(*(7, 29)),Point(*(5, 30)),(((7, 30), (6, 30), (5, 30)),)))
        self.add_line('text-5-0-0-6-0',(5, 30),(2, 30))
        self.primitives.append(Bezier('text-0-1-0-0-0',Point(*(13, 25)),Point(*(19, 25)),(((13, 24), (13, 24), (14, 24)), ((14, 23), (15, 23), (16, 23)), ((17, 23), (18, 23), (18, 24)), ((19, 24), (19, 24), (19, 25)))))
        self.add_line('text-0-1-0-0-1',(19, 25),(19, 28))
        self.primitives.append(Bezier('text-0-1-0-0-2',Point(*(19, 28)),Point(*(13, 28)),(((19, 29), (19, 29), (18, 29)), ((18, 30), (17, 30), (16, 30)), ((15, 30), (14, 30), (14, 29)), ((13, 29), (13, 29), (13, 28)))))
        self.add_line('text-0-1-0-0-3',(13, 28),(13, 25))
        self.add_contour('glyph-0-1-0-0',*['text-0-1-0-0-0', 'text-0-1-0-0-1', 'text-0-1-0-0-2', 'text-0-1-0-0-3'],closed=True)
        self.primitives.append(Bezier('text-0-2-0-0-0',Point(*(24, 25)),Point(*(30, 25)),(((24, 24), (24, 24), (25, 24)), ((25, 23), (26, 23), (27, 23)), ((28, 23), (29, 23), (29, 24)), ((30, 24), (30, 24), (30, 25)))))
        self.add_line('text-0-2-0-0-1',(30, 25),(30, 28))
        self.primitives.append(Bezier('text-0-2-0-0-2',Point(*(30, 28)),Point(*(24, 28)),(((30, 29), (30, 29), (29, 29)), ((29, 30), (28, 30), (27, 30)), ((26, 30), (25, 30), (25, 29)), ((24, 29), (24, 29), (24, 28)))))
        self.add_line('text-0-2-0-0-3',(24, 28),(24, 25))
        self.add_contour('glyph-0-2-0-0',*['text-0-2-0-0-0', 'text-0-2-0-0-1', 'text-0-2-0-0-2', 'text-0-2-0-0-3'],closed=True)

