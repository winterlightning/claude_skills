"""Plus one increment (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7ae0be87-cd69-4c4e-8cc0-e351786a3597'
SOURCE_PATH = 'icons-json/interface-essential/plus one increment_7ae0be87-cd69-4c4e-8cc0-e351786a3597.json'
AUTHOR = 'json_to_solo'

class PlusOneIncrementInterfaceEssential(Solo48):
    icon_id = 'plus-one-increment-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('plus', 'one', 'increment', 'interface-essential')

    def build(self):
        self.add_line('e0', (35, 11), (37, 8))
        self.add_line('e1', (37, 8), (37, 40))
        self.add_line('e2', (29, 40), (37, 40))
        self.add_line('e3', (44, 40), (37, 40))
        self.add_line('e4', (14, 14), (14, 25))
        self.add_line('e5', (4, 25), (14, 25))
        self.add_line('e6', (14, 35), (14, 25))
        self.add_line('e7', (23, 25), (14, 25))
        self.add_bezier('e8', (29, 15), ((30.964, 14.11), (33.818, 12.95), (35, 11)))
        self.add_contour('c0', 'e8', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('c5', 'e6')
        self.add_contour('c6', 'e7')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c6')
