"""Arrow right (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2dabd652-d8dd-4866-92ea-d5ea5b02c1cf'
SOURCE_PATH = 'icons-json/arrows/arrow right_2dabd652-d8dd-4866-92ea-d5ea5b02c1cf.json'
AUTHOR = 'json_to_solo'

class ArrowRight(Solo48):
    icon_id = 'arrow-right'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (33, 8), (44, 18))
        self.add_line('e1', (27, 18), (44, 18))
        self.add_line('e2', (33, 27), (44, 18))
        self.add_bezier('e3', (4, 40), ((4, 39.427), (4, 38.863), (4, 38.291)), ((4, 30.703), (9.6, 22.914), (17.009, 19.781)), ((19.973, 18.535), (23.764, 18), (27, 18)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e3', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
