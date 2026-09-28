"""Airship (blimp) in flight, side view: an elliptical envelope, two triangular
tail fins at the back and a gondola slung under the belly.
Review (meaning): the earlier flat-topped pill with a chevron tail read as a
megaphone. This revision follows the reference: a true 3:2 ellipse
(rx15, ry10), separate upper and lower fin triangles, and a tapered gondola.
Keyshape HRECT_L (4,8)-(44,40): the swept fins need the extra height.
Symbol plan: the ellipse is split only at integer points of the 3-4-5 family
(centre (29,22) +/-(9,8), +(-15,0)) so fins and gondola share real nodes;
fins sweep back to tips at (4,8)/(4,36), mirrored about y=22;
fins mirror about y=20.
Lucide construction: no blimp original; ellipse-and-fin construction follows
Lucide plane/rocket fin joins.
Omissions: window details on the gondola.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '94ee19fa-6c64-4340-9c2b-4d23bc7e3842'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__flying-blimp-airship-batch-033/20260926T125430Z-thuan-mac/reference/airship_94ee19fa-6c64-4340-9c2b-4d23bc7e3842.svg'
AUTHOR = 'claude-opus-5-5'


class _Shapes:
    def circle(self, n, x, y, r):
        pts = [(x - r, y), (x, y - r), (x + r, y), (x, y + r), (x - r, y)]
        for i, (a, b) in enumerate(zip(pts, pts[1:])):
            self.add_arc(f"{n}-{i}", a, b, radius_x=r)
        self.add_contour(n, *(f"{n}-{i}" for i in range(4)), closed=True)

    def lines(self, n, *pts, closed=False):
        """Plain add_line segments grouped in one contour (members joinable by relate)."""
        seq = list(pts) + ([pts[0]] if closed else [])
        ids = []
        for i, (a, b) in enumerate(zip(seq, seq[1:])):
            self.add_line(f"{n}-{i}", a, b)
            ids.append(f"{n}-{i}")
        self.add_contour(n, *ids, closed=closed)
        return ids

class FlyingBlimpAirship(_Shapes, Solo48):
    icon_id = 'flying-blimp-airship-batch-033'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transport/air'
    categories = ('transport',)
    aliases = ('airship', 'blimp', 'zeppelin', 'dirigible')
    keywords = ('airship', 'blimp', 'zeppelin', 'flying', 'aircraft', 'balloon')

    def build(self):
        cx, cy, rx, ry = 29, 22, 15, 10
        a = lambda n, s, e: self.add_arc(n, s, e, radius_x=rx, radius_y=ry)
        ul, nose_t, ll = (cx - 9, cy - 8), (cx, cy - ry), (cx - 9, cy + 8)
        back, nose, lr = (cx - rx, cy), (cx + rx, cy), (cx + 9, cy + 8)
        a('env-1', back, ul)
        a('env-2', ul, nose_t)
        a('env-3', nose_t, nose)
        a('env-4', nose, lr)
        a('env-5', lr, ll)
        a('env-6', ll, back)
        self.add_contour('envelope', *(f'env-{i}' for i in range(1, 7)), closed=True)
        self.lines('fin-top', ul, (4, cy - 14), back)
        self.lines('fin-bottom', ll, (4, cy + 14), back)
        self.lines('gondola', ll, (26, 40), (32, 40), lr)
        for part in ('fin-top', 'fin-bottom', 'gondola'):
            self.relate('connect', 'envelope', part)
        self.relate('connect', 'fin-top', 'fin-bottom')
        