"""Smile upside down (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ee72f06c-87a6-550e-be06-374ee3412ed3'
SOURCE_PATH = 'icons-json/smileys/smile upside down_ee72f06c-87a6-550e-be06-374ee3412ed3.json'
AUTHOR = 'json_to_solo'

class SmileUpsideDownSmileys(Solo48):
    icon_id = 'smile-upside-down-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('smile', 'upside', 'down', 'smileys')

    def build(self):
        self.add_line('e0', (30, 27), (30, 30))
        self.add_line('e1', (18, 28), (18, 30))
        self.add_arc('e2-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e2-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e3', (13, 20), ((17.809, 11.327), (30.218, 11.282), (35, 20)))
        self.add_contour('c0', 'e3')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e1')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
