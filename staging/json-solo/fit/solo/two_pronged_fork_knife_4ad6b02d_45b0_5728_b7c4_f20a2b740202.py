"""Two pronged fork knife (food), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ad6b02d-45b0-5728-b7c4-f20a2b740202'
SOURCE_PATH = 'icons-json/food/two pronged fork knife_4ad6b02d-45b0-5728-b7c4-f20a2b740202.json'
AUTHOR = 'json_to_solo'

class TwoProngedForkKnifeFood(Solo48):
    icon_id = 'two-pronged-fork-knife-food'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('two', 'pronged', 'fork', 'knife', 'food')

    def build(self):
        self.add_line('e0', (8, 25), (17, 25))
        self.add_line('e1', (17, 25), (15, 15))
        self.add_line('e2', (8, 4), (8, 44))
        self.add_line('e3', (29, 5), (29, 15))
        self.add_line('e4', (35, 44), (35, 20))
        self.add_line('e5', (40, 16), (40, 5))
        self.add_arc('e6', (15, 15), (8, 4), radius_x=20, sweep=False)
        self.add_arc('e7', (29, 15), (35, 20), radius_x=5, sweep=False)
        self.add_arc('e8', (35, 20), (40, 16), radius_x=5, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e6')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3', 'e7')
        self.add_contour('c3', 'e4', 'e8', 'e5')
        self.relate('connect', 'c0', 'c1')
