"""Long-handled broom beside an upright dustpan.

Plan: the broom leans on a 1:2 frame, u=(2,-1) across and v=(1,2) along
the handle. Handle from (6,6) to the dome apex A=(11,16); the dome is a
half circle of radius 4|v| about B=A+4v drawn as two quarter cubics onto
the base line P1-B-P2 (B-+4u); three bristles leave P1, B and P2 along 3v,
8.9 apart. Dustpan: vertical handle x=42 full height with a right-triangle
pan (legs 14) at the bottom. Keyshape SQUARE: handle x=6,y=6; pan x=42,y=42.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "9218d7b4-2468-48fa-baee-9384041eb713"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__long-handled-broom-and-dustpan/20260927T164623Z-thuan-mac-1/reference/broom dustpan_9218d7b4-2468-48fa-baee-9384041eb713.svg"
AUTHOR = "claude-opus-5-5"


class LongHandledBroomAndDustpan(Solo48):
    icon_id = "long-handled-broom-and-dustpan"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('broom dustpan', 'sweeping set')
    keywords = ('broom', 'dustpan', 'sweep', 'cleaning', 'housework', 'chores')

    def path(self, name, start, steps, closed=False):
        here, members = start, []
        for j, (kind, end, *args) in enumerate(steps):
            member = f"{name}-{j}"
            if kind == "L":
                self.add_line(member, here, end)
            elif kind == "A":
                self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2],
                             large_arc=args[3] if len(args) > 3 else False)
            else:
                self.add_bezier(member, here, (args[0], args[1], end))
            here = end
            members.append(member)
        self.add_contour(name, *members, closed=closed)

    def build(self) -> None:

        k = 0.5523
        a, b = (11, 16), (15, 24)
        p1, p2 = (7, 28), (23, 20)
        self.add_line("handle", (6, 6), a)
        self.add_bezier("dome-a", p1, ((p1[0] - 4 * k, p1[1] - 8 * k), (a[0] - 8 * k, a[1] + 4 * k), a))
        self.add_bezier("dome-b", a, ((a[0] + 8 * k, a[1] - 4 * k), (p2[0] - 4 * k, p2[1] - 8 * k), p2))
        self.add_line("base-a", p2, b)
        self.add_line("base-b", b, p1)
        self.add_contour("head", "dome-a", "dome-b", "base-a", "base-b", closed=True)
        self.relate("connect", "handle", "head")
        for name, root in (("l", p1), ("m", b), ("r", p2)):
            self.add_line(f"bristle-{name}", root, (root[0] + 3, root[1] + 6))
            self.relate("connect", "head", f"bristle-{name}")
        self.add_line("pan-handle", (42, 6), (42, 28))
        self.path("pan", (42, 28), [("L", (42, 42)), ("L", (28, 42)), ("L", (42, 28))], closed=True)
        self.relate("connect", "pan-handle", "pan")
