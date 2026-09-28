"""Complete source composition; see the accompanying visual and validation evidence."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = '029ca6a7-835a-41db-955b-051554b4b6e1'
SOURCE_PATH = 'pictographic-primitives/state/warning with 400 error_029ca6a7-835a-41db-955b-051554b4b6e1.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('outlined warning triangle', 'exclamation stem and dot', '404 on the lower row')

class Drawing(Sub32):
    icon_id = 'page-404-warning-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    keywords = ('404', 'page', 'not', 'found', 'warning')
    TYPEFACE_GLYPH_IDS = ('digit-4', 'digit-0', 'digit-4')

    def build(self):
        self.add_polyline('triangle',(16,2),(27,18),(5,18),closed=True)
        self.add_line('warning-stem',(16,8),(16,9))
        self.add_dot('warning-dot',(16,14))
        self.add_line('text-4-0-0-0-0',(2, 24),(2, 27.765451))
        self.primitives.append(Bezier('text-4-0-0-0-1',Point(*(2, 27.765451)),Point(*(2.208493, 27.941131)),(((2, 27.862479), (2.093342, 27.941131), (2.208493, 27.941131)),)))
        self.add_contour('glyph-4-0-0-0',*['text-4-0-0-0-0', 'text-4-0-0-0-1'],closed=False)
        self.add_line('text-4-0-0-1-0',(2.208493, 27.941131),(8, 27.941131))
        self.add_line('text-4-0-1-0-0',(6.757593, 24),(6.757593, 30))
        self.primitives.append(Bezier('text-0-1-0-0-0',Point(*(13, 25.713092)),Point(*(19, 25.713092)),(((13, 25.258926), (13.316286, 24.822897), (13.87868, 24.501753)), ((14.441073, 24.180609), (15.204656, 24), (16, 24)), ((16.795344, 24), (17.558927, 24.180609), (18.12132, 24.501753)), ((18.683714, 24.822897), (19, 25.258926), (19, 25.713092)))))
        self.add_line('text-0-1-0-0-1',(19, 25.713092),(19, 28.286908))
        self.primitives.append(Bezier('text-0-1-0-0-2',Point(*(19, 28.286908)),Point(*(13, 28.286908)),(((19, 28.741074), (18.683714, 29.177103), (18.12132, 29.498247)), ((17.558927, 29.819391), (16.795344, 30), (16, 30)), ((15.204656, 30), (14.441073, 29.819391), (13.87868, 29.498247)), ((13.316286, 29.177103), (13, 28.741074), (13, 28.286908)))))
        self.add_line('text-0-1-0-0-3',(13, 28.286908),(13, 25.713092))
        self.add_contour('glyph-0-1-0-0',*['text-0-1-0-0-0', 'text-0-1-0-0-1', 'text-0-1-0-0-2', 'text-0-1-0-0-3'],closed=True)
        self.add_line('text-4-2-0-0-0',(24, 24),(24, 27.765451))
        self.primitives.append(Bezier('text-4-2-0-0-1',Point(*(24, 27.765451)),Point(*(24.208493, 27.941131)),(((24, 27.862479), (24.093342, 27.941131), (24.208493, 27.941131)),)))
        self.add_contour('glyph-4-2-0-0',*['text-4-2-0-0-0', 'text-4-2-0-0-1'],closed=False)
        self.add_line('text-4-2-0-1-0',(24.208493, 27.941131),(30, 27.941131))
        self.add_line('text-4-2-1-0-0',(28.757593, 24),(28.757593, 30))

