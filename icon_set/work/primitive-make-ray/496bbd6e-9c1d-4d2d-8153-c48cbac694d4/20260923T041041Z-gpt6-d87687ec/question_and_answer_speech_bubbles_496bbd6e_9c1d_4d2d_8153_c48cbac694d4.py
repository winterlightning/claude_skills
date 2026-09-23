"""A question bubble answered by a check-mark speech bubble.

HRECT_L extrema (4,8)-(44,40). The two bubbles share a top node; the second
is lower and to the right as in the source. Lucide messages-square guides
the rounded overlapping contours.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "496bbd6e-9c1d-4d2d-8153-c48cbac694d4"
SOURCE_PATH = "pictographic-primitives/_uncategorized_13/counseling 3_496bbd6e-9c1d-4d2d-8153-c48cbac694d4.svg"
AUTHOR = "gpt-6"


class QuestionAndAnswerSpeechBubbles(Solo48):
    icon_id = "question-and-answer-speech-bubbles"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "communication/chat"
    aliases = ("counseling", "question answered")
    keywords = ("question", "check", "answer", "conversation")

    def build(self) -> None:
        self.add_line("back-right",(32,16),(32,12))
        self.add_arc("back-ne",(32,12),(28,8),radius_x=4,radius_y=4,sweep=False)
        self.add_line("back-top",(28,8),(8,8))
        self.add_arc("back-nw",(8,8),(4,12),radius_x=4,radius_y=4,sweep=False)
        self.add_line("back-left",(4,12),(4,28))
        self.add_arc("back-sw",(4,28),(8,32),radius_x=4,radius_y=4,sweep=False)
        self.add_line("back-bottom",(8,32),(10,32))
        self.add_line("back-tail-down",(10,32),(10,40))
        self.add_line("back-tail-up",(10,40),(18,32))
        self.add_contour("back","back-right","back-ne","back-top","back-nw","back-left","back-sw","back-bottom","back-tail-down","back-tail-up")
        self.add_bezier("question",(14,20),((14,18),(15,17),(16,17)),((17,17),(17,19),(16,20)),((16,21),(16,21),(16,23)))
        self.add_line("front-top-left",(30,16),(32,16))
        self.add_line("front-top-right",(32,16),(40,16))
        self.add_arc("front-ne",(40,16),(44,20),radius_x=4,radius_y=4,sweep=True)
        self.add_line("front-right",(44,20),(44,34))
        self.add_arc("front-se",(44,34),(40,38),radius_x=4,radius_y=4,sweep=True)
        self.add_line("front-bottom-right",(40,38),(38,38))
        self.add_line("front-tail-down",(38,38),(38,40))
        self.add_line("front-tail-up",(38,40),(34,38))
        self.add_line("front-bottom-left",(34,38),(30,38))
        self.add_arc("front-sw",(30,38),(25,33),radius_x=5,radius_y=5,sweep=True)
        self.add_line("front-left",(25,33),(25,21))
        self.add_arc("front-nw",(25,21),(30,16),radius_x=5,radius_y=5,sweep=True)
        self.add_contour("front","front-top-left","front-top-right","front-ne","front-right","front-se","front-bottom-right","front-tail-down","front-tail-up","front-bottom-left","front-sw","front-left","front-nw",closed=True)
        self.add_polyline("check",(34,26),(35,29),(35,25))
        self.relate("connect","back","front")
