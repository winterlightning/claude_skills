"""Rectangle shape (design), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '432b99ac-4502-55ae-b924-896645c9c530'
SOURCE_PATH = 'icons-json/design/rectangle shape_432b99ac-4502-55ae-b924-896645c9c530.json'
AUTHOR = 'json_to_solo'

class RectangleShape(Solo48):
    icon_id = 'rectangle-shape'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('rectangle', 'shape', 'design')

    def build(self):
        self.add_line('e0', (40, 40), (7, 40))
        self.add_line('e1', (4, 36), (4, 12))
        self.add_line('e2', (7, 8), (42, 8))
        self.add_line('e3', (44, 12), (44, 39))
        self.add_arc('e4-1', (7, 40), (4, 37), radius_x=3)
        self.add_line('e4-2', (4, 37), (4, 36))
        self.add_line('e5-1', (4, 12), (4, 10))
        self.add_arc('e5-2', (4, 10), (6, 8), radius_x=3)
        self.add_line('e5-3', (6, 8), (7, 8))
        self.add_arc('e6-1', (42, 8), (44, 9), radius_x=3)
        self.add_line('e6-2', (44, 9), (44, 11))
        self.add_arc('e6-3', (44, 11), (44, 12), radius_x=23, sweep=False)
        self.add_line('e7', (44, 39), (40, 40))
        self.add_contour('c0', 'e0', 'e4-1', 'e4-2', 'e1', 'e5-1', 'e5-2', 'e5-3', 'e2', 'e6-1', 'e6-2', 'e6-3', 'e3', 'e7', closed=True)
