"""Arrow thick 3 bottom right (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a175cfe6-38cd-5d00-94e0-f4c812fa06d5'
SOURCE_PATH = 'icons-json/arrows/arrow thick 3 bottom right_a175cfe6-38cd-5d00-94e0-f4c812fa06d5.json'
AUTHOR = 'json_to_solo'

class ArrowThick3BottomRightArrows(Solo48):
    icon_id = 'arrow-thick-3-bottom-right-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'bottom', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (8, 13), (26, 33))
        self.add_line('e1', (26, 33), (12, 33))
        self.add_line('e2', (12, 42), (42, 42))
        self.add_line('e3', (42, 42), (42, 14))
        self.add_line('e4', (33, 12), (33, 27))
        self.add_line('e5', (33, 27), (14, 8))
        self.add_bezier('e6', (14, 8), ((13.133, 7.1), (12.39, 6.008), (11.073, 6.008)), ((10.942, 6.008), (10.811, 6), (10.68, 6)), ((10.475, 6), (10.279, 6.008), (10.075, 6.008)), ((8.152, 6.008), (6.016, 7.915), (6.016, 9.895)), ((6.008, 10.031), (6, 10.16), (6, 10.289)), ((6, 10.291), (6, 10.293), (6, 10.295)), ((6, 11.335), (7.313, 12.28), (8, 13)))
        self.add_bezier('e7', (12, 33), ((10.396, 33), (8.422, 33.475), (7.391, 34.792)), ((6, 37.058), (6.483, 40.715), (9.232, 41.746)), ((9.821, 41.967), (10.565, 41.992), (11.187, 41.992)), ((11.269, 41.992), (11.359, 42), (11.449, 42)), ((11.539, 42), (11.91, 42), (12, 42)))
        self.add_bezier('e8', (42, 14), ((42, 13.403), (41.984, 12.987), (41.984, 12.382)), ((41.984, 10.025), (41.861, 8.291), (39.766, 6.818)), ((39.145, 6.376), (38.49, 6.008), (37.705, 6.008)), ((37.639, 6.008), (37.565, 6), (37.5, 6)), ((37.499, 6), (37.498, 6), (37.497, 6)), ((37.432, 6), (37.36, 6), (37.295, 6)), ((36.665, 6), (36.117, 6.295), (35.594, 6.614)), ((33.605, 7.816), (33, 9.758), (33, 12)))
        self.add_contour('c0', 'e6', 'e0', 'e1', 'e7', 'e2', 'e3', 'e8', 'e4', 'e5', closed=True)
