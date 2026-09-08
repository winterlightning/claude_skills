"""Tarot card with a pointed almond eye; inner decorative border omitted. Bounds (8,2)-(40,46)."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a1eb9358-b279-40cf-a5b0-e27e098455a2'
SOURCE_PATH = 'pictographic-primitives/culture/batch-06/tarot_a1eb9358-b279-40cf-a5b0-e27e098455a2.svg'
AUTHOR = 'astra-chatgpt'


class TarotCardEye(Solo48):
    icon_id = 'tarot-card-eye'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture"
    aliases = ()
    keywords = ('tarot', 'card', 'eye', 'divination', 'fortune', 'occult', 'deck', 'mystic', 'lucide:eye', 'lucide:rectangle-vertical')

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
        self.add_arc("eye-top", (15,24), (33,24), radius_x=12, radius_y=14)
        self.add_arc("eye-bottom", (33,24), (15,24), radius_x=12, radius_y=14)
        self.add_contour("eye", "eye-top", "eye-bottom", closed=True)
