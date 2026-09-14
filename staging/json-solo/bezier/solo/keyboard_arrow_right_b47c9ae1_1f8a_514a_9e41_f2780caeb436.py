"""Keyboard arrow right (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b47c9ae1-1f8a-514a-9e41-f2780caeb436'
SOURCE_PATH = 'icons-json/interface-essential/keyboard arrow right_b47c9ae1-1f8a-514a-9e41-f2780caeb436.json'
AUTHOR = 'json_to_solo'

class KeyboardArrowRightB47c9ae1(Solo48):
    icon_id = 'keyboard-arrow-right-b47c9ae1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('keyboard', 'arrow', 'right', 'interface-essential')

    def build(self):
        self.add_line('e0', (44, 18), (35, 27))
        self.add_line('e1', (35, 8), (44, 17))
        self.add_line('e2', (44, 17), (14, 17))
        self.add_line('e3', (15, 40), (23, 40))
        self.add_bezier('e4', (14, 17), ((9.973, 17), (6.964, 18.58), (5.091, 22.62)), ((4.464, 23.96), (4.018, 25.59), (4.018, 27.12)), ((4.009, 27.2), (4.009, 27.28), (4, 27.36)), ((4, 27.361), (4, 27.362), (4, 27.364)), ((4, 27.442), (4.009, 27.521), (4.009, 27.6)), ((4.009, 32.99), (7.718, 37.65), (12.2, 39.35)), ((13.045, 39.66), (14.1, 40), (15, 40)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e4', 'e3')
