"""Keyboard arrow right (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e04c22b8-a6e1-4e7c-b9aa-431ee1f46ae2'
SOURCE_PATH = 'icons-json/interface-essential/keyboard arrow right_e04c22b8-a6e1-4e7c-b9aa-431ee1f46ae2.json'
AUTHOR = 'json_to_solo'

class KeyboardArrowRightE04c22b8(Solo48):
    icon_id = 'keyboard-arrow-right-e04c22b8'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('keyboard', 'arrow', 'right', 'interface-essential')

    def build(self):
        self.add_line('e0', (23, 40), (15, 40))
        self.add_line('e1', (12, 18), (44, 18))
        self.add_line('e2', (35, 27), (44, 18))
        self.add_line('e3', (35, 8), (44, 18))
        self.add_bezier('e4', (15, 40), ((14.291, 40), (13.373, 39.72), (12.691, 39.49)), ((8.236, 38.02), (4.009, 33.44), (4.009, 28.04)), ((4.009, 27.961), (4, 27.892), (4, 27.814)), ((4, 27.812), (4, 27.811), (4, 27.81)), ((4, 27.54), (4.009, 27.28), (4.009, 27.01)), ((4.009, 22.11), (7.527, 18), (12, 18)))
        self.add_contour('c0', 'e0', 'e4', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
