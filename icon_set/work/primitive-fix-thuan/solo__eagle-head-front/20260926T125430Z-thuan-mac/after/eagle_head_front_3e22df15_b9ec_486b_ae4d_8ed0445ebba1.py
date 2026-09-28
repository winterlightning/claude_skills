"""Eagle head, front view: a domed head with scalloped neck feathers, fierce
slanted brows and a hooked beak pointing down at the centre.
Review (meaning): the earlier head had a bent-line beak joined to the brows
that read as a symbol, not a bird. This revision separates the parts the
reference uses: a squared dome (r10 shoulders so the brows can sit inside),
two angry brows slanting down to the centre, and a proper closed beak - a
rounded top narrowing to a hooked tip that reaches the bottom extreme.
Keyshape SQUARE (6,6)-(42,42).
Lucide construction: bird (closed beak drop) and angry-face brows; mirrored
about x=24.
Omissions: the reference's third central feather scallop (the beak takes its
place).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3e22df15-b9ec-486b-ae4d-8ed0445ebba1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__eagle-head-front/20260926T125430Z-thuan-mac/reference/wild bird eagle head_3e22df15-b9ec-486b-ae4d-8ed0445ebba1.svg'
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

class EagleHeadFront(_Shapes, Solo48):
    icon_id = 'eagle-head-front'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals/birds'
    categories = ('animals',)
    aliases = ('wild bird eagle head',)
    keywords = ('eagle', 'head', 'bird', 'wild', 'hawk', 'raptor', 'beak')

    def build(self):
        a = self.add_arc
        # head: open-bottom dome whose lower edges run into the beak corners
        self.add_line('chin-l', (16, 36), (6, 36))
        self.add_line('wall-l', (6, 36), (6, 16))
        a('shoulder-l', (6, 16), (16, 6), radius_x=10)
        self.add_line('crown', (16, 6), (32, 6))
        a('shoulder-r', (32, 6), (42, 16), radius_x=10)
        self.add_line('wall-r', (42, 16), (42, 36))
        self.add_line('chin-r', (42, 36), (32, 36))
        self.add_contour('head', 'chin-l', 'wall-l', 'shoulder-l', 'crown',
                         'shoulder-r', 'wall-r', 'chin-r')
        # brows
        self.add_line('brow-l', (15, 15), (20, 19))
        self.add_line('brow-r', (28, 19), (33, 15))
        # beak: broad rounded top between the corners, hooked point below
        a('beak-top', (16, 36), (32, 36), radius_x=8)
        self.add_bezier('beak-r', (32, 36), ((31, 39), (27, 40), (24, 42)))
        self.add_bezier('beak-l', (24, 42), ((21, 40), (17, 39), (16, 36)))
        self.add_contour('beak', 'beak-top', 'beak-r', 'beak-l', closed=True)
        self.relate('connect', 'head', 'beak')
