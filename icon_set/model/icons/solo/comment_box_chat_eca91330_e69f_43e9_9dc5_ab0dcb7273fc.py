"""Comment box (chat), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'eca91330-e69f-43e9-9dc5-ab0dcb7273fc'
SOURCE_PATH = 'icons-json/chat/comment box_eca91330-e69f-43e9-9dc5-ab0dcb7273fc.json'
AUTHOR = 'gpt-6'

class CommentBoxChat(Solo48):
    icon_id = 'comment-box-chat'
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
        self.add_line('e4', (4, 13), (4, 29))
        self.add_line('e5', (8, 33), (12, 33))
        self.add_line('e6', (12, 33), (12, 40))
        self.add_arc('e7', (39, 33), (44, 30), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('e8-1', (44, 12), (40, 8), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('e8-2', (40, 8), (8, 8))
        self.add_line('e9-1', (8, 8), (5, 9))
        self.add_line('e9-2', (5, 9), (4, 13))
        self.add_arc('e10', (4, 29), (8, 33), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e7', 'e2', 'e8-1', 'e8-2', 'e9-1', 'e9-2', 'e4', 'e10', 'e5', 'e6', closed=True)
