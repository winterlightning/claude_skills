"""Franc circle (money), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'acd03875-660c-4af9-9378-1461c22875e1'
SOURCE_PATH = 'icons-json/money/franc circle_acd03875-660c-4af9-9378-1461c22875e1.json'
AUTHOR = 'json_to_solo'

class FrancCircleMoney(Solo48):
    icon_id = 'franc-circle-money'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('franc', 'circle', 'money')

    def build(self):
        self.add_line('e0', (31, 13), (18, 13))
        self.add_line('e1', (18, 13), (18, 24))
        self.add_line('e2', (18, 35), (18, 24))
        self.add_line('e3', (29, 24), (18, 24))
        self.add_arc('e4-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e4-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
