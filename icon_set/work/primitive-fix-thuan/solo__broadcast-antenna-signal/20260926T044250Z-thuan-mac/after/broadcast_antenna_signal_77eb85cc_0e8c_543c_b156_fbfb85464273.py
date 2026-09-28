"""A broadcast antenna: a mast topped by a small ring, with two pairs of signal arcs on either side.

Symbol plan: symmetric about x=24. The head is a ring (r3, the approved 6-diameter
circle) on top of a vertical mast (shared endpoint at the ring's bottom). The outer
arcs are r20 about the head centre (3-4-5 endpoints 12 above and below it), reaching the
envelope sides. The inner arcs are r12 through (33, 20+-7): their centre sits just off
the head, which keeps them 8+ from both the head and the outer arcs.
Lucide construction: 'radio' / 'antenna' - mast with a head and paired signal arcs.
Keyshape HRECT_L: centerline x 4..44 (outer arcs), y 8..40 (outer arc tops, mast foot).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "77eb85cc-0e8c-543c-b156-fbfb85464273"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__broadcast-antenna-signal/20260926T044250Z-thuan-mac/reference/wifi signal_77eb85cc-0e8c-543c-b156-fbfb85464273.svg"
AUTHOR = "claude-opus-5-5"


class BroadcastAntennaSignal(Solo48):
    icon_id = "broadcast-antenna-signal"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "technology/signal"
    aliases = ("wifi signal", "radio antenna", "hotspot", "broadcast")
    keywords = ("antenna", "broadcast", "signal", "wifi", "radio", "hotspot", "wireless", "transmit")

    def build(self) -> None:
        ax, cy, hr = 24, 20, 3
        pts = [(ax - hr, cy), (ax, cy - hr), (ax + hr, cy), (ax, cy + hr)]
        names = ("head-nw", "head-ne", "head-se", "head-sw")
        for i, n in enumerate(names):
            self.add_arc(n, pts[i], pts[(i + 1) % 4], radius_x=hr)
        self.add_contour("head", *names, closed=True)
        self.add_line("mast", (ax, cy + hr), (ax, 40))
        self.relate("connect", "head", "mast")
        for side, sx in (("r", 1), ("l", -1)):
            self.add_arc(f"inner-{side}", (ax + sx * 9, cy - 7), (ax + sx * 9, cy + 7), radius_x=12,
                         sweep=(sx == 1))
            self.add_arc(f"outer-{side}", (ax + sx * 16, cy - 12), (ax + sx * 16, cy + 12), radius_x=20,
                         sweep=(sx == 1))
