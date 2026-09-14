"""Chemical hexagon (health), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '234919ff-c70d-4bef-84b0-e2745dfa1825'
SOURCE_PATH = 'icons-json/health/chemical hexagon_234919ff-c70d-4bef-84b0-e2745dfa1825.json'
AUTHOR = 'json_to_solo'

class ChemicalHexagon234919ff(Solo48):
    icon_id = 'chemical-hexagon-234919ff'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('chemical', 'hexagon', 'health')

    def build(self):
        self.add_line('e0', (10, 27), (4, 30))
        self.add_line('e1', (4, 30), (4, 37))
        self.add_line('e2', (4, 37), (10, 40))
        self.add_line('e3', (10, 40), (17, 37))
        self.add_line('e4', (17, 37), (17, 30))
        self.add_line('e5', (10, 27), (17, 30))
        self.add_line('e6', (10, 27), (10, 19))
        self.add_line('e7', (17, 30), (24, 26))
        self.add_line('e8', (37, 18), (44, 15))
        self.add_line('e9', (4, 8), (4, 16))
        self.add_line('e10', (4, 16), (10, 18))
        self.add_line('e11', (10, 18), (17, 16))
        self.add_line('e12', (17, 16), (17, 8))
        self.add_line('e13', (37, 18), (30, 15))
        self.add_line('e14', (30, 15), (24, 18))
        self.add_line('e15', (24, 18), (24, 26))
        self.add_line('e16', (24, 26), (30, 29))
        self.add_line('e17', (30, 29), (37, 26))
        self.add_line('e18', (37, 26), (37, 18))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4')
        self.add_contour('c1', 'e5')
        self.add_contour('c2', 'e6')
        self.add_contour('c3', 'e7')
        self.add_contour('c4', 'e8')
        self.add_contour('c5', 'e9', 'e10', 'e11', 'e12')
        self.add_contour('c6', 'e13', 'e14', 'e15', 'e16', 'e17', 'e18', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c4', 'c6')
