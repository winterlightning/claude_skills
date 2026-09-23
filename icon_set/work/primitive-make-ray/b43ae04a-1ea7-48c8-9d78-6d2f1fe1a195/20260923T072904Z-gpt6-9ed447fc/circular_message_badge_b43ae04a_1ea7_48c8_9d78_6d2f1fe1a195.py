"""A round badge enclosing a smaller two-line speech bubble.

Symbol plan: concentric outer ring and inner elliptical speech contour;
two centered dashes share one length and an eight-unit vertical step.
Lucide message-circle informed the small integrated pointed tail.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "b43ae04a-1ea7-48c8-9d78-6d2f1fe1a195"
SOURCE_PATH = "pictographic-primitives/_uncategorized_27/messages bubble text_b43ae04a-1ea7-48c8-9d78-6d2f1fe1a195.svg"
AUTHOR = "gpt-6"


class CircularMessageBadge(Solo48):
    icon_id = "circular-message-badge"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "communication/messages"
    aliases = ("message bubble badge", "text chat circle")
    keywords = ("round", "chat", "speech", "text")

    def build(self) -> None:
        self.add_arc("badge-right", (24, 4), (24, 44), radius_x=20, sweep=True)
        self.add_arc("badge-left", (24, 44), (24, 4), radius_x=20, sweep=True)
        self.add_contour("badge", "badge-right", "badge-left", closed=True)

        self.add_arc("bubble-nw", (14, 24), (24, 12), radius_x=10, radius_y=12, sweep=True)
        self.add_arc("bubble-ne", (24, 12), (34, 24), radius_x=10, radius_y=12, sweep=True)
        self.add_arc("bubble-se", (34, 24), (24, 36), radius_x=10, radius_y=12, sweep=True)
        self.add_arc("bubble-sw", (24, 36), (20, 35), radius_x=10, radius_y=12, sweep=True)
        self.add_line("tail-lower", (20, 35), (17, 33))
        self.add_line("tail-upper", (17, 33), (15, 27))
        self.add_arc("bubble-left-low", (15, 27), (14, 24), radius_x=10, radius_y=12, sweep=True)
        self.add_contour("speech-bubble", "bubble-nw", "bubble-ne", "bubble-se", "bubble-sw", "tail-lower", "tail-upper", "bubble-left-low", closed=True)
        self.add_line("text-top", (23, 20), (25, 20))
        self.add_line("text-bottom", (23, 28), (25, 28))
