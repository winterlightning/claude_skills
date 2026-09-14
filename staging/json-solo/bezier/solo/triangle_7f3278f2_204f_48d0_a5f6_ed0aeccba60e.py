"""Triangle (design), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7f3278f2-204f-48d0-a5f6-ed0aeccba60e'
SOURCE_PATH = 'icons-json/design/triangle_7f3278f2-204f-48d0-a5f6-ed0aeccba60e.json'
AUTHOR = 'json_to_solo'

class Triangle7f3278f2(Solo48):
    icon_id = 'triangle-7f3278f2'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('triangle', 'design')

    def build(self):
        self.add_line('e0', (44, 40), (24, 8))
        self.add_line('e1', (24, 8), (4, 40))
        self.add_line('e2', (4, 40), (44, 40))
        self.add_contour('c0', 'e0', 'e1', 'e2', closed=True)
