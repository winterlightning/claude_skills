"""A smiling message bubble with a small overlapping reply.

HRECT_L extrema (4,8)-(44,40). Eye positions share y=17; the smile is one
gentle curve. The tiny source speck in the reply vanishes at 48 pixels.
Lucide messages-square informs the rounded two-bubble construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "8d648ec6-1ff1-4de1-a5b4-4e9f74b89aef"
SOURCE_PATH = "pictographic-primitives/_uncategorized_12/conversation smile type_8d648ec6-1ff1-4de1-a5b4-4e9f74b89aef.svg"
AUTHOR = "gpt-6"


class HappyChatBubbles(Solo48):
    icon_id = "happy-chat-bubbles"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "communication/chat"
    aliases = ("smiling speech bubble pair", "happy conversation")
    keywords = ("smile", "messages", "reply", "face")

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
        self.add_dot("eye-left",(13,17))
        self.add_dot("eye-right",(23,17))
        self.add_bezier("smile",(14,26),((16,28),(19,28),(21,26)))
        self.add_line("front-top",(34,18),(40,18))
        self.add_arc("front-ne",(40,18),(44,22),radius_x=4,radius_y=4,sweep=True)
        self.add_line("front-right",(44,22),(44,32))
        self.add_arc("front-se",(44,32),(40,36),radius_x=4,radius_y=4,sweep=True)
        self.add_line("front-bottom-right",(40,36),(38,36))
        self.add_line("front-tail-down",(38,36),(38,40))
        self.add_line("front-tail-up",(38,40),(34,36))
        self.add_arc("front-sw",(34,36),(30,32),radius_x=4,radius_y=4,sweep=True)
        self.add_line("front-left",(30,32),(30,22))
        self.add_arc("front-nw",(30,22),(34,18),radius_x=4,radius_y=4,sweep=True)
        self.add_contour("front","front-top","front-ne","front-right","front-se","front-bottom-right","front-tail-down","front-tail-up","front-sw","front-left","front-nw",closed=True)
        self.relate("connect","back","front")
