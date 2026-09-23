"""A wide rounded message card with three left-aligned text lines.

Symbol plan: a parameterized rounded rectangle encloses a three-row
text series; the first two rows match and the third is shorter.
Lucide rectangle-ellipsis informed the corner construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "cc4b9374-2d55-42d6-a0ab-68de19d30cc4"
SOURCE_PATH = "pictographic-primitives/_uncategorized_27/messages logo_cc4b9374-2d55-42d6-a0ab-68de19d30cc4.svg"
AUTHOR = "gpt-6"


class RoundedTextMessageCard(Solo48):
    icon_id = "rounded-text-message-card"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "communication/messages"
    aliases = ("message logo", "text card")
    keywords = ("chat", "writing", "lines", "note")

    def build(self) -> None:
        x1, x2, y1, y2, r = 6, 42, 6, 42, 4
        self.add_line("card-top", (x1 + r, y1), (x2 - r, y1))
        self.add_arc("card-ne", (x2 - r, y1), (x2, y1 + r), radius_x=r, sweep=True)
        self.add_line("card-right", (x2, y1 + r), (x2, y2 - r))
        self.add_arc("card-se", (x2, y2 - r), (x2 - r, y2), radius_x=r, sweep=True)
        self.add_line("card-bottom", (x2 - r, y2), (x1 + r, y2))
        self.add_arc("card-sw", (x1 + r, y2), (x1, y2 - r), radius_x=r, sweep=True)
        self.add_line("card-left", (x1, y2 - r), (x1, y1 + r))
        self.add_arc("card-nw", (x1, y1 + r), (x1 + r, y1), radius_x=r, sweep=True)
        self.add_contour("card", "card-top", "card-ne", "card-right", "card-se", "card-bottom", "card-sw", "card-left", "card-nw", closed=True)
        for name, y, end in (("text-top", 15, 33), ("text-middle", 24, 33), ("text-bottom", 33, 27)):
            self.add_line(name, (15, y), (end, y))
