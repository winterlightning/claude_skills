"""Deploy (design), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aab49738-a401-514b-847e-1fe43007c663'
SOURCE_PATH = 'icons-json/design/deploy_aab49738-a401-514b-847e-1fe43007c663.json'
AUTHOR = 'json_to_solo'

class DeployDesign(Solo48):
    icon_id = 'deploy-design'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('deploy', 'design')

    def build(self):
        self.add_line('e0', (29, 9), (35, 4))
        self.add_line('e1', (35, 4), (40, 9))
        self.add_line('e2', (35, 4), (35, 41))
        self.add_line('e3', (32, 44), (11, 44))
        self.add_line('e4', (8, 41), (8, 21))
        self.add_line('e5', (27, 23), (16, 23))
        self.add_line('e6', (16, 23), (16, 36))
        self.add_line('e7', (16, 36), (27, 36))
        self.add_line('e8', (27, 36), (27, 23))
        self.add_bezier('e9', (35, 41), ((35, 42.555), (33.179, 43.982), (31.907, 43.982)), ((31.848, 43.991), (31.789, 43.991), (31.731, 44)), ((31.68, 44), (32.051, 44), (32, 44)))
        self.add_bezier('e10', (11, 44), ((10.806, 44), (10.981, 43.991), (10.787, 43.991)), ((10.661, 43.991), (10.535, 43.991), (10.408, 43.991)), ((10.341, 43.991), (10.282, 43.991), (10.215, 44)), ((10.156, 43.991), (10.097, 43.991), (10.029, 43.991)), ((8.977, 43.991), (8, 42.536), (8, 41.482)), ((8, 41.409), (8, 41.073), (8, 41)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e9', 'e3', 'e10', 'e4')
        self.add_contour('c3', 'e5', 'e6', 'e7', 'e8', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
