"""Curly brackets (programing), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b0b92f6f-2602-450a-ad0e-3d84e809ce25'
SOURCE_PATH = 'icons-json/programing/curly brackets_b0b92f6f-2602-450a-ad0e-3d84e809ce25.json'
AUTHOR = 'json_to_solo'

class CurlyBracketsB0b92f6f(Solo48):
    icon_id = 'curly-brackets-b0b92f6f'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('curly', 'brackets', 'programing')

    def build(self):
        self.add_bezier('sym-e0', (14, 6), ((11.717, 6.499), (10.401, 7.66), (10, 10)))
        self.add_bezier('sym-e1', (10, 10), ((9.951, 10.286), (10, 10.722), (10, 11)))
        self.add_line('sym-e2', (10, 11), (10, 17))
        self.add_bezier('sym-e3', (10, 17), ((10, 17.335), (10.098, 18.665), (10, 19)))
        self.add_bezier('sym-e4', (10, 19), ((9.354, 21.234), (7.857, 22.65), (6, 24)))
        self.add_bezier('sym-e5', (6, 24), ((7.857, 25.35), (9.354, 26.766), (10, 29)))
        self.add_bezier('sym-e6', (10, 29), ((10.098, 29.335), (10, 30.665), (10, 31)))
        self.add_line('sym-e7', (10, 31), (10, 37))
        self.add_bezier('sym-e8', (10, 37), ((10, 37.278), (9.951, 37.714), (10, 38)))
        self.add_bezier('sym-e9', (10, 38), ((10.401, 40.34), (11.717, 41.501), (14, 42)))
        self.add_bezier('sym-e10', (34, 6), ((36.283, 6.499), (37.599, 7.66), (38, 10)))
        self.add_bezier('sym-e11', (38, 10), ((38.049, 10.286), (38, 10.722), (38, 11)))
        self.add_line('sym-e12', (38, 11), (38, 17))
        self.add_bezier('sym-e13', (38, 17), ((38, 17.335), (37.902, 18.665), (38, 19)))
        self.add_bezier('sym-e14', (38, 19), ((38.646, 21.234), (40.143, 22.65), (42, 24)))
        self.add_bezier('sym-e15', (42, 24), ((40.143, 25.35), (38.646, 26.766), (38, 29)))
        self.add_bezier('sym-e16', (38, 29), ((37.902, 29.335), (38, 30.665), (38, 31)))
        self.add_line('sym-e17', (38, 31), (38, 37))
        self.add_bezier('sym-e18', (38, 37), ((38, 37.278), (38.049, 37.714), (38, 38)))
        self.add_bezier('sym-e19', (38, 38), ((37.599, 40.34), (36.283, 41.501), (34, 42)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9')
        self.add_contour('sym-c1', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19')
