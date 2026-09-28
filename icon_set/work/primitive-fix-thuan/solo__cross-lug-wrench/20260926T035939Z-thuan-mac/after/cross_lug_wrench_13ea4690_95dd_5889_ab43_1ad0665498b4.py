"""A cross lug wrench (four-way wheel brace): four shafts from a round hub, each ending in
a socket.

Symbol plan: four-fold about (24,24). The two bars cross straight through the centre
(a separate hub circle cannot be both wide enough to keep opposite shafts 8 apart and
8 clear of the sockets), each bar running socket to socket. A socket is a cup 8
wide: its inner side is straight (the bar ends on its middle, 12 from the centre), its
sides run 4 outward and its outer end is a semicircle (r4) whose crown is on radius 20. The four sockets are one authored socket
turned by 90-degree steps, so their facing corners sit 8.5 apart.
Lucide construction: no lug-wrench glyph; straight shafts from a centre circle as in
'crosshair', sockets as small rounded rectangles.
Keyshape CIRCLE: socket crowns reach centerline radius 20 about (24,24).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "13ea4690-95dd-5889-ab43-1ad0665498b4"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__cross-lug-wrench/20260926T035939Z-thuan-mac/reference/car tool lug wrench_13ea4690-95dd-5889-ab43-1ad0665498b4.svg"
AUTHOR = "claude-opus-5-5"


def _turn(p, k):
    x, y = p[0] - 24, p[1] - 24
    for _ in range(k):
        x, y = -y, x
    return (x + 24, y + 24)


class CrossLugWrench(Solo48):
    icon_id = "cross-lug-wrench"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools/automotive"
    aliases = ("car-tool-lug-wrench", "lug-wrench", "wheel-brace", "cross-wrench")
    keywords = ("lug", "wrench", "wheel", "brace", "tire", "car", "tool", "nut", "spanner", "cross")

    def build(self) -> None:
        self.add_line("bar-horizontal", (12, 24), (36, 24))
        self.add_line("bar-vertical", (24, 12), (24, 36))
        self.relate("connect", "bar-horizontal", "bar-vertical")
        # right-hand socket, turned for the others; bars end on the socket inner sides
        pts = [(36, 24), (36, 20), (40, 20), (44, 24), (40, 28), (36, 28)]
        bars = {"right": "bar-horizontal", "down": "bar-vertical", "left": "bar-horizontal", "up": "bar-vertical"}
        for k, name in enumerate(("right", "down", "left", "up")):
            P = [_turn(p, k) for p in pts]
            self.add_line(f"socket-{name}-1", P[0], P[1])
            self.add_line(f"socket-{name}-2", P[1], P[2])
            self.add_arc(f"socket-{name}-3", P[2], P[3], radius_x=4, sweep=True)
            self.add_arc(f"socket-{name}-4", P[3], P[4], radius_x=4, sweep=True)
            self.add_line(f"socket-{name}-5", P[4], P[5])
            self.add_line(f"socket-{name}-6", P[5], P[0])
            self.add_contour(f"socket-{name}", *[f"socket-{name}-{i}" for i in range(1, 7)], closed=True)
            self.relate("connect", bars[name], f"socket-{name}")
