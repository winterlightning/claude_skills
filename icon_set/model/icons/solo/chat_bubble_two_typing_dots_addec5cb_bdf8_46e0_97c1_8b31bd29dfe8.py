"""A two-lobed, cloudlike message bubble with two typing dots.

Symbol plan: a small left lobe joins a larger right lobe at two deliberate
notches; the dots share a horizontal baseline. Lucide cloud informed the
unequal lobes and continuous silhouette, without adding a speech tail.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "addec5cb-bdf8-46e0-97c1-8b31bd29dfe8"
SOURCE_PATH = "pictographic-primitives/_uncategorized_27/messages bubble typing_addec5cb-bdf8-46e0-97c1-8b31bd29dfe8.svg"
AUTHOR = "gpt-6"


class ChatBubbleTwoTypingDots(Solo48):
    icon_id = "chat-bubble-two-typing-dots"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("two-dot message", "cloud bubble typing")
    keywords = ("chat", "speech", "ellipsis", "lobed")

    def build(self) -> None:
        self.add_arc("upper-left-lobe", (15, 14), (4, 25), radius_x=11, sweep=False)
        self.add_arc("lower-left-lobe", (4, 25), (15, 36), radius_x=11, sweep=False)
        self.add_arc("lower-bulge-left", (15, 36), (22, 40), radius_x=7, radius_y=4, sweep=False)
        self.add_arc("lower-bulge-right", (22, 40), (29, 38), radius_x=7, radius_y=2, sweep=False)
        self.add_arc("large-right-lower", (29, 38), (44, 23), radius_x=15, sweep=False)
        self.add_arc("large-right-upper", (44, 23), (29, 8), radius_x=15, sweep=False)
        self.add_arc("large-top-left", (29, 8), (18, 15), radius_x=11, radius_y=7, sweep=False)
        self.add_line("lobe-notch", (18, 15), (15, 14))
        self.add_contour("bubble", "upper-left-lobe", "lower-left-lobe", "lower-bulge-left", "lower-bulge-right", "large-right-lower", "large-right-upper", "large-top-left", "lobe-notch", closed=True)
        self.add_dot("typing-left", (15, 25))
        self.add_dot("typing-right", (25, 25))
