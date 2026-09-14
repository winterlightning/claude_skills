"""Circular arrow (state), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a576eae9-10c6-460b-afb1-570ec971a498'
SOURCE_PATH = 'icons-json/state/circular arrow_a576eae9-10c6-460b-afb1-570ec971a498.json'
AUTHOR = 'json_to_solo'

class CircularArrowState(Solo48):
    icon_id = 'circular-arrow-state'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('circular', 'arrow', 'state')

    def build(self):
        self.add_line('e0', (41, 15), (36, 11))
        self.add_line('e1', (40, 31), (42, 26))
        self.add_line('e2', (32, 16), (41, 16))
        self.add_line('e3', (41, 16), (41, 7))
        self.add_bezier('e4', (36, 11), ((35.067, 10.223), (34.391, 9.256), (33.385, 8.585)), ((30.914, 6.957), (27.78, 6.016), (24.818, 6.016)), ((24.442, 6.016), (24.065, 6), (23.689, 6)), ((23.686, 6), (23.683, 6), (23.681, 6)), ((23.503, 6), (23.326, 6), (23.149, 6)), ((21.717, 6), (20.245, 6.352), (18.878, 6.753)), ((13.65, 8.315), (9.575, 11.883), (7.366, 16.898)), ((6.573, 18.706), (6.016, 20.76), (6.016, 22.748)), ((6.016, 22.928), (6, 23.116), (6, 23.296)), ((6, 23.3), (6, 23.304), (6, 23.307)), ((6, 23.541), (6.008, 23.783), (6.008, 24.016)), ((6.008, 31.56), (11.032, 38.343), (18.044, 40.895)), ((19.688, 41.501), (21.529, 41.984), (23.296, 41.984)), ((23.558, 41.984), (23.82, 42), (24.082, 42)), ((24.087, 42), (24.092, 42), (24.097, 42)), ((24.411, 42), (24.725, 41.984), (25.039, 41.984)), ((30.766, 41.984), (36.445, 38.155), (39.284, 33.319)), ((39.644, 32.714), (39.779, 31.671), (40, 31)))
        self.add_contour('c0', 'e0', 'e4', 'e1')
        self.add_contour('c1', 'e2', 'e3')
        self.relate('connect', 'c0', 'c1')
