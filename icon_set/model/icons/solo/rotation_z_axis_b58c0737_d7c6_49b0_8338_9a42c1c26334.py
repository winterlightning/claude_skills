"""Rotation z axis (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b58c0737-d7c6-49b0-8338-9a42c1c26334'
SOURCE_PATH = 'icons-json/arrows/rotation z axis_b58c0737-d7c6-49b0-8338-9a42c1c26334.json'
AUTHOR = 'json_to_solo'

class RotationZAxis(Solo48):
    icon_id = 'rotation-z-axis'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('rotation', 'z', 'axis', 'arrows')

    def build(self):
        self.add_line('e0', (9, 13), (8, 14))
        self.add_line('e1', (8, 14), (13, 14))
        self.add_line('e2', (8, 8), (8, 14))
        self.add_arc('e3-top', (20, 24), (28, 24), radius_x=4)
        self.add_arc('e3-bottom', (28, 24), (20, 24), radius_x=4)
        self.add_line('e4-1', (6, 22), (7, 30))
        self.add_arc('e4-2', (7, 30), (14, 39), radius_x=20, sweep=False)
        self.add_arc('e4-3', (14, 39), (18, 41), radius_x=18, sweep=False)
        self.add_line('e4-4', (18, 41), (24, 42))
        self.add_arc('e4-5', (24, 42), (42, 24), radius_x=18, sweep=False)
        self.add_arc('e4-6', (42, 24), (24, 6), radius_x=18, sweep=False)
        self.add_line('e4-7', (24, 6), (18, 7))
        self.add_arc('e4-8', (18, 7), (9, 13), radius_x=21, sweep=False)
        self.add_contour('c0', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e4-6', 'e4-7', 'e4-8', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
