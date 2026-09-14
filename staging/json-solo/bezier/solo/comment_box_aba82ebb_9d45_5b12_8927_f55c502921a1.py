"""Comment box (chat), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aba82ebb-9d45-5b12-8927-f55c502921a1'
SOURCE_PATH = 'icons-json/chat/comment box_aba82ebb-9d45-5b12-8927-f55c502921a1.json'
AUTHOR = 'json_to_solo'

class CommentBoxAba82ebb(Solo48):
    icon_id = 'comment-box-aba82ebb'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'chat'
    aliases = ()
    keywords = ('comment', 'box', 'chat')

    def build(self):
        self.add_line('e0', (12, 40), (22, 33))
        self.add_line('e1', (22, 33), (39, 33))
        self.add_line('e2', (44, 30), (44, 12))
        self.add_line('e3', (38, 8), (8, 8))
        self.add_line('e4', (4, 13), (4, 29))
        self.add_line('e5', (8, 33), (12, 33))
        self.add_line('e6', (12, 33), (12, 40))
        self.add_bezier('e7', (39, 33), ((40.809, 33), (42.873, 32.312), (43.655, 30.804)), ((43.791, 30.535), (44, 30.312), (44, 30)))
        self.add_bezier('e8', (44, 12), ((44, 11.84), (43.991, 11.891), (43.991, 11.731)), ((43.991, 9.608), (41.873, 8.017), (39.682, 8.017)), ((39.1, 8.017), (38.527, 8), (37.945, 8)), ((37.845, 8), (38.1, 8), (38, 8)))
        self.add_bezier('e9', (8, 8), ((5.936, 8), (4.018, 9.811), (4.018, 11.613)), ((4.018, 11.941), (4, 12.269), (4, 12.598)), ((4, 12.749), (4, 12.848), (4, 13)))
        self.add_bezier('e10', (4, 29), ((4, 29.101), (4.009, 29.255), (4.009, 29.356)), ((4.009, 31.141), (5.855, 33), (8, 33)))
        self.add_contour('c0', 'e0', 'e1', 'e7', 'e2', 'e8', 'e3', 'e9', 'e4', 'e10', 'e5', 'e6', closed=True)
