"""Lab whisk cup (science), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c2b53cb4-7182-5cc8-9a12-e648e6a45290'
SOURCE_PATH = 'icons-json/science/lab whisk cup_c2b53cb4-7182-5cc8-9a12-e648e6a45290.json'
AUTHOR = 'json_to_solo'

class LabWhiskCupScience(Solo48):
    icon_id = 'lab-whisk-cup-science'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('lab', 'whisk', 'cup', 'science')

    def build(self):
        self.add_line('e0', (40, 26), (11, 26))
        self.add_line('e1', (25, 26), (40, 4))
        self.add_line('e2', (11, 39), (11, 18))
        self.add_line('e3', (11, 18), (8, 13))
        self.add_line('e4', (8, 13), (40, 13))
        self.add_line('e5', (40, 13), (40, 39))
        self.add_line('e6', (34, 44), (17, 44))
        self.add_bezier('e7', (17, 44), ((16.94, 43.991), (16.88, 43.991), (16.82, 43.982)), ((14.92, 43.982), (12.77, 42.682), (11.78, 41.264)), ((11.39, 40.718), (11.21, 39.609), (11, 39)))
        self.add_bezier('e8', (40, 39), ((39.99, 39.145), (39.99, 38.836), (39.98, 38.982)), ((39.98, 41.455), (37.19, 43.991), (34.48, 43.991)), ((34.4, 43.991), (34.32, 44), (34.24, 44)), ((34.16, 44), (34.08, 44), (34, 44)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e7', 'e2', 'e3', 'e4', 'e5', 'e8', 'e6', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c0')
