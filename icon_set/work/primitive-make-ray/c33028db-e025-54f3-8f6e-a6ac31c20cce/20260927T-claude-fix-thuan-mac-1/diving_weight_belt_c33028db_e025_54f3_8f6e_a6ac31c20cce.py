"""Diving weight belt: a belt strap with a raised central buckle and two lead
weights hanging from it.

Revision (disapproved, reason not recorded): the rejected drawing split the belt
into two closed boxes with no buckle and hung two small squares on stubs, so it
read as a sign on posts; the original is one strap running through a raised
buckle that stands proud of it, with two weight blocks hanging below. The strap,
the proud buckle and hanging weights are restored.

Symbol plan: mirror axis x=24. Strap band y 12-22 from the belt ends x=4/44 into
the buckle. Buckle: rounded rectangle (15,8)-(33,22), radius-3 top corners,
standing 4 above the strap; its base is the strap's lower edge. Weights: rounded
blocks (4,30)-(16,40) and (32,30)-(44,40), radius-3 corners, each hung from the
strap's lower edge by a strap at x=10 / x=38.
Omissions: the buckle's two tongue slots (a line inside the 14-high buckle cannot
keep 8 from its top and bottom).
Lucide construction: rounded-rectangle corners.
Keyshape HRECT_L: centerline x 4..44 (belt ends, weights), y 8 (buckle) .. 40.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "c33028db-e025-54f3-8f6e-a6ac31c20cce"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__diving-weight-belt/20260926T182653Z-thuan-mac-1/reference/diving weight belt_c33028db-e025-54f3-8f6e-a6ac31c20cce.svg"
AUTHOR = "claude-opus-5-5"

STRAP_TOP, STRAP_BOTTOM = 12, 22
BUCKLE_L, BUCKLE_R, BUCKLE_TOP = 15, 33, 8


class DivingWeightBelt(Solo48):
    icon_id = "diving-weight-belt"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports/diving"
    aliases = ("weight-belt", "dive-belt")
    keywords = ("diving", "weight", "belt", "buckle", "lead", "scuba", "ballast")

    def block(self, name, x0, y0, x1, y1, r, hang_x):
        self.add_line(f"{name}-top-a", (x0 + r, y0), (hang_x, y0))
        self.add_line(f"{name}-top-b", (hang_x, y0), (x1 - r, y0))
        self.add_arc(f"{name}-tr", (x1 - r, y0), (x1, y0 + r), radius_x=r)
        self.add_line(f"{name}-right", (x1, y0 + r), (x1, y1 - r))
        self.add_arc(f"{name}-br", (x1, y1 - r), (x1 - r, y1), radius_x=r)
        self.add_line(f"{name}-bottom", (x1 - r, y1), (x0 + r, y1))
        self.add_arc(f"{name}-bl", (x0 + r, y1), (x0, y1 - r), radius_x=r)
        self.add_line(f"{name}-left", (x0, y1 - r), (x0, y0 + r))
        self.add_arc(f"{name}-tl", (x0, y0 + r), (x0 + r, y0), radius_x=r)
        self.add_contour(name, f"{name}-top-a", f"{name}-top-b", f"{name}-tr", f"{name}-right", f"{name}-br",
                         f"{name}-bottom", f"{name}-bl", f"{name}-left", f"{name}-tl", closed=True)

    def build(self) -> None:
        # Belt outline: strap ends, strap edges and the proud buckle in one closed contour.
        pts_top = [(4, STRAP_TOP), (BUCKLE_L, STRAP_TOP)]
        self.add_line("strap-end-left", (4, STRAP_BOTTOM), (4, STRAP_TOP))
        self.add_line("strap-top-left", (4, STRAP_TOP), (BUCKLE_L, STRAP_TOP))
        self.add_line("buckle-left", (BUCKLE_L, STRAP_TOP), (BUCKLE_L, BUCKLE_TOP + 3))
        self.add_arc("buckle-tl", (BUCKLE_L, BUCKLE_TOP + 3), (BUCKLE_L + 3, BUCKLE_TOP), radius_x=3)
        self.add_line("buckle-top", (BUCKLE_L + 3, BUCKLE_TOP), (BUCKLE_R - 3, BUCKLE_TOP))
        self.add_arc("buckle-tr", (BUCKLE_R - 3, BUCKLE_TOP), (BUCKLE_R, BUCKLE_TOP + 3), radius_x=3)
        self.add_line("buckle-right", (BUCKLE_R, BUCKLE_TOP + 3), (BUCKLE_R, STRAP_TOP))
        self.add_line("strap-top-right", (BUCKLE_R, STRAP_TOP), (44, STRAP_TOP))
        self.add_line("strap-end-right", (44, STRAP_TOP), (44, STRAP_BOTTOM))
        self.add_line("strap-bottom-r1", (44, STRAP_BOTTOM), (38, STRAP_BOTTOM))
        self.add_line("strap-bottom-r2", (38, STRAP_BOTTOM), (10, STRAP_BOTTOM))
        self.add_line("strap-bottom-l", (10, STRAP_BOTTOM), (4, STRAP_BOTTOM))
        self.add_contour("belt", "strap-end-left", "strap-top-left", "buckle-left", "buckle-tl", "buckle-top",
                         "buckle-tr", "buckle-right", "strap-top-right", "strap-end-right", "strap-bottom-r1",
                         "strap-bottom-r2", "strap-bottom-l", closed=True)
        self.add_line("buckle-side-left", (BUCKLE_L, STRAP_TOP), (BUCKLE_L, STRAP_BOTTOM))
        self.add_line("buckle-side-right", (BUCKLE_R, STRAP_TOP), (BUCKLE_R, STRAP_BOTTOM))
        self.relate("connect", "belt", "buckle-side-left")
        self.relate("connect", "belt", "buckle-side-right")

        for name, x0, hang in (("weight-left", 4, 10), ("weight-right", 32, 38)):
            self.block(name, x0, 30, x0 + 12, 40, 3, hang)
            self.add_line(f"{name}-hanger", (hang, STRAP_BOTTOM), (hang, 30))
            self.relate("connect", f"{name}-hanger", "belt")
            self.relate("connect", f"{name}-hanger", name)
