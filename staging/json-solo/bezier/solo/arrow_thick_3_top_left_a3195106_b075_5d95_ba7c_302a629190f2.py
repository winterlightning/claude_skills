"""Arrow thick 3 top left (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a3195106-b075-5d95-ba7c-302a629190f2'
SOURCE_PATH = 'icons-json/arrows/arrow thick 3 top left_a3195106-b075-5d95-ba7c-302a629190f2.json'
AUTHOR = 'json_to_solo'

class ArrowThick3TopLeftArrows(Solo48):
    icon_id = 'arrow-thick-3-top-left-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'top', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (15, 21), (34, 40))
        self.add_line('e1', (40, 35), (22, 15))
        self.add_line('e2', (22, 15), (36, 15))
        self.add_line('e3', (36, 6), (6, 6))
        self.add_line('e4', (6, 6), (6, 34))
        self.add_line('e5', (15, 36), (15, 21))
        self.add_bezier('e6', (34, 40), ((34.867, 40.9), (35.61, 41.992), (36.927, 41.992)), ((37.058, 41.992), (37.189, 42), (37.32, 42)), ((37.525, 42), (37.721, 41.992), (37.925, 41.992)), ((39.848, 41.992), (41.984, 40.085), (41.984, 38.097)), ((41.992, 37.968), (42, 37.84), (42, 37.711)), ((42, 37.709), (42, 37.707), (42, 37.705)), ((42, 36.665), (40.687, 35.72), (40, 35)))
        self.add_bezier('e7', (36, 15), ((37.604, 15), (39.578, 14.525), (40.609, 13.208)), ((42, 10.942), (41.517, 7.285), (38.768, 6.254)), ((38.179, 6.033), (37.435, 6.008), (36.813, 6.008)), ((36.731, 6.008), (36.641, 6), (36.551, 6)), ((36.461, 6), (36.09, 6), (36, 6)))
        self.add_bezier('e8', (6, 34), ((6, 34.597), (6.016, 35.013), (6.016, 35.618)), ((6.016, 37.975), (6.139, 39.709), (8.234, 41.182)), ((8.855, 41.624), (9.51, 41.992), (10.295, 41.992)), ((10.361, 41.992), (10.435, 42), (10.5, 42)), ((10.501, 42), (10.502, 42), (10.503, 42)), ((10.568, 42), (10.64, 42), (10.705, 41.992)), ((11.335, 41.992), (11.883, 41.705), (12.406, 41.386)), ((14.395, 40.184), (15, 38.242), (15, 36)))
        self.add_contour('c0', 'e0', 'e6', 'e1', 'e2', 'e7', 'e3', 'e4', 'e8', 'e5', closed=True)
