"""Chemical hexagon (health), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '621db80c-1add-451c-9953-27071a412659'
SOURCE_PATH = 'pictographic-primitives/health/chemical hexagon_621db80c-1add-451c-9953-27071a412659.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ChemicalHexagonHealth(Solo48):
    icon_id = 'chemical-hexagon-health'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('chemical', 'hexagon', 'health')

    def build(self):
        self.add_line('e0', (34, 6), (34, 11))
        self.add_line('e1', (6, 13), (11, 16))
        self.add_line('e2', (12, 41), (18, 37))
        self.add_line('e3', (40, 41), (35, 37))
        self.add_line('e4', (34, 11), (42, 16))
        self.add_line('e5', (42, 16), (42, 25))
        self.add_line('e6', (42, 25), (35, 29))
        self.add_line('e7', (34, 11), (26, 16))
        self.add_line('e8', (26, 25), (35, 29))
        self.add_line('e9', (26, 25), (26, 16))
        self.add_line('e10', (26, 25), (18, 29))
        self.add_line('e11', (35, 29), (35, 37))
        self.add_line('e12', (35, 37), (26, 42))
        self.add_line('e13', (26, 42), (18, 37))
        self.add_line('e14', (18, 37), (18, 29))
        self.add_line('e15', (18, 29), (11, 25))
        self.add_line('e16', (11, 25), (11, 16))
        self.add_line('e17', (11, 16), (18, 11))
        self.add_line('e18', (18, 11), (26, 16))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4', 'e5', 'e6')
        self.add_contour('c5', 'e7')
        self.add_contour('c6', 'e8')
        self.add_contour('c7', 'e9')
        self.add_contour('c8', 'e10')
        self.add_contour('c9', 'e11')
        self.add_contour('c10', 'e12', 'e13')
        self.add_contour('c11', 'e14')
        self.add_contour('c12', 'e15', 'e16')
        self.add_contour('c13', 'e17', 'e18')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c1', 'c12')
        self.relate('connect', 'c1', 'c13')
        self.relate('connect', 'c12', 'c13')
        self.relate('connect', 'c10', 'c11')
        self.relate('connect', 'c10', 'c2')
        self.relate('connect', 'c11', 'c2')
        self.relate('connect', 'c10', 'c3')
        self.relate('connect', 'c10', 'c9')
        self.relate('connect', 'c3', 'c9')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c4', 'c9')
        self.relate('connect', 'c6', 'c9')
        self.relate('connect', 'c13', 'c5')
        self.relate('connect', 'c13', 'c7')
        self.relate('connect', 'c5', 'c7')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c6', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c11', 'c12')
        self.relate('connect', 'c11', 'c8')
        self.relate('connect', 'c12', 'c8')
