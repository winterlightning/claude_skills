from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4951d915-1048-4d07-8908-3f70b952de8a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__parcel-platform-cart/20260927T093511Z-thuan-mac-1/reference/warehouse cart package ribbon_4951d915-1048-4d07-8908-3f70b952de8a.svg'
AUTHOR = "gpt-6"


class ParcelPlatformCart(Solo48):
    icon_id = 'parcel-platform-cart'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "shipping"
    categories = ("primitives", "shipping")
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
        self.add_polyline("parcel", (14,18), (10,18), (4,18), (4,34), (10,34), (28,34), (30,34), (30,18), (24,18), (22,18))
        self.add_polyline("upper", (10,18), (10,8), (24,8), (24,18))
        self.add_polyline("ribbon-tail", (14,18), (14,26), (18,22), (22,26), (22,18))
        self.relate("connect", "parcel", "platform")
        self.relate("connect", "parcel", "upper")
        self.relate("connect", "parcel", "ribbon-tail")
        # Repeated circular wheels share a radius and baseline.
        for n, x in enumerate((10, 28)):
            self.add_arc(f"wheel-{n}-right", (x,34), (x,40), radius_x=3)
            self.add_arc(f"wheel-{n}-left", (x,40), (x,34), radius_x=3)
            self.add_contour(f"wheel-{n}", f"wheel-{n}-right", f"wheel-{n}-left", closed=True)
        for n in range(2):
            self.relate("connect", "platform", f"wheel-{n}")
            self.relate("connect", "parcel", f"wheel-{n}")
