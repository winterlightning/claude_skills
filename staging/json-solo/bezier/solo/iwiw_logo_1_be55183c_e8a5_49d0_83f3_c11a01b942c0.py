"""Iwiw logo 1 (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'be55183c-e8a5-49d0-83f3-c11a01b942c0'
SOURCE_PATH = 'icons-json/logos/iwiw logo 1_be55183c-e8a5-49d0-83f3-c11a01b942c0.json'
AUTHOR = 'json_to_solo'

class IwiwLogo1Logos(Solo48):
    icon_id = 'iwiw-logo-1-logos'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('iwiw', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (28, 42), (28, 34))
        self.add_line('e1', (29, 17), (35, 22))
        self.add_line('e2', (29, 17), (21, 22))
        self.add_line('e3', (29, 17), (29, 11))
        self.add_line('e4', (30, 9), (35, 6))
        self.add_line('e5', (36, 6), (41, 9))
        self.add_line('e6', (42, 11), (42, 17))
        self.add_line('e7', (41, 17), (35, 22))
        self.add_line('e8', (28, 34), (35, 31))
        self.add_line('e9', (35, 29), (35, 22))
        self.add_line('e10', (28, 34), (21, 29))
        self.add_line('e11', (21, 22), (13, 17))
        self.add_line('e12', (12, 17), (7, 22))
        self.add_line('e13', (6, 22), (6, 29))
        self.add_line('e14', (7, 31), (13, 34))
        self.add_line('e15', (13, 34), (21, 29))
        self.add_line('e16', (21, 22), (21, 29))
        self.add_bezier('e17', (29, 11), ((29, 10.329), (29.615, 9.483), (30, 9)))
        self.add_bezier('e18', (35, 6), ((35.548, 6), (35.452, 6), (36, 6)))
        self.add_bezier('e19', (41, 9), ((41.589, 9.393), (41.836, 10.403), (42, 11)))
        self.add_bezier('e20', (42, 17), ((42, 17.466), (41.303, 16.795), (41, 17)))
        self.add_bezier('e21', (35, 31), ((35.532, 30.73), (35, 29.54), (35, 29)))
        self.add_bezier('e22', (13, 17), ((12.607, 16.738), (12.385, 16.681), (12, 17)))
        self.add_bezier('e23', (7, 22), ((6.795, 22.164), (6.319, 21.75), (6.155, 21.971)), ((6.074, 22.085), (6.09, 21.894), (6, 22)))
        self.add_bezier('e24', (6, 29), ((6.172, 29.507), (6.452, 30.689), (7, 31)))
        self.add_bezier('e25', (13, 34), ((13.262, 34), (12.738, 34), (13, 34)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e17', 'e4', 'e18', 'e5', 'e19', 'e6', 'e20', 'e7')
        self.add_contour('c4', 'e8', 'e21', 'e9')
        self.add_contour('c5', 'e10')
        self.add_contour('c6', 'e11', 'e22', 'e12', 'e23', 'e13', 'e24', 'e14', 'e25', 'e15')
        self.add_contour('c7', 'e16')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c2', 'c7')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c5', 'c7')
        self.relate('connect', 'c6', 'c7')
