"""Two round speech bubbles, a large rear bubble and smaller reply.

SQUARE extrema (6,6)-(42,42). Each bubble is an open continuous outline;
intentional asymmetry preserves the conversational overlap. Lucide
messages-square informs rounded corners and opposing tails.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "e4382b10-8ac8-4987-81ed-59d3a71384e1"
SOURCE_PATH = "pictographic-primitives/_uncategorized_12/conversation chat 2_e4382b10-8ac8-4987-81ed-59d3a71384e1.svg"
AUTHOR = "gpt-6"


class DoubleSpeechBubblesConversation(Solo48):
    icon_id = "double-speech-bubbles-conversation"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("conversation bubbles", "messages")
    keywords = ("dialogue", "speech", "two", "reply")

    def build(self) -> None:
        self.add_line("back-right",(34,13),(34,9))
        self.add_arc("back-ne",(34,9),(31,6),radius_x=3,radius_y=3,sweep=False)
        self.add_line("back-top",(31,6),(9,6))
        self.add_arc("back-nw",(9,6),(6,9),radius_x=3,radius_y=3,sweep=False)
        self.add_line("back-left",(6,9),(6,23))
        self.add_arc("back-sw",(6,23),(9,26),radius_x=3,radius_y=3,sweep=False)
        self.add_line("back-bottom",(9,26),(12,26))
        self.add_line("back-tail-down",(12,26),(12,36))
        self.add_line("back-tail-up",(12,36),(15,33))
        self.add_contour("back","back-right","back-ne","back-top","back-nw","back-left","back-sw","back-bottom","back-tail-down","back-tail-up")
        self.add_arc("front-nw",(24,25),(27,22),radius_x=3,radius_y=3,sweep=True)
        self.add_line("front-top",(27,22),(39,22))
        self.add_arc("front-ne",(39,22),(42,25),radius_x=3,radius_y=3,sweep=True)
        self.add_line("front-right",(42,25),(42,33))
        self.add_arc("front-se",(42,33),(39,36),radius_x=3,radius_y=3,sweep=True)
        self.add_line("front-bottom-right",(39,36),(36,36))
        self.add_line("front-tail-down",(36,36),(36,42))
        self.add_line("front-tail-up",(36,42),(30,36))
        self.add_line("front-bottom-left",(30,36),(27,36))
        self.add_arc("front-sw",(27,36),(24,33),radius_x=3,radius_y=3,sweep=True)
        self.add_line("front-left",(24,33),(24,25))
        self.add_contour("front","front-nw","front-top","front-ne","front-right","front-se","front-bottom-right","front-tail-down","front-tail-up","front-bottom-left","front-sw","front-left",closed=True)
