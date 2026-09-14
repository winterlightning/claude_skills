"""Affinity designer logo (_uncategorized_01), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3afd9516-37f7-4b8b-b3a9-8ba2e70ade56'
SOURCE_PATH = 'icons-json/_uncategorized_01/affinity designer logo_3afd9516-37f7-4b8b-b3a9-8ba2e70ade56.json'
AUTHOR = 'json_to_solo'

class AffinityDesignerLogoUncategorized01(Solo48):
    icon_id = 'affinity-designer-logo-uncategorized-01'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_01'
    aliases = ()
    keywords = ('affinity', 'designer', 'logo', '_uncategorized_01')

    def build(self):
        self.add_line('e0', (14, 29), (16, 32))
        self.add_line('e1', (16, 32), (21, 40))
        self.add_line('e2', (14, 29), (29, 29))
        self.add_line('e3', (14, 29), (21, 18))
        self.add_line('e4', (29, 29), (44, 29))
        self.add_line('e5', (29, 29), (21, 18))
        self.add_line('e6', (44, 29), (44, 38))
        self.add_line('e7', (42, 40), (21, 40))
        self.add_line('e8', (44, 29), (44, 10))
        self.add_line('e9', (42, 8), (28, 8))
        self.add_line('e10', (21, 40), (6, 40))
        self.add_line('e11', (4, 38), (4, 32))
        self.add_line('e12', (4, 30), (19, 9))
        self.add_line('e13', (20, 8), (28, 8))
        self.add_line('e14', (21, 18), (28, 8))
        self.add_bezier('e15', (44, 38), ((43.436, 39.12), (43.155, 39.469), (42, 40)))
        self.add_bezier('e16', (44, 10), ((43.709, 9.377), (43.227, 8), (42.273, 8)), ((42.245, 8), (42.027, 8), (42, 8)))
        self.add_bezier('e17', (6, 40), ((4.664, 39.495), (4.564, 39.229), (4, 38)))
        self.add_bezier('e18', (4, 32), ((4, 31.436), (4, 30.564), (4, 30)))
        self.add_bezier('e19', (19, 9), ((19.718, 8.562), (19.236, 8.244), (20, 8)))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('c5', 'e6', 'e15', 'e7')
        self.add_contour('c6', 'e8', 'e16', 'e9')
        self.add_contour('c7', 'e10', 'e17', 'e11', 'e18', 'e12', 'e19', 'e13')
        self.add_contour('c8', 'e14')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c0', 'c7')
        self.relate('connect', 'c5', 'c7')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c8')
        self.relate('connect', 'c4', 'c8')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c6', 'c8')
        self.relate('connect', 'c7', 'c8')
