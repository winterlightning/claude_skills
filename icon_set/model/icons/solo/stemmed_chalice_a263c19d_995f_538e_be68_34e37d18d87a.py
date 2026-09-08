"""A deep bowl on a stem and flared foot. Bounds (8,2)-(40,46)."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a263c19d-995f-538e-be68-34e37d18d87a'
SOURCE_PATH = 'pictographic-primitives/culture/batch-06/challice_a263c19d-995f-538e-be68-34e37d18d87a.svg'
AUTHOR = 'astra-chatgpt'


class StemmedChalice(Solo48):
    icon_id = 'stemmed-chalice'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture"
    aliases = ()
    keywords = ('chalice', 'goblet', 'cup', 'grail', 'wine', 'vessel', 'ceremony', 'drink', 'lucide:wine')

    def build(self) -> None:
        self.add_line("rim", (8,2), (40,2))
        self.add_line("right", (40,2), (40,12))
        self.add_arc("bowl-right", (40,12), (24,28), radius_x=16)
        self.add_arc("bowl-left", (24,28), (8,12), radius_x=16)
        self.add_line("left", (8,12), (8,2))
        self.add_contour("bowl", "rim", "right", "bowl-right", "bowl-left", "left", closed=True)
        self.add_line("stem", (24,28), (24,38))
        self.add_polyline("foot", (24,38), (14,46), (34,46), closed=True)
        self.relate("connect", "bowl", "stem")
        self.relate("connect", "stem", "foot")
