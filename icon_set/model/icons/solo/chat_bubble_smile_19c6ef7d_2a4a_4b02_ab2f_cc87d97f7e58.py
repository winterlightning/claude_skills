"""A smiling oval chat bubble. HRECT_L centerline extremes (6,8)-(42,40). Lucide message-circle-heart informs the coherent oval and integrated tail; the source face is intrinsic rather than a separate hosted symbol. Retain vertical eyes and a broad curved smile, with deliberate left tail asymmetry."""
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
    category = "objects/symbols"
    aliases = ()
    keywords = ('chat', 'smile', 'bubble', 'happy', 'emoji', 'message', 'feedback', 'friendly')

    def build(self) -> None:
        self.add_arc('top',(6,23),(42,23),radius_x=20,radius_y=15)
        self.add_arc('lower-right',(42,23),(24,38),radius_x=20,radius_y=15)
        self.add_arc('lower-left',(24,38),(12,35),radius_x=20,radius_y=15)
        self.add_line('tail-low',(12,35),(6,40))
        self.add_line('tail-high',(6,40),(8,32))
        self.add_arc('left',(8,32),(6,23),radius_x=20,radius_y=15)
        self.add_contour('face','top','lower-right','lower-left','tail-low','tail-high','left',closed=True)
        self.add_line('eye-left',(18,18),(18,19))
        self.add_line('eye-right',(30,18),(30,19))
        self.add_arc('smile',(17,28),(31,28),radius_x=10,radius_y=4,sweep=False)
