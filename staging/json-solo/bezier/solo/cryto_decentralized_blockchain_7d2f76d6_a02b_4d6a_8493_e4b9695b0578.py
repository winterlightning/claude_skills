"""Cryto decentralized blockchain (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7d2f76d6-a02b-4d6a-8493-e4b9695b0578'
SOURCE_PATH = 'icons-json/arrows/cryto decentralized blockchain_7d2f76d6-a02b-4d6a-8493-e4b9695b0578.json'
AUTHOR = 'json_to_solo'

class CrytoDecentralizedBlockchainArrows(Solo48):
    icon_id = 'cryto-decentralized-blockchain-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('cryto', 'decentralized', 'blockchain', 'arrows')

    def build(self):
        self.add_line('e0', (21, 9), (24, 6))
        self.add_line('e1', (9, 21), (6, 24))
        self.add_line('e2', (9, 27), (6, 24))
        self.add_line('e3', (6, 24), (19, 24))
        self.add_line('e4', (21, 39), (24, 42))
        self.add_line('e5', (27, 39), (24, 42))
        self.add_line('e6', (39, 27), (42, 24))
        self.add_line('e7', (39, 21), (42, 24))
        self.add_line('e8', (42, 24), (29, 24))
        self.add_line('e9', (27, 9), (24, 6))
        self.add_line('e10', (24, 6), (24, 19))
        self.add_line('e11', (24, 29), (24, 42))
        self.add_arc('e12-top', (19, 24), (29, 24), radius_x=5)
        self.add_arc('e12-bottom', (29, 24), (19, 24), radius_x=5)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('c5', 'e6')
        self.add_contour('c6', 'e7', 'e8')
        self.add_contour('c7', 'e9', 'e10')
        self.add_contour('c8', 'e11')
        self.add_contour('e12', 'e12-top', 'e12-bottom', closed=True)
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c8')
        self.relate('connect', 'c4', 'c8')
        self.relate('connect', 'c2', 'e12')
        self.relate('connect', 'c6', 'e12')
        self.relate('connect', 'c7', 'e12')
        self.relate('connect', 'c8', 'e12')
