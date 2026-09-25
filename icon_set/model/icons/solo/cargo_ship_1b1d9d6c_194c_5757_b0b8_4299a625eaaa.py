from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1b1d9d6c-194c-5757-b0b8-4299a625eaaa'
SOURCE_PATH = 'pictographic-primitives/shipping/cargo boat_1b1d9d6c-194c-5757-b0b8-4299a625eaaa.svg'
AUTHOR = 'gpt-6-astra'


class CargoShip(Solo48):
    icon_id = 'cargo-ship'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "shipping"
    aliases = ()
    keywords = ('ship', 'cargo', 'boat', 'freight', 'sea', 'transport')

    def build(self) -> None:
        # Horizontal centerlines (4,8)-(44,40), cargo left and bridge right.
        self.add_polyline("hull", (4,28), (8,28), (24,28), (34,28), (42,28), (44,28), (38,40), (12,40), (4,28))
        self.add_polyline("cargo", (8,28), (8,10), (24,10), (24,28))
        self.add_polyline("bridge", (34,28), (34,18), (38,18), (42,18), (42,28))
        self.add_line("mast", (38,8), (38,18))
        self.relate("connect", "hull", "cargo")
        self.relate("connect", "hull", "bridge")
        self.relate("connect", "bridge", "mast")
