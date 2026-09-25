from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4951d915-1048-4d07-8908-3f70b952de8a'
SOURCE_PATH = 'pictographic-primitives/shipping/warehouse cart package ribbon_4951d915-1048-4d07-8908-3f70b952de8a.svg'
AUTHOR = 'gpt-6-astra'


class ParcelPlatformCart(Solo48):
    icon_id = 'parcel-platform-cart'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "shipping"
    aliases = ()
    keywords = ('cart', 'parcel', 'box', 'trolley', 'warehouse', 'transport')

    def build(self) -> None:
        # Horizontal centerline extremes (4,8)-(44,40); right-side handle.
        self.add_polyline("platform", (4,34), (10,34), (28,34), (36,34))
        self.add_arc("heel", (36,34), (40,30), radius_x=4, sweep=False)
        self.add_line("upright", (40,30), (40,12))
        self.add_arc("grip", (40,12), (44,8), radius_x=4)
        self.add_contour("handle", "heel", "upright", "grip")
        self.relate("connect", "platform", "handle")
        self.add_polyline("parcel", (4,34), (4,18), (10,18), (18,18), (24,18), (30,18), (30,34), (28,34), (10,34), (4,34))
        self.add_polyline("upper", (10,18), (10,8), (24,8), (24,18))
        self.add_line("seal", (18,18), (18,26))
        self.relate("connect", "parcel", "platform")
        self.relate("connect", "parcel", "upper")
        self.relate("connect", "parcel", "seal")
        # Repeated circular wheels share a radius and baseline.
        for n, x in enumerate((10, 28)):
            self.add_arc(f"wheel-{n}-right", (x,34), (x,40), radius_x=3)
            self.add_arc(f"wheel-{n}-left", (x,40), (x,34), radius_x=3)
            self.add_contour(f"wheel-{n}", f"wheel-{n}-right", f"wheel-{n}-left", closed=True)
        for n in range(2):
            self.relate("connect", "platform", f"wheel-{n}")
            self.relate("connect", "parcel", f"wheel-{n}")
