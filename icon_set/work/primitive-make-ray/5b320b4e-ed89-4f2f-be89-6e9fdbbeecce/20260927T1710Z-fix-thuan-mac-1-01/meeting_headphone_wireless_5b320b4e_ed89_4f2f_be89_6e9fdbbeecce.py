from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "5b320b4e-ed89-4f2f-be89-6e9fdbbeecce"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__meeting-headphone-wireless/20260927T164821Z-thuan-mac-1/reference/meeting headphone wireless_5b320b4e-ed89-4f2f-be89-6e9fdbbeecce.svg"
AUTHOR = "claude-fable-5-1"


def _path(icon, name, start, steps, closed=False):
    """steps: ('L', end) | ('A', end, r[, ry], sweep[, large]) | ('C', c1, c2, end)"""
    here, members = start, []
    for i, st in enumerate(steps):
        m = f"{name}-{i + 1}"
        if st[0] == "L":
            icon.add_line(m, here, st[1]); here = st[1]
        elif st[0] == "A":
            end, r = st[1], st[2]
            rest = list(st[3:])
            ry = r
            if rest and not isinstance(rest[0], bool):
                ry = rest.pop(0)
            sweep = rest[0] if rest else True
            large = rest[1] if len(rest) > 1 else False
            icon.add_arc(m, here, end, radius_x=r, radius_y=ry, large_arc=large, sweep=sweep); here = end
        else:
            icon.add_bezier(m, here, (st[1], st[2], st[3])); here = st[3]
        members.append(m)
    icon.add_contour(name, *members, closed=closed)


def _circle(icon, name, cx, cy, r):
    _path(icon, name, (cx, cy - r), [("A", (cx + r, cy), r, True), ("A", (cx, cy + r), r, True),
                                      ("A", (cx - r, cy), r, True), ("A", (cx, cy - r), r, True)], True)


def _smooth(icon, name, pts, closed=True, t=1/3):
    """Catmull-Rom cubics through integer knots."""
    n = len(pts); segs = []
    rng = range(n) if closed else range(n - 1)
    for i in rng:
        p0 = pts[(i - 1) % n] if (closed or i > 0) else pts[i]
        p1 = pts[i]; p2 = pts[(i + 1) % n]
        p3 = pts[(i + 2) % n] if (closed or i + 2 < n) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) * t / 2, p1[1] + (p2[1] - p0[1]) * t / 2)
        c2 = (p2[0] - (p3[0] - p1[0]) * t / 2, p2[1] - (p3[1] - p1[1]) * t / 2)
        segs.append(("C", c1, c2, p2))
    _path(icon, name, pts[0], segs, closed)


def _herm(icon, name, knots, closed=True, k=1.0):
    """knots: [(point, tangent_dir)]; controls at chord/3*k along the unit tangents."""
    import math
    def unit(v):
        n = math.hypot(*v)
        return (v[0] / n, v[1] / n)
    segs = []
    n = len(knots)
    for i in range(n if closed else n - 1):
        (p1, t1), (p2, t2) = knots[i], knots[(i + 1) % n]
        L = math.hypot(p2[0] - p1[0], p2[1] - p1[1]) / 3 * k
        u1, u2 = unit(t1), unit(t2)
        segs.append(("C", (p1[0] + u1[0] * L, p1[1] + u1[1] * L), (p2[0] - u2[0] * L, p2[1] - u2[1] * L), p2))
    _path(icon, name, knots[0][0], segs, closed)



class MeetingHeadphoneWireless(Solo48):
    """Wireless meeting headset: a signal arc with its source dot above a headphone band with
    two ear cups, and a boom microphone curving from the left cup to the chin position.

    Plan: VRECT_M (10..38 x 4..44). Signal = r9 arc about (24,13) (top at 4) + dot at its centre.
    Band = r14 semicircle about (24,36) (top 22, 9 below the dot) ending on the cups' top points.
    Cups = r2 rings (paint as solid 8-wide discs) about (10,38)/(38,38).
    Boom leaves the left cup's bottom (10,40) and curves to the mouth position (22,44).
    Head omitted: band + cups + boom already read as a meeting headset at 48.
    """
    icon_id = "meeting-headphone-wireless"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("wireless headset", "meeting headset")
    keywords = ("headphone", "headset", "wireless", "meeting", "microphone", "call", "bluetooth")

    def build(self) -> None:
        self.add_arc("signal", (15, 13), (33, 13), radius_x=9, sweep=True)
        self.add_dot("source", (24, 13))
        self.add_arc("band", (10, 36), (38, 36), radius_x=14, sweep=True)
        self.add_line("leg-left", (10, 36), (10, 38))
        self.add_line("leg-right", (38, 36), (38, 38))
        _circle(self, "cup-left", 12, 38, 2)
        _circle(self, "cup-right", 36, 38, 2)
        self.add_bezier("boom", (12, 40), ((12, 44), (16, 44), (22, 44)))
        self.relate("connect", "band", "leg-left")
        self.relate("connect", "band", "leg-right")
        self.relate("connect", "leg-left", "cup-left")
        self.relate("connect", "leg-right", "cup-right")
        self.relate("connect", "boom", "cup-left")
