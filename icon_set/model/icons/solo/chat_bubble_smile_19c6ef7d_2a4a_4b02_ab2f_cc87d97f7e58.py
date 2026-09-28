'Smiling chat bubble: smooth rounded bubble and tail with centrally balanced eyes and smile.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '19c6ef7d-2a4a-4b02-ab2f-cc87d97f7e58'
SOURCE_PATH = 'pictographic-primitives/symbol/messages bubble round smile_19c6ef7d-2a4a-4b02-ab2f-cc87d97f7e58.svg'
AUTHOR = 'gpt-6'


class ChatBubbleSmile(Solo48):
    icon_id = 'chat-bubble-smile'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol", "state")
    aliases = ()
    keywords = ('chat', 'smile', 'bubble', 'happy', 'emoji', 'message', 'feedback', 'friendly')

    def build(self) -> None:
        self.add_bezier('upper',(4,23),((4,14),(13,8),(24,8)),((35,8),(44,14),(44,23)))
        self.add_bezier('lower',(44,23),((44,33),(34,40),(24,40)),((19,40),(16,39),(13,36)))
        self.add_polyline('tail',(13,36),(4,40),(7,31))
        self.add_bezier('side',(7,31),((5,29),(4,26),(4,23)))
        self.relate('connect','upper','lower');self.relate('connect','lower','tail');self.relate('connect','tail','side');self.relate('connect','side','upper')
        self.add_dot('eye-left',(18,18));self.add_dot('eye-right',(30,18))
        self.add_arc('smile',(18,28),(30,28),radius_x=6,radius_y=3,sweep=False)
