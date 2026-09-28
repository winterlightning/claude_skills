from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '31bbb1ad-764f-41fb-8c90-de6d0596385a'
SOURCE_PATH = 'pictographic-primitives/shipping/warehouse cart_31bbb1ad-764f-41fb-8c90-de6d0596385a.svg'
AUTHOR = 'gpt-6-astra'


class PalletJack(Solo48):
    icon_id = 'pallet-jack'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "shipping"
    categories = ("primitives", "shipping")
    aliases = ()
    keywords = ('pallet', 'jack', 'warehouse', 'lifting', 'truck', 'handling')

    def build(self) -> None:
        # Horizontal centerlines (4,8)-(44,40); triangular steering grip.
        self.add_polyline("grip", (6,8), (22,8), (14,18), (6,8))
        self.add_line("shaft", (14,18), (14,26))
        self.add_polyline("housing-fork", (9,30), (9,26), (14,26), (17,26), (21,34), (38,34), (44,34))
        self.relate("connect", "grip", "shaft")
        self.relate("connect", "shaft", "housing-fork")
        # Repeated circular wheels share a radius and baseline.
        for n, x in enumerate((9,)):
            self.add_arc(f"wheel-{n}-right", (x,30), (x,40), radius_x=5)
            self.add_arc(f"wheel-{n}-left", (x,40), (x,30), radius_x=5)
            self.add_contour(f"wheel-{n}", f"wheel-{n}-right", f"wheel-{n}-left", closed=True)
        self.relate("connect", "wheel-0", "housing-fork")
        self.add_arc("roller-r", (38,34), (38,40), radius_x=3)
        self.add_arc("roller-l", (38,40), (38,34), radius_x=3)
        self.add_contour("roller", "roller-r", "roller-l", closed=True)
        self.relate("connect", "roller", "housing-fork")
