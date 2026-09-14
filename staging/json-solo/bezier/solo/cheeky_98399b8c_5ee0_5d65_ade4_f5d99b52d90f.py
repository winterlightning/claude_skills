"""Cheeky (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '98399b8c-5ee0-5d65-ade4-f5d99b52d90f'
SOURCE_PATH = 'icons-json/smileys/cheeky_98399b8c-5ee0-5d65-ade4-f5d99b52d90f.json'
AUTHOR = 'json_to_solo'

class CheekySmileys(Solo48):
    icon_id = 'cheeky-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('cheeky', 'smileys')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e1', (13, 21), ((13.127, 20.273), (13.3, 19.745), (13.664, 19.082)), ((14.682, 17.209), (17.073, 17.018), (18.455, 18.582)), ((19.1, 19.318), (18.836, 20.082), (19, 21)))
        self.add_bezier('e2', (28, 21), ((28.091, 20.491), (27.745, 20.318), (27.973, 19.836)), ((28.973, 17.727), (31.845, 16.9), (33.791, 18.209)), ((34.3, 18.545), (34.645, 18.527), (35, 19)))
        self.add_bezier('e3', (15, 29), ((18.109, 38.118), (30.027, 38.3), (33, 29)))
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
