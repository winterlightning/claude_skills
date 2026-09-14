"""Blessed (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4669a42f-119e-5431-9305-4e31305f43c1'
SOURCE_PATH = 'icons-json/smileys/blessed_4669a42f-119e-5431-9305-4e31305f43c1.json'
AUTHOR = 'json_to_solo'

class BlessedSmileys(Solo48):
    icon_id = 'blessed-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('blessed', 'smileys')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e1', (12, 22), ((12.264, 21.355), (12.682, 20.845), (13.118, 20.291)), ((14.373, 18.727), (16.827, 18.073), (18.591, 19.145)), ((19.373, 19.618), (19.536, 20.264), (20, 21)))
        self.add_bezier('e2', (28, 22), ((29.755, 17.591), (34.273, 17.555), (36, 22)))
        self.add_bezier('e3', (15, 29), ((16.036, 30.727), (17.164, 32.727), (18.873, 33.836)), ((24.264, 37.345), (30.973, 34.245), (34, 29)))
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
