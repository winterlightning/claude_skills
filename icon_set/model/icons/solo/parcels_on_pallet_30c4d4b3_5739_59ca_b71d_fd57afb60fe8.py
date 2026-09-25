from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '30c4d4b3-5739-59ca-b71d-fd57afb60fe8'
SOURCE_PATH = 'pictographic-primitives/shipping/warehouse packages_30c4d4b3-5739-59ca-b71d-fd57afb60fe8.svg'
AUTHOR = 'gpt-6-astra'


class ParcelsOnPallet(Solo48):
    icon_id = 'parcels-on-pallet'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "shipping"
    aliases = ()
    keywords = ('parcel', 'pallet', 'warehouse', 'stack', 'freight', 'storage')

    def build(self) -> None:
        # Square centerlines (6,6)-(42,42); pallet has 8-unit depth.
        self.add_polyline("upper", (16,18), (16,6), (32,6), (32,18))
        self.add_polyline("load", (8,34), (8,18), (16,18), (24,18), (32,18), (40,18), (40,34), (24,34), (8,34))
        self.add_line("division", (24,18), (24,34))
        self.add_polyline("pallet-top", (6,34), (8,34), (14,34), (24,34), (34,34), (40,34), (42,34))
        self.add_polyline("pallet-bottom", (6,42), (14,42), (34,42), (42,42))
        for x in (14,34):
            self.add_line(f"support-{x}", (x,34), (x,42))
            self.relate("connect", "pallet-top", f"support-{x}")
            self.relate("connect", "pallet-bottom", f"support-{x}")
            self.relate("connect", "load", f"support-{x}")
        self.relate("connect", "upper", "load")
        self.relate("connect", "load", "division")
        self.relate("connect", "load", "pallet-top")
        self.relate("connect", "division", "pallet-top")
