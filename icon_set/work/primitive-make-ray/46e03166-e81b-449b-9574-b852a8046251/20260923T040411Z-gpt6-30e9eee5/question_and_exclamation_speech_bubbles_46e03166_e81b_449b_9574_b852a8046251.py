"""A question bubble with a smaller exclamation reply.

HRECT_L extrema (4,8)-(44,40). Two attached bubble outlines share a top
node. Lucide messages-square informs opposing tails and round corners.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "46e03166-e81b-449b-9574-b852a8046251"
SOURCE_PATH = "pictographic-primitives/_uncategorized_12/conversation question warning_46e03166-e81b-449b-9574-b852a8046251.svg"
AUTHOR = "gpt-6"


class QuestionAndExclamationSpeechBubbles(Solo48):
    icon_id = "question-and-exclamation-speech-bubbles"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "communication/chat"
    aliases = ("question warning chat", "uncertain conversation")
    keywords = ("question", "exclamation", "reply", "speech")

    def build(self) -> None:
        self.add_line("back-right",(30,14),(30,12))
        self.add_arc("back-ne",(30,12),(26,8),radius_x=4,radius_y=4,sweep=False)
        self.add_line("back-top",(26,8),(8,8))
        self.add_arc("back-nw",(8,8),(4,12),radius_x=4,radius_y=4,sweep=False)
        self.add_line("back-left",(4,12),(4,26))
        self.add_arc("back-sw",(4,26),(8,30),radius_x=4,radius_y=4,sweep=False)
        self.add_line("back-bottom",(8,30),(10,30))
        self.add_line("back-tail-down",(10,30),(10,36))
        self.add_line("back-tail-up",(10,36),(16,30))
        self.add_contour("back","back-right","back-ne","back-top","back-nw","back-left","back-sw","back-bottom","back-tail-down","back-tail-up")
        self.add_bezier("question",(13,20),((13,18),(14,17),(16,17)),((18,17),(18,19),(16,20)),((15,20),(15,20),(15,21)))
        self.add_line("front-top",(30,14),(40,14))
        self.add_arc("front-ne",(40,14),(44,18),radius_x=4,radius_y=4,sweep=True)
        self.add_line("front-right",(44,18),(44,32))
        self.add_arc("front-se",(44,32),(40,36),radius_x=4,radius_y=4,sweep=True)
        self.add_line("front-bottom-right",(40,36),(38,36))
        self.add_line("front-tail-down",(38,36),(38,40))
        self.add_line("front-tail-up",(38,40),(34,36))
        self.add_line("front-bottom-left",(34,36),(30,36))
        self.add_arc("front-sw",(30,36),(26,32),radius_x=4,radius_y=4,sweep=True)
        self.add_line("front-left",(26,32),(26,18))
        self.add_arc("front-nw",(26,18),(30,14),radius_x=4,radius_y=4,sweep=True)
        self.add_contour("front","front-top","front-ne","front-right","front-se","front-bottom-right","front-tail-down","front-tail-up","front-bottom-left","front-sw","front-left","front-nw",closed=True)
        self.add_line("exclamation",(35,23),(35,27))
        self.relate("connect","back","front")
