"""Bookmark (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1c26a9c6-fac8-4352-bc90-e409954efaf5'
SOURCE_PATH = 'icons-json/interface-essential/bookmark_1c26a9c6-fac8-4352-bc90-e409954efaf5.json'
AUTHOR = 'json_to_solo'

class Bookmark1c26a9c6(Solo48):
    icon_id = 'bookmark-1c26a9c6'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('bookmark', 'interface-essential')

    def build(self):
        self.add_line('e0', (8, 44), (23, 33))
        self.add_line('e1', (26, 34), (40, 44))
        self.add_line('e2', (40, 44), (40, 32))
        self.add_line('e3', (40, 32), (40, 7))
        self.add_line('e4', (36, 4), (11, 4))
        self.add_line('e5', (8, 7), (8, 44))
        self.add_bezier('e6', (23, 33), ((24.8, 32.855), (24.64, 33.027), (26, 34)))
        self.add_bezier('e7', (40, 7), ((39.99, 6.855), (39.99, 6.445), (39.98, 6.3)), ((39.98, 5.255), (38.72, 4), (37.55, 4)), ((37.4, 4), (37.25, 4.009), (37.1, 4.009)), ((36.95, 4.009), (36.81, 4.009), (36.66, 4)), ((36.58, 4), (36.51, 4), (36.44, 4)), ((36.29, 4), (36.15, 4), (36, 4)))
        self.add_bezier('e8', (11, 4), ((10.94, 4), (10.87, 4), (10.81, 4)), ((9.5, 4), (8, 5.282), (8, 6.5)), ((8, 6.582), (8, 6.927), (8, 7)))
        self.add_contour('c0', 'e0', 'e6', 'e1', 'e2', 'e3', 'e7', 'e4', 'e8', 'e5', closed=True)
