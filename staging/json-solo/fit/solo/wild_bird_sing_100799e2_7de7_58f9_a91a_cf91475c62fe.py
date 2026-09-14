"""Wild bird sing (animals), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '100799e2-7de7-58f9-a91a-cf91475c62fe'
SOURCE_PATH = 'icons-json/animals/wild bird sing_100799e2-7de7-58f9-a91a-cf91475c62fe.json'
AUTHOR = 'json_to_solo'

class WildBirdSing(Solo48):
    icon_id = 'wild-bird-sing'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('wild', 'bird', 'sing', 'animals')

    def build(self):
        self.add_line('e0', (30, 27), (40, 15))
        self.add_line('e1', (40, 15), (28, 18))
        self.add_line('e2', (28, 18), (25, 4))
        self.add_line('e3', (25, 4), (19, 16))
        self.add_line('e4', (30, 27), (27, 21))
        self.add_arc('e5', (29, 44), (30, 27), radius_x=20)
        self.add_arc('e6-1', (27, 21), (15, 16), radius_x=13, sweep=False)
        self.add_arc('e6-2', (15, 16), (8, 26), radius_x=11, sweep=False)
        self.add_line('e6-3', (8, 26), (10, 38))
        self.add_arc('e6-4', (10, 38), (8, 44), radius_x=23)
        self.add_contour('c0', 'e5')
        self.add_contour('c1', 'e0', 'e1', 'e2', 'e3')
        self.add_contour('c2', 'e4', 'e6-1', 'e6-2', 'e6-3', 'e6-4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c2')
