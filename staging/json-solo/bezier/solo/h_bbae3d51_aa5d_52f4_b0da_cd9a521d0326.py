"""H (typeface), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bbae3d51-aa5d-52f4-b0da-cd9a521d0326'
SOURCE_PATH = 'icons-json/typeface/H_bbae3d51-aa5d-52f4-b0da-cd9a521d0326.json'
AUTHOR = 'json_to_solo'

class HBbae3d51(Solo48):
    icon_id = 'h-bbae3d51'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('h', 'typeface')

    def build(self):
        self.add_line('e0', (8, 4), (8, 44))
        self.add_line('e1', (40, 24), (8, 24))
        self.add_line('e2', (40, 44), (40, 4))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c0')
