"""Hierarchy (programing), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '74cd9468-a057-5e62-8b17-2fbc2ef92c08'
SOURCE_PATH = 'icons-json/programing/hierarchy_74cd9468-a057-5e62-8b17-2fbc2ef92c08.json'
AUTHOR = 'json_to_solo'

class Hierarchy74cd9468(Solo48):
    icon_id = 'hierarchy-74cd9468'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('hierarchy', 'programing')

    def build(self):
        self.add_line('e0', (23, 16), (12, 32))
        self.add_line('e1', (25, 16), (36, 32))
        self.add_line('e2', (32, 36), (16, 36))
        self.add_arc('e3-top', (19, 11), (29, 11), radius_x=5)
        self.add_arc('e3-bottom', (29, 11), (19, 11), radius_x=5)
        self.add_arc('e4-top', (6, 37), (16, 37), radius_x=5)
        self.add_arc('e4-bottom', (16, 37), (6, 37), radius_x=5)
        self.add_arc('e5-top', (32, 37), (42, 37), radius_x=5)
        self.add_arc('e5-bottom', (42, 37), (32, 37), radius_x=5)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'e3')
        self.relate('connect', 'c0', 'e4')
        self.relate('connect', 'c1', 'e3')
        self.relate('connect', 'c1', 'e5')
        self.relate('connect', 'c2', 'e5')
        self.relate('connect', 'c2', 'e4')
