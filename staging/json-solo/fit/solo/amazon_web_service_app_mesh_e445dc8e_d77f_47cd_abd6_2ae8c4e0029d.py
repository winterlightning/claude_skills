"""Amazon web service app mesh (_uncategorized_02), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e445dc8e-d77f-47cd-abd6-2ae8c4e0029d'
SOURCE_PATH = 'icons-json/_uncategorized_02/amazon web service app mesh_e445dc8e-d77f-47cd-abd6-2ae8c4e0029d.json'
AUTHOR = 'json_to_solo'

class AmazonWebServiceAppMeshUncategorized02(Solo48):
    icon_id = 'amazon-web-service-app-mesh-uncategorized-02'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_02'
    aliases = ()
    keywords = ('amazon', 'web', 'service', 'app', 'mesh', '_uncategorized_02')

    def build(self):
        self.add_line('e0', (36, 36), (28, 31))
        self.add_line('e1', (12, 36), (20, 31))
        self.add_line('e2', (24, 14), (24, 22))
        self.add_arc('e3-top', (36, 39), (42, 39), radius_x=3)
        self.add_arc('e3-bottom', (42, 39), (36, 39), radius_x=3)
        self.add_arc('e4-top', (6, 39), (12, 39), radius_x=3)
        self.add_arc('e4-bottom', (12, 39), (6, 39), radius_x=3)
        self.add_arc('e5-top', (21, 9), (27, 9), radius_x=3)
        self.add_arc('e5-bottom', (27, 9), (21, 9), radius_x=3)
        self.add_arc('e6-top', (18, 27), (30, 27), radius_x=6)
        self.add_arc('e6-bottom', (30, 27), (18, 27), radius_x=6)
        self.add_arc('e7', (24, 13), (24, 14), radius_x=16, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e7', 'e2')
        self.add_contour('e6', 'e6-top', 'e6-bottom', closed=True)
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'e3')
        self.relate('connect', 'c0', 'e6')
        self.relate('connect', 'c1', 'e4')
        self.relate('connect', 'c1', 'e6')
        self.relate('connect', 'c2', 'e5')
        self.relate('connect', 'c2', 'e6')
