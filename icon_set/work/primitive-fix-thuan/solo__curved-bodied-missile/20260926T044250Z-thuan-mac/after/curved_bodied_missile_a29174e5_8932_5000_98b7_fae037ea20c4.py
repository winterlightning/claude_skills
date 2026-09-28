"""A bomb rocket / missile flying up to the right: a long body with a pointed curved nose,
two swept tail fins and an exhaust streak.

Symbol plan: mirror-symmetric about its axis x+y=48 (reflection (x,y) -> (48-y, 48-x)).
The body edges are straight, 14 apart (offsets +-(5,5) from the axis), from the flat
tail T=(18,30) to the shoulders; the nose is two cubics meeting at the point (42,6) with
vertical and horizontal tangents there; a seam across the shoulders marks the nose cone. Each fin is an open cubic swept back from the
body edge near the tail. One exhaust streak trails behind the tail, 9.9 clear of it.
Lucide construction: 'rocket' - diagonal body with a curved nose and swept fins.
Keyshape SQUARE: centerline x 6..42, y 6..42 (exhaust, nose).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "a29174e5-8932-5000-98b7-fae037ea20c4"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__curved-bodied-missile/20260926T044250Z-thuan-mac/reference/bomb rocket_a29174e5-8932-5000-98b7-fae037ea20c4.svg"
AUTHOR = "claude-opus-5-5"


def _m(p):
    return (48 - p[1], 48 - p[0])


class CurvedBodiedMissile(Solo48):
    icon_id = "curved-bodied-missile"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "weapons/rockets"
    aliases = ("bomb-rocket", "missile", "rocket")
    keywords = ("missile", "rocket", "bomb", "launch", "weapon", "projectile", "space", "fly")

    def build(self) -> None:
        tl, tr = (13, 25), (23, 35)        # tail corners
        sl, sr = (25, 13), (35, 23)        # shoulders
        N = (42, 6)
        self.add_line("tail", tl, tr)
        self.add_line("side-lower", tr, sr)
        self.add_bezier("nose-lower", sr, ((39, 19), (42, 12), N))
        self.add_bezier("nose-upper", N, ((36, 6), (29, 9), sl))
        self.add_line("side-upper", sl, tl)
        self.add_contour("body", "tail", "side-lower", "nose-lower", "nose-upper", "side-upper", closed=True)
        self.add_line("nose-seam", sl, sr)
        self.relate("connect", "body", "nose-seam")
        f0, fc1, fc2, ft = (16, 22), (13, 18), (9, 17), (6, 20)
        self.add_bezier("fin-upper", f0, (fc1, fc2, ft))
        self.add_bezier("fin-lower", _m(f0), (_m(fc1), _m(fc2), _m(ft)))
        self.relate("connect", "body", "fin-upper")
        self.relate("connect", "body", "fin-lower")
        self.add_line("exhaust", (12, 38), (9, 41))
