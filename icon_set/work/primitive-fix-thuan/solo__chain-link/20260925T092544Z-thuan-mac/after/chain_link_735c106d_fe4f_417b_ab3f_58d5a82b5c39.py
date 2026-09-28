"""Chain link: two open chain links facing each other on the diagonal, joined
by a short straight link seen edge-on.

Symbol plan: one link definition rotated 180 degrees about the centre (24,24).
Each link is a radius-10 round cap whose 6-8-10 end points sit on the arm lines
x+y=34 and x+y=62 (19.8 apart), with straight arms running toward the centre;
the edge-on middle link lies on the axis x+y=48, 9.9 from both arm lines.
Keyshape SQUARE: upper cap top y=6 / right x=42, lower cap bottom y=42 /
left x=6.
Lucide construction: link-2 (two open brackets with a centre bar), rotated
to the reference's 45-degree diagonal.
Revision of the rejected drawing ("Bad stroke drawn"): the old drawing had
octagonal flat-cornered ends; here each link end is a true round cap.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "735c106d-fe4f-417b-ab3f-58d5a82b5c39"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__chain-link/20260925T092544Z-thuan-mac/reference/link slash_735c106d-fe4f-417b-ab3f-58d5a82b5c39.svg"
AUTHOR = "claude-opus-5-5"

CENTRE = 24
CAP = (32, 16)          # upper link cap centre on the axis x+y=48
CAP_R = 10
ARM = 6                 # arm length in diagonal steps
BAR = 3                 # half-length of the middle link in diagonal steps


def rot(point):
    """Rotate 180 degrees about the icon centre."""
    return (2 * CENTRE - point[0], 2 * CENTRE - point[1])


class ChainLink(Solo48):
    icon_id = "chain-link"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("link", "hyperlink")
    keywords = ("chain", "link", "url", "connect", "attach", "hyperlink")

    def build(self) -> None:
        cx, cy = CAP
        outer = (cx - 6, cy - 8)            # 6-8-10 points on the cap circle
        inner = (cx + 8, cy + 6)
        for name, f in (("upper", lambda p: p), ("lower", rot)):
            self.add_line(f"{name}-arm-outer", f((outer[0] - ARM, outer[1] + ARM)), f(outer))
            self.add_arc(f"{name}-cap", f(outer), f(inner), radius_x=CAP_R, sweep=True)
            self.add_line(f"{name}-arm-inner", f(inner), f((inner[0] - ARM, inner[1] + ARM)))
            self.add_contour(f"{name}-link", f"{name}-arm-outer", f"{name}-cap", f"{name}-arm-inner")
        self.add_line("middle-link", (CENTRE - BAR, CENTRE + BAR), (CENTRE + BAR, CENTRE - BAR))
