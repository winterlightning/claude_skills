"""Tarot card with a pointed almond eye; inner decorative border omitted. Bounds (8,4)-(40,44)."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a1eb9358-b279-40cf-a5b0-e27e098455a2'
SOURCE_PATH = 'pictographic-primitives/culture/batch-06/tarot_a1eb9358-b279-40cf-a5b0-e27e098455a2.svg'
AUTHOR = 'gpt-6'


class TarotCardEye(Solo48):
    icon_id = 'tarot-card-eye'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture"
    aliases = ()
    keywords = ('tarot', 'card', 'eye', 'divination', 'fortune', 'occult', 'deck', 'mystic', 'lucide:eye', 'lucide:rectangle-vertical')

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
        self.add_arc("eye-top", (17,24), (31,24), radius_x=9, radius_y=14)
        self.add_arc("eye-bottom", (31,24), (17,24), radius_x=9, radius_y=14)
        self.add_contour("eye", "eye-top", "eye-bottom", closed=True)
