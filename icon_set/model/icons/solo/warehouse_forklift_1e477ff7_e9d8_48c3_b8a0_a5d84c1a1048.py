from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1e477ff7-e9d8-48c3-b8a0-a5d84c1a1048'
SOURCE_PATH = 'pictographic-primitives/shipping/warehouse truck delivery_1e477ff7-e9d8-48c3-b8a0-a5d84c1a1048.svg'
AUTHOR = 'gpt-6-astra'


class WarehouseForklift(Solo48):
    icon_id = 'warehouse-forklift'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "shipping"
    aliases = ()
    keywords = ('forklift', 'warehouse', 'truck', 'lifting', 'freight', 'transport')

    def build(self) -> None:
        # Horizontal centerlines (4,8)-(44,40); mast and fork face left.
        self.add_polyline("fork", (4,34), (9,34), (9,8))
        self.add_polyline("cab-top", (23,25), (25,12))
        self.add_arc("roof-round", (25,12), (29,8), radius_x=4)
        self.add_line("roof", (29,8), (40,8))
        self.add_line("cab-back", (40,8), (40,25))
        self.add_contour("cab", "roof-round", "roof", "cab-back")
        self.relate("connect", "cab-top", "cab")
        self.add_polyline("body", (23,30), (23,25), (40,25), (44,25), (44,35), (43,35))
        self.relate("connect", "cab-top", "body")
        self.relate("connect", "cab", "body")
        # Repeated circular wheels share a radius and baseline.
        for n, x in enumerate((23, 38)):
            self.add_arc(f"wheel-{n}-right", (x,30), (x,40), radius_x=5)
            self.add_arc(f"wheel-{n}-left", (x,40), (x,30), radius_x=5)
            self.add_contour(f"wheel-{n}", f"wheel-{n}-right", f"wheel-{n}-left", closed=True)
        self.add_line("axle", (28,35), (33,35))
        self.relate("connect", "body", "wheel-0")
        self.relate("connect", "body", "wheel-1")
        self.relate("connect", "axle", "wheel-0")
        self.relate("connect", "axle", "wheel-1")
