from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f70dfc47-8ff7-4234-bde3-e6c50611a8e7'
SOURCE_PATH = 'pictographic-primitives/shipping/warehouse cart packages_f70dfc47-8ff7-4234-bde3-e6c50611a8e7.svg'
AUTHOR = 'gpt-6-astra'


class LoadedPlatformCart(Solo48):
    icon_id = 'loaded-platform-cart'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "shipping"
    aliases = ()
    keywords = ('cart', 'parcel', 'package', 'warehouse', 'trolley', 'transport')

    def build(self) -> None:
        # Horizontal centerline extremes (4,8)-(44,40); left-side handle.
        self.add_polyline("handle-top", (8,8), (4,8), (4,30))
        self.add_arc("heel", (4,30), (8,34), radius_x=4, sweep=False)
        self.add_polyline("platform", (8,34), (20,34), (38,34), (44,34))
        self.relate("connect", "handle-top", "heel")
        self.relate("connect", "heel", "platform")
        self.add_polyline("load", (16,34), (16,18), (24,18), (30,18), (36,18), (44,18), (44,34), (38,34), (30,34), (20,34), (16,34))
        self.add_line("division", (30,18), (30,34))
        self.add_polyline("upper", (24,18), (24,8), (36,8), (36,18))
        self.relate("connect", "load", "division")
        self.relate("connect", "load", "upper")
        self.relate("connect", "load", "platform")
        self.relate("connect", "platform", "division")
        # Repeated circular wheels share a radius and baseline.
        for n, x in enumerate((20, 38)):
            self.add_arc(f"wheel-{n}-right", (x,34), (x,40), radius_x=3)
            self.add_arc(f"wheel-{n}-left", (x,40), (x,34), radius_x=3)
            self.add_contour(f"wheel-{n}", f"wheel-{n}-right", f"wheel-{n}-left", closed=True)
        for n in range(2):
            self.relate("connect", "platform", f"wheel-{n}")
            self.relate("connect", "load", f"wheel-{n}")
