"""diagonal-chain-links-open (redraw of the new-pipeline traced SVG).

Plan: two identical open chain links on the 45-degree axis x+y=48 of a
SQUARE keyshape (centerline box (6,6)-(42,42)); the lower link is the upper
one rotated 180 degrees about (24,24).
- each link is one open stadium: side walls on x+y=40 and x+y=56 (11.3
  apart), a closed outer cap whose extremes are the quarter arc (36,6)->(42,12)
  about Q=(36,12) r6, joined to the walls by short 45-degree cubics, so the
  upper link sets the top/right bounds and the lower one the left/bottom.
- the inner cap about P=(31,17) keeps only its two 45-degree shoulders: each
  wall curls in to a round tip at P+(-6,0) / P+(0,6), leaving the link open
  toward its partner, as in the generated image.
Metric issues:
- clearance e0/e1 4.61 (error): fixed. The inner caps sit 7.1 further apart
  along the axis than the trace, so the facing tips are 11.3 apart on
  centerlines (7.3 ink) instead of 4.6.
- stroke-width 2.77 -> 4 (info): handled, all spacing is budgeted at stroke 4.
Lucide `link` / `unlink` informed the 45-degree construction (two rounded
links on the diagonal, open ends facing each other).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "fe393bf8-c98b-5602-b212-fd9970a67853"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1157-diagonal-chain-links-open/"
    "diagonal-chain-links-open_raw.svg"
)
AUTHOR = "claude-opus-5-5"

Q = (36, 12)   # outer cap centre (upper link), r6 reaches y=6 and x=42
P = (31, 17)   # inner cap centre (upper link)
R = 6          # cap radius at the extremes
W = 4          # wall end offset from a cap centre along (+-1,+-1): x+y = 48 -+ 8
H = 1.6        # cubic handle on the 45-degree shoulders (~0.265 * R)
D = H / 2 ** 0.5


def _flip(pt):
    """Rotate 180 degrees about (24,24)."""
    return (48 - pt[0], 48 - pt[1])


class DiagonalChainLinksOpenRedraw(Solo48):
    icon_id = "diagonal-chain-links-open-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ("unlink", "broken link", "open chain")
    keywords = ("chain", "link", "unlink", "open", "disconnect", "url")

    def _link(self, name: str, f) -> None:
        qx, qy = Q
        px, py = P
        tip_a = (px - R, py)                 # left point of the inner cap
        wall_a0 = (px - W, py - W)           # on x+y=40
        wall_a1 = (qx - W, qy - W)
        top = (qx, qy - R)
        right = (qx + R, qy)
        wall_b1 = (qx + W, qy + W)           # on x+y=56
        wall_b0 = (px + W, py + W)
        tip_b = (px, py + R)                 # bottom point of the inner cap

        def pts(*p):
            return tuple(f(q) for q in p)

        self.add_bezier(f"{name}-curl-a", f(tip_a),
                        pts((tip_a[0], tip_a[1] - H), (wall_a0[0] - D, wall_a0[1] + D), wall_a0))
        self.add_line(f"{name}-wall-a", f(wall_a0), f(wall_a1))
        self.add_bezier(f"{name}-shoulder-a", f(wall_a1),
                        pts((wall_a1[0] + D, wall_a1[1] - D), (top[0] - H, top[1]), top))
        self.add_arc(f"{name}-cap", f(top), f(right), radius_x=R, sweep=True)
        self.add_bezier(f"{name}-shoulder-b", f(right),
                        pts((right[0], right[1] + H), (wall_b1[0] + D, wall_b1[1] - D), wall_b1))
        self.add_line(f"{name}-wall-b", f(wall_b1), f(wall_b0))
        self.add_bezier(f"{name}-curl-b", f(wall_b0),
                        pts((wall_b0[0] - D, wall_b0[1] + D), (tip_b[0] + H, tip_b[1]), tip_b))
        self.add_contour(name, *(f"{name}-{p}" for p in (
            "curl-a", "wall-a", "shoulder-a", "cap", "shoulder-b", "wall-b", "curl-b")))

    def build(self) -> None:
        self._link("upper-link", lambda p: p)
        self._link("lower-link", _flip)
