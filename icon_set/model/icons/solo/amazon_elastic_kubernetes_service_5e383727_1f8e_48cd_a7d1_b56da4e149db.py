"""Amazon elastic kubernetes service (_uncategorized_02), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5e383727-1f8e-48cd-a7d1-b56da4e149db'
SOURCE_PATH = 'icons-json/_uncategorized_02/amazon elastic kubernetes service_5e383727-1f8e-48cd-a7d1-b56da4e149db.json'
AUTHOR = 'json_to_solo'

class AmazonElasticKubernetesService(Solo48):
    icon_id = 'amazon-elastic-kubernetes-service'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_02'
    aliases = ()
    keywords = ('amazon', 'elastic', 'kubernetes', 'service', '_uncategorized_02')

    def build(self):
        self.add_line('e0', (20, 16), (20, 32))
        self.add_line('e1', (29, 31), (23, 23))
        self.add_line('e2', (29, 17), (23, 23))
        self.add_line('e3', (20, 27), (23, 23))
        self.add_line('e4', (24, 44), (8, 34))
        self.add_line('e5', (8, 34), (8, 14))
        self.add_line('e6', (8, 14), (24, 4))
        self.add_line('e7', (25, 4), (40, 14))
        self.add_line('e8', (40, 14), (40, 34))
        self.add_line('e9', (40, 34), (24, 44))
        self.add_arc('e10', (24, 4), (25, 4), radius_x=75, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4', 'e5', 'e6', 'e10', 'e7', 'e8', 'e9', closed=True)
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c3', 'c0')
