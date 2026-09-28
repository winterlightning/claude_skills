"""Closed lips with a central seam: a mouth drawn as full upper and lower lips
meeting at pointed corners, the upper lip with a cupid's-bow dip.
Review (meaning): the earlier oval with a straight bar read as a burger or an
eye. This revision uses the reference's lip silhouette: pointed mouth corners
on the horizontal axis, two rounded upper-lip peaks with a central dip, a
fuller lower lip, and a gently curving seam joining the corners.
Keyshape HRECT_M (4,10)-(44,38).
Symbol plan: every curve mirrors about x=24; upper lip = four cubics
(corner-peak-dip-peak-corner), lower lip = two cubics, seam = two cubics, all
sharing the corner nodes so converging edges end on a common node.
Lucide construction: no lips original; smooth-cubic joins follow Lucide
heart/mouth curves.
Omissions: none.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd077ca8e-11b1-40d1-a612-b89115575b84'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__closed-lips-with-central-seam/20260926T125430Z-thuan-mac/reference/lip_d077ca8e-11b1-40d1-a612-b89115575b84.svg'
AUTHOR = "claude-opus-5-5"


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

class ClosedLipsWithCentralSeam(_Shapes, Solo48):
    icon_id = 'closed-lips-with-central-seam'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'body/face'
    categories = ('body',)
    aliases = ('lip', 'lips', 'mouth')
    keywords = ('lip', 'lips', 'mouth', 'kiss', 'closed', 'beauty')

    def build(self):
        L, R, y = (4, 24), (44, 24), 24
        b = self.add_bezier
        b('upper-1', L, ((8, 19), (11, 10), (16, 10)))
        b('upper-2', (16, 10), ((20, 10), (22, 14), (24, 15)))
        b('upper-3', (24, 15), ((26, 14), (28, 10), (32, 10)))
        b('upper-4', (32, 10), ((37, 10), (40, 19), R))
        b('lower-1', R, ((38, 32), (31, 38), (24, 38)))
        b('lower-2', (24, 38), ((17, 38), (10, 32), L))
        self.add_contour('lips', 'upper-1', 'upper-2', 'upper-3', 'upper-4',
                         'lower-1', 'lower-2', closed=True)
        b('seam-1', L, ((12, 25), (18, 27), (24, 26)))
        b('seam-2', (24, 26), ((30, 27), (36, 25), R))
        self.add_contour('seam', 'seam-1', 'seam-2')
        self.relate('connect', 'lips', 'seam')
