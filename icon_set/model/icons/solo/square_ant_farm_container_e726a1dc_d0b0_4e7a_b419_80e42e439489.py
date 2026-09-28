from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "e726a1dc-d0b0-4e7a-b419-80e42e439489"
SOURCE_PATH = "pictographic-primitives/_uncategorized_19/formicarium_e726a1dc-d0b0-4e7a-b419-80e42e439489.svg"
AUTHOR = "gpt-6"

class SquareAntFarmContainer(Solo48):
    icon_id = "square-ant-farm-container"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("formicarium", "ant farm")
    keywords = ("container", "insect", "nest")

    def build(self) -> None:
        # Mirrored square enclosure; circular chamber is bisected by a continuous shelf.
        self.add_polyline("enclosure", (10, 6), (38, 6), (42, 10), (42, 38), (38, 42), (10, 42), (6, 38), (6, 10), (10, 6), closed=True)
        self.add_line("midline", (6, 24), (42, 24))
        self.add_arc("chamber-top", (17, 24), (31, 24), radius_x=7, sweep=True)
        self.add_arc("chamber-bottom", (31, 24), (17, 24), radius_x=7, sweep=True)
        self.add_contour("chamber", "chamber-top", "chamber-bottom", closed=True)
        self.relate("connect", "midline", "enclosure")
        self.relate("connect", "midline", "chamber")
