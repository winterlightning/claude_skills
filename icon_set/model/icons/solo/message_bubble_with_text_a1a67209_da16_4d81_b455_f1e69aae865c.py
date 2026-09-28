"""An oval speech bubble with three lines of message text.

Symbol plan: one continuous speech outline with an integrated lower-left
tail; three text runs form a short-long-short series at eight-unit spacing.
Lucide message-square-text informed the attached tail and content rhythm.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "a1a67209-da16-4d81-b455-f1e69aae865c"
SOURCE_PATH = "pictographic-primitives/_uncategorized_27/messages bubble text 1_a1a67209-da16-4d81-b455-f1e69aae865c.svg"
AUTHOR = "gpt-6"


class MessageBubbleWithText(Solo48):
    icon_id = "message-bubble-with-text"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "communication/messages"
    aliases = ("text message bubble", "chat with text")
    keywords = ("speech", "conversation", "message", "lines")

    def build(self) -> None:
        rx, ry = 18, 17
        self.add_arc("bubble-nw", (6, 23), (24, 6), radius_x=rx, radius_y=ry, sweep=True)
        self.add_arc("bubble-ne", (24, 6), (42, 23), radius_x=rx, radius_y=ry, sweep=True)
        self.add_arc("bubble-se", (42, 23), (24, 40), radius_x=rx, radius_y=ry, sweep=True)
        self.add_arc("bubble-sw", (24, 40), (14, 37), radius_x=rx, radius_y=ry, sweep=True)
        self.add_line("tail-lower", (14, 37), (9, 42))
        self.add_line("tail-upper", (9, 42), (10, 31))
        self.add_line("bubble-left", (10, 31), (6, 23))
        self.add_contour("speech-outline", "bubble-nw", "bubble-ne", "bubble-se", "bubble-sw", "tail-lower", "tail-upper", "bubble-left", closed=True)
        self.add_line("text-top", (20, 15), (28, 15))
        self.add_line("text-middle", (16, 23), (32, 23))
        self.add_line("text-bottom", (20, 31), (28, 31))
