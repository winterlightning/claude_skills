"""Rotate angle (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '73aa349f-3438-5c1a-9f18-d639114cde2d'
SOURCE_PATH = 'icons-json/arrows/rotate angle_73aa349f-3438-5c1a-9f18-d639114cde2d.json'
AUTHOR = 'json_to_solo'

class RotateAngleArrows(Solo48):
    icon_id = 'rotate-angle-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('rotate', 'angle', 'arrows')

    def build(self):
        self.add_line('e0', (41, 17), (35, 16))
        self.add_line('e1', (42, 9), (41, 17))
        self.add_arc('e2-1', (29, 41), (23, 42), radius_x=22)
        self.add_arc('e2-2', (23, 42), (6, 24), radius_x=19)
        self.add_arc('e2-3', (6, 24), (24, 6), radius_x=18)
        self.add_arc('e2-4', (24, 6), (41, 17), radius_x=19)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e0')
        self.add_contour('c1', 'e1')
