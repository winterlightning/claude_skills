"""Two tapered mesh router units beneath three nested radio arcs.

Symbol plan: two identical router instances mirrored about x=24;
three centered elliptical signal arcs form a width and height series.
Lucide router informed the low device bodies; wifi informed the arcs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "080c193b-0809-4e52-843c-538aec12a350"
SOURCE_PATH = "pictographic-primitives/_uncategorized_27/mesh wifi router_080c193b-0809-4e52-843c-538aec12a350.svg"
AUTHOR = "gpt-6"


class DualMeshWirelessRouters(Solo48):
    icon_id = "dual-mesh-wireless-routers"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("mesh wifi router", "twin routers")
    keywords = ("wireless", "signal", "network", "pair")

    def build(self) -> None:
        for name, left, right in (("left-router", 6, 20), ("right-router", 28, 42)):
            self.add_polyline(name, (left + 3, 33), (right - 3, 33), (right, 42), (left, 42), closed=True)
        for name, half_width, endpoint_y, rx, ry in (
            ("signal-outer", 14, 13, 14, 7),
            ("signal-middle", 8, 21, 8, 6),
            ("signal-inner", 1, 26, 1, 2),
        ):
            self.add_arc(name, (24 - half_width, endpoint_y), (24 + half_width, endpoint_y), radius_x=rx, radius_y=ry, sweep=True)
