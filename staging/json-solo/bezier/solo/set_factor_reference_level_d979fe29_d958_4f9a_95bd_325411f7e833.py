"""Set factor reference level (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd979fe29-d958-4f9a-95bd-325411f7e833'
SOURCE_PATH = 'icons-json/interface-essential/set factor reference level_d979fe29-d958-4f9a-95bd-325411f7e833.json'
AUTHOR = 'json_to_solo'

class SetFactorReferenceLevelInterfaceEssential(Solo48):
    icon_id = 'set-factor-reference-level-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('set', 'factor', 'reference', 'level', 'interface-essential')

    def build(self):
        self.add_line('e0', (8, 4), (8, 44))
        self.add_line('e1', (40, 26), (16, 26))
        self.add_line('e2', (40, 39), (16, 39))
        self.add_line('e3', (28, 11), (16, 11))
        self.add_line('e4', (40, 11), (36, 11))
        self.add_arc('e5-top', (28, 11), (36, 11), radius_x=4)
        self.add_arc('e5-bottom', (36, 11), (28, 11), radius_x=4)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.relate('connect', 'c4', 'e5')
