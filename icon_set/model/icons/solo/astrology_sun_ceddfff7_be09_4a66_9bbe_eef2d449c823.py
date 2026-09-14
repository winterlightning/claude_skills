"""Astrology sun (_uncategorized_04), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ceddfff7-be09-4a66-9bbe-eef2d449c823'
SOURCE_PATH = 'icons-json/_uncategorized_04/astrology sun_ceddfff7-be09-4a66-9bbe-eef2d449c823.json'
AUTHOR = 'json_to_solo'

class AstrologySun(Solo48):
    icon_id = 'astrology-sun'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_04'
    aliases = ()
    keywords = ('astrology', 'sun', '_uncategorized_04')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e1-top', (19, 24), (29, 24), radius_x=5)
        self.add_arc('e1-bottom', (29, 24), (19, 24), radius_x=5)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
