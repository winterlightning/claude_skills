"""Tarot card with a crescent moon; corner ornaments omitted. Bounds (8,2)-(40,46)."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '10f87b03-becd-4543-a939-ff28e4353b11'
SOURCE_PATH = 'pictographic-primitives/culture/batch-06/tarot_10f87b03-becd-4543-a939-ff28e4353b11.svg'


class TarotCardMoon(Solo48):
    icon_id = 'tarot-card-moon'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture"
    aliases = ()
    keywords = ('tarot', 'card', 'moon', 'divination', 'fortune', 'occult', 'deck', 'mystic', 'lucide:moon', 'lucide:rectangle-vertical')

    def build(self) -> None:
        self.add_line("top", (12,2), (36,2))
        self.add_arc("ne", (36,2), (40,6), radius_x=4)
        self.add_line("right", (40,6), (40,42))
        self.add_arc("se", (40,42), (36,46), radius_x=4)
        self.add_line("bottom", (36,46), (12,46))
        self.add_arc("sw", (12,46), (8,42), radius_x=4)
        self.add_line("left", (8,42), (8,6))
        self.add_arc("nw", (8,6), (12,2), radius_x=4)
        self.add_contour("card", "top", "ne", "right", "se", "bottom", "sw", "left", "nw", closed=True)
        self.add_arc("moon-outer", (29,13), (29,35), radius_x=14, radius_y=11, sweep=False)
        self.add_arc("moon-inner", (29,35), (29,13), radius_x=5, radius_y=11)
        self.add_contour("moon", "moon-outer", "moon-inner", closed=True)
