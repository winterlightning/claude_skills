"""Warp bulge (design), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5b98a2b1-ae7c-5444-a2ba-7bd6baaf76f5'
SOURCE_PATH = 'icons-json/design/warp bulge_5b98a2b1-ae7c-5444-a2ba-7bd6baaf76f5.json'
AUTHOR = 'json_to_solo'

class WarpBulgeDesign(Solo48):
    icon_id = 'warp-bulge-design'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('warp', 'bulge', 'design')

    def build(self):
        self.add_line('e0', (44, 24), (4, 24))
        self.add_arc('e1-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e1-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0')
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
        self.relate('connect', 'c0', 'e1')
        self.relate('connect', 'c0', 'e1')
