"""Tarot card with a crescent moon; corner ornaments omitted. Bounds (8,4)-(40,44)."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '10f87b03-becd-4543-a939-ff28e4353b11'
SOURCE_PATH = 'pictographic-primitives/culture/batch-06/tarot_10f87b03-becd-4543-a939-ff28e4353b11.svg'
AUTHOR = 'gpt-6'


class TarotCardMoon(Solo48):
    icon_id = 'tarot-card-moon'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture"
    categories = ("culture", "primitives")
    aliases = ()
    keywords = ('tarot', 'card', 'moon', 'divination', 'fortune', 'occult', 'deck', 'mystic', 'lucide:moon', 'lucide:rectangle-vertical')

    def build(self) -> None:
        self.add_line("top", (12,4), (36,4))
        self.add_arc("ne", (36,4), (40,8), radius_x=4)
        self.add_line("right", (40,8), (40,40))
        self.add_arc("se", (40,40), (36,44), radius_x=4)
        self.add_line("bottom", (36,44), (12,44))
        self.add_arc("sw", (12,44), (8,40), radius_x=4)
        self.add_line("left", (8,40), (8,8))
        self.add_arc("nw", (8,8), (12,4), radius_x=4)
        self.add_contour("card", "top", "ne", "right", "se", "bottom", "sw", "left", "nw", closed=True)
        self.add_arc("moon-outer", (31,13), (31,35), radius_x=14, radius_y=11, sweep=False)
        self.add_arc("moon-inner", (31,35), (31,13), radius_x=5, radius_y=11)
        self.add_contour("moon", "moon-outer", "moon-inner", closed=True)
