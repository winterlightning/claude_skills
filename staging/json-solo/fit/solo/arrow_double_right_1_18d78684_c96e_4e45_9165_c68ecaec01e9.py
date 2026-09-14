"""Arrow double right 1 (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '18d78684-c96e-4e45-9165-c68ecaec01e9'
SOURCE_PATH = 'icons-json/arrows/arrow double right 1_18d78684-c96e-4e45-9165-c68ecaec01e9.json'
AUTHOR = 'json_to_solo'

class ArrowDoubleRight1Arrows(Solo48):
    icon_id = 'arrow-double-right-1-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'double', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (4, 40), (14, 25))
        self.add_line('e1', (14, 23), (4, 8))
        self.add_line('e2', (4, 8), (14, 8))
        self.add_line('e3', (15, 9), (24, 23))
        self.add_line('e4', (24, 25), (15, 39))
        self.add_line('e5', (14, 40), (4, 40))
        self.add_line('e6', (23, 8), (33, 23))
        self.add_line('e7', (33, 25), (23, 40))
        self.add_line('e8', (25, 40), (33, 40))
        self.add_line('e9', (34, 39), (44, 25))
        self.add_line('e10', (44, 23), (35, 9))
        self.add_line('e11', (33, 8), (23, 8))
        self.add_arc('e12', (14, 25), (14, 23), radius_x=3, sweep=False)
        self.add_line('e13', (14, 8), (15, 9))
        self.add_arc('e14', (24, 23), (24, 25), radius_x=2)
        self.add_line('e15', (15, 39), (14, 40))
        self.add_arc('e16', (33, 23), (33, 25), radius_x=3)
        self.add_line('e17-1', (23, 40), (24, 40))
        self.add_arc('e17-2', (24, 40), (25, 40), radius_x=28)
        self.add_line('e18', (33, 40), (34, 39))
        self.add_line('e19', (44, 25), (44, 23))
        self.add_line('e20', (35, 9), (33, 8))
        self.add_contour('c0', 'e0', 'e12', 'e1', 'e2', 'e13', 'e3', 'e14', 'e4', 'e15', 'e5', closed=True)
        self.add_contour('c1', 'e6', 'e16', 'e7', 'e17-1', 'e17-2', 'e8', 'e18', 'e9', 'e19', 'e10', 'e20', 'e11', closed=True)
