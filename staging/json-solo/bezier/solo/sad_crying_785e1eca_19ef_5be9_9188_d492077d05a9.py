"""Sad crying (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '785e1eca-19ef-5be9-9188-d492077d05a9'
SOURCE_PATH = 'icons-json/smileys/sad crying_785e1eca-19ef-5be9-9188-d492077d05a9.json'
AUTHOR = 'json_to_solo'

class SadCryingSmileys(Solo48):
    icon_id = 'sad-crying-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('sad', 'crying', 'smileys')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e1', (29, 16), ((30.764, 18.3), (33.045, 18.864), (36, 19)))
        self.add_bezier('e2', (12, 19), ((14.882, 19.091), (17.182, 18.3), (19, 16)))
        self.add_bezier('e3', (13, 23), ((15.064, 23.4), (17.191, 23.082), (19, 22)))
        self.add_bezier('e4', (29, 22), ((30.855, 23.218), (32.845, 23.436), (35, 23)))
        self.add_bezier('e5', (32, 37), ((31.6, 37.1), (31.445, 36.982), (31.018, 36.973)), ((29.064, 36.927), (27.273, 35.573), (25.236, 35.482)), ((23.573, 35.4), (22.091, 35.591), (20.527, 36.164)), ((19.755, 36.445), (19.036, 36.809), (18.236, 36.982)), ((14.582, 37.745), (15.209, 34.555), (16.555, 32.482)), ((17.018, 31.773), (17.645, 31.055), (18.273, 30.491)), ((21.655, 27.455), (25.909, 27.864), (29.527, 30.182)), ((31.273, 31.3), (33.409, 33.927), (32.636, 36.155)), ((32.545, 36.409), (32.127, 36.809), (32, 37)))
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5', closed=True)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
