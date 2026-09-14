"""Z (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '27cfa6e0-e0e2-4acb-be7e-e12f86259775'
SOURCE_PATH = 'icons-json/typeface/z_27cfa6e0-e0e2-4acb-be7e-e12f86259775.json'
AUTHOR = 'json_to_solo'

class Z27cfa6e0(Solo48):
    icon_id = 'z-27cfa6e0'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('z', 'typeface')

    def build(self):
        self.add_line('e0', (9, 4), (40, 4))
        self.add_line('e1', (40, 4), (8, 44))
        self.add_line('e2', (8, 44), (35, 44))
        self.add_contour('c0', 'e0', 'e1', 'e2')
