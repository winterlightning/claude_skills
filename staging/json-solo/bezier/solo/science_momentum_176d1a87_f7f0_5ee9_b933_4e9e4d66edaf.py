"""Science momentum (science), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '176d1a87-f7f0-5ee9-b933-4e9e4d66edaf'
SOURCE_PATH = 'icons-json/science/science momentum_176d1a87-f7f0-5ee9-b933-4e9e4d66edaf.json'
AUTHOR = 'json_to_solo'

class ScienceMomentumScience(Solo48):
    icon_id = 'science-momentum-science'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('science', 'momentum')

    def build(self):
        self.add_line('e0', (22, 25), (42, 6))
        self.add_line('e1', (42, 6), (35, 7))
        self.add_line('e2', (41, 13), (42, 6))
        self.add_arc('e3-top', (6, 32), (26, 32), radius_x=10)
        self.add_arc('e3-bottom', (26, 32), (6, 32), radius_x=10)
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'e3')
