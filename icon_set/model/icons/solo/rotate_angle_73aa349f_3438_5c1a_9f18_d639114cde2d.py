"""Rotate angle (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '73aa349f-3438-5c1a-9f18-d639114cde2d'
SOURCE_PATH = 'icons-json/arrows/rotate angle_73aa349f-3438-5c1a-9f18-d639114cde2d.json'
AUTHOR = 'json_to_solo'

class RotateAngle(Solo48):
    icon_id = 'rotate-angle'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('rotate', 'angle', 'arrows')

    def build(self):
        self.add_line('e0', (41, 17), (35, 16))
        self.add_line('e1', (42, 9), (41, 17))
        self.add_bezier('e2', (29, 41), ((27.257, 41.368), (25.317, 41.992), (23.534, 41.992)), ((23.397, 41.992), (23.26, 42), (23.131, 42)), ((23.129, 42), (23.127, 42), (23.125, 42)), ((22.985, 42), (22.846, 41.992), (22.715, 41.992)), ((21.292, 41.992), (19.394, 41.419), (18.068, 40.936)), ((11.302, 38.449), (6.016, 31.985), (6.016, 24.581)), ((6.016, 24.335), (6, 24.082), (6, 23.836)), ((6, 23.832), (6, 23.828), (6, 23.824)), ((6, 23.567), (6.008, 23.317), (6.008, 23.067)), ((6.008, 21.562), (6.368, 19.999), (6.818, 18.567)), ((9.109, 11.285), (16.203, 6.016), (23.885, 6.016)), ((24.022, 6.016), (24.167, 6), (24.304, 6)), ((24.307, 6), (24.309, 6), (24.311, 6)), ((24.434, 6.008), (24.548, 6.008), (24.671, 6.016)), ((29.621, 6.016), (34.489, 8.373), (37.852, 11.94)), ((39.153, 13.323), (39.969, 15.421), (41, 17)))
        self.add_contour('c0', 'e2', 'e0')
        self.add_contour('c1', 'e1')
