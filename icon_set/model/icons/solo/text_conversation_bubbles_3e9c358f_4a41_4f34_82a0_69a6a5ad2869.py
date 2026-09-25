"""Two overlapping rounded message bubbles containing text strokes.

HRECT_L extrema (4,8)-(44,40). The back message has long and short text runs; the smaller reply has one
short run. Repeated corners and tail nodes stay attached.
Lucide messages-square informs the rounded two-bubble construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "3e9c358f-4a41-4f34-82a0-69a6a5ad2869"
SOURCE_PATH = "pictographic-primitives/_uncategorized_12/conversation text_3e9c358f-4a41-4f34-82a0-69a6a5ad2869.svg"
AUTHOR = "gpt-6"


class TextConversationBubbles(Solo48):
    icon_id = "text-conversation-bubbles"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("text chat", "message exchange")
    keywords = ("text", "messages", "reply", "conversation")

    def build(self) -> None:
        self.add_line("back-right",(34,18),(34,12))
        self.add_arc("back-ne",(34,12),(30,8),radius_x=4,radius_y=4,sweep=False)
        self.add_line("back-top",(30,8),(8,8))
        self.add_arc("back-nw",(8,8),(4,12),radius_x=4,radius_y=4,sweep=False)
        self.add_line("back-left",(4,12),(4,32))
        self.add_arc("back-sw",(4,32),(8,36),radius_x=4,radius_y=4,sweep=False)
        self.add_line("back-bottom",(8,36),(12,36))
        self.add_line("back-tail-down",(12,36),(12,40))
        self.add_line("back-tail-up",(12,40),(18,36))
        self.add_contour("back","back-right","back-ne","back-top","back-nw","back-left","back-sw","back-bottom","back-tail-down","back-tail-up")
        self.add_line("message-long",(13,17),(18,17))
        self.add_line("message-short",(13,25),(16,25))
        self.add_line("front-top-left",(30,18),(34,18))
        self.add_line("front-top-right",(34,18),(40,18))
        self.add_arc("front-ne",(40,18),(44,22),radius_x=4,radius_y=4,sweep=True)
        self.add_line("front-right",(44,22),(44,32))
        self.add_arc("front-se",(44,32),(40,36),radius_x=4,radius_y=4,sweep=True)
        self.add_line("front-bottom-right",(40,36),(38,36))
        self.add_line("front-tail-down",(38,36),(38,40))
        self.add_line("front-tail-up",(38,40),(34,36))
        self.add_line("front-bottom-left",(34,36),(30,36))
        self.add_arc("front-sw",(30,36),(26,32),radius_x=4,radius_y=4,sweep=True)
        self.add_line("front-left",(26,32),(26,22))
        self.add_arc("front-nw",(26,22),(30,18),radius_x=4,radius_y=4,sweep=True)
        self.add_contour("front","front-top-left","front-top-right","front-ne","front-right","front-se","front-bottom-right","front-tail-down","front-tail-up","front-bottom-left","front-sw","front-left","front-nw",closed=True)
        self.add_dot("reply-text",(35,27))
        self.relate("connect","back","front")
