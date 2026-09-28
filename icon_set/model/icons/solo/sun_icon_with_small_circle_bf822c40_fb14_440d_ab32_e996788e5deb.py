"""A ray-ring sun with a detached small circle at upper right."""

from ...keyshapes import Keyshape
from ._base import Solo48


SOURCE_ICON_ID = "bf822c40-fb14-440d-ab32-e996788e5deb"
SOURCE_PATH = "pictographic-primitives/_uncategorized_01/air purifier 6_bf822c40-fb14-440d-ab32-e996788e5deb.svg"
AUTHOR = "gpt-5"


class SunIconWithSmallCircle(Solo48):
    icon_id = "sun-icon-with-small-circle"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("sun-with-particle", "ray-circle-with-dot")
    keywords = ("sun", "rays", "circle", "particle", "status")

    def build(self) -> None:
        # Plan: a circular sun definition owns eight radial members. Every ray
        # attaches at an exact 5-12-13 point, keeping adjacent ray roots more
        # than eight units apart. A separate small circle preserves the source's
        # unresolved mark.
        cx, cy, radius = 17, 27, 13
        left, right = (cx - radius, cy), (cx + radius, cy)
        self.add_arc("sun-top", left, right, radius_x=radius)
        self.add_arc("sun-bottom", right, left, radius_x=radius)
        self.add_contour("sun-center", "sun-top", "sun-bottom", closed=True)

        rays = {
            "upper-left": ((12, 15), (10, 10)),
            "upper-right": ((22, 15), (24, 10)),
            "right-upper": ((29, 22), (34, 20)),
            "right-lower": ((29, 32), (34, 34)),
            "lower-right": ((22, 39), (24, 40)),
            "lower-left": ((12, 39), (10, 40)),
            "left-lower": ((5, 32), (4, 34)),
            "left-upper": ((5, 22), (4, 20)),
        }
        for name, (start, end) in rays.items():
            element = f"ray-{name}"
            self.add_line(element, start, end)
            self.relate("connect", "sun-center", element)

        dot_cx, dot_cy, dot_radius = 41, 11, 3
        self.add_arc(
            "small-circle-top",
            (dot_cx - dot_radius, dot_cy),
            (dot_cx + dot_radius, dot_cy),
            radius_x=dot_radius,
        )
        self.add_arc(
            "small-circle-bottom",
            (dot_cx + dot_radius, dot_cy),
            (dot_cx - dot_radius, dot_cy),
            radius_x=dot_radius,
        )
        self.add_contour(
            "small-circle",
            "small-circle-top",
            "small-circle-bottom",
            closed=True,
        )
