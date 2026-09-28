from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "6638dde1-f82d-45e5-9acf-2ac56c0bb9f4"
SOURCE_PATH = "pictographic-primitives/_uncategorized_22/home improvement 10_6638dde1-f82d-45e5-9acf-2ac56c0bb9f4.svg"
AUTHOR = "gpt-6"

class BathroomSinkWithWaterDrop(Solo48):
    icon_id = "bathroom-sink-with-water-drop"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/plumbing"
    aliases = ("sink and droplet",)
    keywords = ("basin", "faucet", "drain", "water")

    def build(self) -> None:
        # Basin, attached faucet and drain occupy the right; droplet sits at lower left.
        self.add_polyline("basin", (22, 18), (42, 18), (40, 24), (38, 28), (26, 28), (24, 24), (22, 18), closed=True)
        self.add_polyline("faucet", (28, 14), (28, 10), (30, 6), (34, 6), (36, 10), (36, 18))
        self.relate("connect", "faucet", "basin")
        self.add_polyline("drainpipe", (30, 28), (30, 36), (34, 40), (38, 36), (38, 32), (42, 32))
        self.relate("connect", "drainpipe", "basin")
        self.add_polyline("droplet", (12, 30), (18, 38), (16, 42), (8, 42), (6, 38), (12, 30), closed=True)
