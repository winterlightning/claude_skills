"""Variable font (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'de8c9243-bc9c-4c89-8720-203c0db986ff'
SOURCE_PATH = 'icons-json/interface-essential/variable font_de8c9243-bc9c-4c89-8720-203c0db986ff.json'
AUTHOR = 'json_to_solo'

class VariableFont(Solo48):
    icon_id = 'variable-font'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('variable', 'font', 'interface-essential')

    def build(self):
        self.add_line('e0', (6, 9), (6, 6))
        self.add_line('e1', (6, 6), (13, 6))
        self.add_line('e2', (10, 26), (13, 26))
        self.add_line('e3', (16, 26), (13, 26))
        self.add_line('e4', (21, 9), (21, 6))
        self.add_line('e5', (21, 6), (13, 6))
        self.add_line('e6', (13, 26), (13, 6))
        self.add_line('e7', (28, 9), (28, 6))
        self.add_line('e8', (28, 6), (35, 6))
        self.add_line('e9', (31, 26), (35, 26))
        self.add_line('e10', (38, 26), (35, 26))
        self.add_line('e11', (42, 9), (42, 6))
        self.add_line('e12', (42, 6), (35, 6))
        self.add_line('e13', (35, 26), (35, 6))
        self.add_line('e14', (6, 38), (19, 38))
        self.add_line('e15', (42, 38), (27, 38))
        self.add_arc('e16-top', (19, 38), (27, 38), radius_x=4)
        self.add_arc('e16-bottom', (27, 38), (19, 38), radius_x=4)
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4', 'e5')
        self.add_contour('c4', 'e6')
        self.add_contour('c5', 'e7', 'e8')
        self.add_contour('c6', 'e9')
        self.add_contour('c7', 'e10')
        self.add_contour('c8', 'e11', 'e12')
        self.add_contour('c9', 'e13')
        self.add_contour('c10', 'e14')
        self.add_contour('c11', 'e15')
        self.add_contour('e16', 'e16-top', 'e16-bottom', closed=True)
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c5', 'c8')
        self.relate('connect', 'c5', 'c9')
        self.relate('connect', 'c8', 'c9')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c6', 'c9')
        self.relate('connect', 'c7', 'c9')
        self.relate('connect', 'c10', 'e16')
        self.relate('connect', 'c11', 'e16')
