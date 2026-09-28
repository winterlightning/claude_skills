from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "2ac64939-46bf-4dd1-9f96-1b8c0d3a2cd5"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__limousine/20260927T164345Z-thuan-mac-1/reference/limo_2ac64939-46bf-4dd1-9f96-1b8c0d3a2cd5.svg"
AUTHOR = "claude-opus-5-5"


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


class Limousine(Solo48):
    """Side view of a long car: low body, a long cabin with sloped pillars and two side
    windows, and two round wheels set into the sill line at the ends of a long wheelbase.

    Plan (HRECT_M, x 4..44, y 10..38): roof y=10, window sill/beltline y=20, sill y=33 at
    the wheel centres; r5 wheels at x=9 and x=39 so the vertical end walls land ON each
    wheel's outer point (wall and wheel share a node). One centre pillar splits the glass
    into two large windows, as in the reference. All joins share endpoints.
    """
    icon_id = "limousine"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    categories = ("primitives", "transportation")
    aliases = ("limo", "sedan", "car")
    keywords = ("limousine", "car", "vehicle", "transport", "luxury", "chauffeur")

    def build(self) -> None:
        belt, sill, r = 20, 33, 5
        wl, wr = 9, 39
        _path(self, "body", (wl - r, sill), [
            ("L", (4, belt + 2)), ("A", (6, belt), 2, True),
            ("L", (8, belt)), ("L", (14, 10)), ("L", (34, 10)), ("L", (40, belt)),
            ("L", (42, belt)), ("A", (44, belt + 2), 2, True), ("L", (wr + r, sill))])
        self.add_line("window-sill", (8, belt), (40, belt))
        self.add_line("pillar", (24, 10), (24, belt))
        self.add_line("sill", (wl + r, sill), (wr - r, sill))
        _circle(self, "wheel-rear", wl, sill, r)
        _circle(self, "wheel-front", wr, sill, r)
        for a, b in (("window-sill", "body"), ("pillar", "body"), ("pillar", "window-sill"),
                     ("sill", "wheel-rear"), ("sill", "wheel-front"),
                     ("body", "wheel-rear"), ("body", "wheel-front")):
            self.relate("connect", a, b)
