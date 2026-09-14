"""Won (money), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '18f047b9-f81e-571a-a3ea-2c4af962bcb7'
SOURCE_PATH = 'icons-json/money/won_18f047b9-f81e-571a-a3ea-2c4af962bcb7.json'
AUTHOR = 'json_to_solo'

class Won(Solo48):
    icon_id = 'won'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('won', 'money')

    def build(self):
        self.add_line('e0', (44, 8), (35, 40))
        self.add_line('e1', (35, 40), (24, 8))
        self.add_line('e2', (24, 8), (13, 39))
        self.add_line('e3', (13, 39), (4, 8))
        self.add_line('e4', (44, 23), (4, 23))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3')
        self.add_contour('c1', 'e4')
