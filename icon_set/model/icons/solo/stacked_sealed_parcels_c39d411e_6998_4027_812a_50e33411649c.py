from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c39d411e-6998-4027-812a-50e33411649c'
SOURCE_PATH = 'pictographic-primitives/shipping/packages_c39d411e-6998-4027-812a-50e33411649c.svg'
AUTHOR = 'gpt-6-astra'


class StackedSealedParcels(Solo48):
    icon_id = 'stacked-sealed-parcels'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "shipping"
    aliases = ()
    keywords = ('parcel', 'stack', 'box', 'shipping', 'package', 'freight')

    def build(self) -> None:
        # Three physically stacked cartons, shared horizontal support line.
        self.add_polyline("upper", (15,24), (15,6), (24,6), (33,6), (33,24))
        self.add_polyline("lower", (6,24), (15,24), (24,24), (33,24), (42,24), (42,42), (24,42), (6,42), (6,24))
        self.add_line("divider", (24,24), (24,42))
        self.add_line("upper-seal", (24,6), (24,14))
        self.add_line("left-seal", (15,24), (15,32))
        self.add_line("right-seal", (33,24), (33,32))
        self.relate("connect", "upper", "lower")
        self.relate("connect", "upper", "upper-seal")
        for part in ("divider", "left-seal", "right-seal"):
            self.relate("connect", "lower", part)
        for part in ("left-seal", "right-seal"):
            self.relate("connect", "upper", part)
