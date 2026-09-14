"""Wild bird sing (animals), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e5', (29, 44), ((27.577, 39.827), (26.947, 36.055), (28.076, 31.655)), ((28.505, 29.964), (29.368, 28.609), (30, 27)))
        self.add_bezier('e6', (27, 21), ((26.663, 20.264), (26.307, 19.882), (25.726, 19.364)), ((23.714, 17.582), (21.507, 16.373), (18.947, 15.818)), ((13.651, 14.673), (8.008, 19.691), (8.008, 25.564)), ((8.008, 25.791), (8, 26.009), (8, 26.236)), ((8, 26.536), (8.017, 26.836), (8.017, 27.136)), ((8.017, 29.873), (9.608, 32.173), (10.063, 34.791)), ((10.653, 38.155), (9.297, 41.027), (8, 44)))
        self.add_contour('c0', 'e5')
        self.add_contour('c1', 'e0', 'e1', 'e2', 'e3')
        self.add_contour('c2', 'e4', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c2')
