"""Arrow thick 3 bottom left (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ddd7ea21-d806-5134-a35f-80d2eb3aa660'
SOURCE_PATH = 'icons-json/arrows/arrow thick 3 bottom left_ddd7ea21-d806-5134-a35f-80d2eb3aa660.json'
AUTHOR = 'json_to_solo'

class ArrowThick3BottomLeftArrows(Solo48):
    icon_id = 'arrow-thick-3-bottom-left-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'bottom', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (21, 33), (40, 14))
        self.add_line('e1', (35, 8), (15, 26))
        self.add_line('e2', (15, 26), (15, 12))
        self.add_line('e3', (6, 12), (6, 42))
        self.add_line('e4', (6, 42), (34, 42))
        self.add_line('e5', (36, 33), (21, 33))
        self.add_bezier('e6', (40, 14), ((40.9, 13.133), (41.992, 12.39), (41.992, 11.073)), ((41.992, 10.942), (42, 10.811), (42, 10.68)), ((42, 10.475), (41.992, 10.279), (41.992, 10.075)), ((41.992, 8.152), (40.085, 6.016), (38.097, 6.016)), ((37.968, 6.008), (37.84, 6), (37.711, 6)), ((37.709, 6), (37.707, 6), (37.705, 6)), ((36.665, 6), (35.72, 7.313), (35, 8)))
        self.add_bezier('e7', (15, 12), ((15, 10.396), (14.525, 8.422), (13.208, 7.391)), ((10.942, 6), (7.285, 6.483), (6.254, 9.232)), ((6.033, 9.821), (6.008, 10.565), (6.008, 11.187)), ((6.008, 11.269), (6, 11.359), (6, 11.449)), ((6, 11.539), (6, 11.91), (6, 12)))
        self.add_bezier('e8', (34, 42), ((34.597, 42), (35.013, 41.984), (35.618, 41.984)), ((37.975, 41.984), (39.709, 41.861), (41.182, 39.766)), ((41.624, 39.145), (41.992, 38.49), (41.992, 37.705)), ((41.992, 37.639), (42, 37.565), (42, 37.5)), ((42, 37.499), (42, 37.498), (42, 37.497)), ((42, 37.432), (42, 37.36), (41.992, 37.295)), ((41.992, 36.665), (41.705, 36.117), (41.386, 35.594)), ((40.184, 33.605), (38.242, 33), (36, 33)))
        self.add_contour('c0', 'e0', 'e6', 'e1', 'e2', 'e7', 'e3', 'e4', 'e8', 'e5', closed=True)
