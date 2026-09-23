"""A large question bubble with a smaller reply bubble at lower right.

SQUARE extrema (6,6)-(42,42). The rear message and reply share one outline
node. The source's question hook has no dot. Lucide message-circle-question-mark
informs the hook and rounded speech silhouette.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "5a2da2f9-5219-4329-80cf-1d9d601abab0"
SOURCE_PATH = "pictographic-primitives/_uncategorized_12/conversation question warning 1_5a2da2f9-5219-4329-80cf-1d9d601abab0.svg"
AUTHOR = "gpt-6"


class QuestionMarkConversationBubbles(Solo48):
    icon_id = "question-mark-conversation-bubbles"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "communication/chat"
    aliases = ("question chat", "help conversation")
    keywords = ("question", "reply", "bubbles", "support")

    def build(self) -> None:
        self.add_line("back-right",(34,14),(34,12))
        self.add_arc("back-ne",(34,12),(28,6),radius_x=6,radius_y=6,sweep=False)
        self.add_line("back-top",(28,6),(12,6))
        self.add_arc("back-nw",(12,6),(6,12),radius_x=6,radius_y=6,sweep=False)
        self.add_line("back-left",(6,12),(6,26))
        self.add_arc("back-sw",(6,26),(12,32),radius_x=6,radius_y=6,sweep=False)
        self.add_line("back-tail-down",(12,32),(12,38))
        self.add_line("back-tail-up",(12,38),(16,34))
        self.add_line("back-bottom",(16,34),(29,32))
        self.add_contour("back","back-right","back-ne","back-top","back-nw","back-left","back-sw","back-tail-down","back-tail-up","back-bottom")
        self.add_bezier("question",(15,19),((15,16),(17,15),(20,15)),((23,15),(24,17),(23,19)),((23,21),(20,20),(20,23)),((20,24),(20,24),(20,25)))
        self.add_arc("front-nw",(29,27),(32,24),radius_x=3,radius_y=3,sweep=True)
        self.add_line("front-top",(32,24),(39,24))
        self.add_arc("front-ne",(39,24),(42,27),radius_x=3,radius_y=3,sweep=True)
        self.add_line("front-right",(42,27),(42,33))
        self.add_arc("front-se",(42,33),(39,36),radius_x=3,radius_y=3,sweep=True)
        self.add_line("front-bottom-right",(39,36),(36,36))
        self.add_line("front-tail-down",(36,36),(36,42))
        self.add_line("front-tail-up",(36,42),(32,36))
        self.add_arc("front-sw",(32,36),(29,33),radius_x=3,radius_y=3,sweep=True)
        self.add_line("front-left-low",(29,33),(29,32))
        self.add_line("front-left-high",(29,32),(29,27))
        self.add_contour("front","front-nw","front-top","front-ne","front-right","front-se","front-bottom-right","front-tail-down","front-tail-up","front-sw","front-left-low","front-left-high",closed=True)
        self.relate("connect","back","front")
