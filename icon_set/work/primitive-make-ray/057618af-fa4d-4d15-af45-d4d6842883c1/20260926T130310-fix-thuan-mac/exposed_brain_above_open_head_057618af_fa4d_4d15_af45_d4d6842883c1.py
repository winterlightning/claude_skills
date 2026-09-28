"""Exposed brain above an open head: a profile head whose skull is cut flat,
with the lobed brain sitting on the cut.
Review (meaning): the frontal cup-and-neck read as an ice cream / torch. A head
in profile (forehead, nose, chin, jaw and neck facing right) makes "head"
unmistakable; the brain keeps the reference's lobed cloud over a straight cut
line, 
Keyshape SQUARE (6,6)-(42,42).
Symbol plan: brain = five clockwise arcs on integer nodes (cardinal quarters at
the left/right extremes, an r10 crown whose apex is the top extreme) closed by
the cut line; the head hangs from two nodes of the cut line.
Lucide construction: brain (lobed outline) and the common "open mind" profile;
human_ref consulted for head/neck proportion.
Omissions: ears and inner brain folds (no 8-unit room inside a 14-tall brain).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '057618af-fa4d-4d15-af45-d4d6842883c1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__exposed-brain-above-open-head/20260926T125430Z-thuan-mac/reference/brain open skill_057618af-fa4d-4d15-af45-d4d6842883c1.svg'
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

class ExposedBrainAboveOpenHead(_Shapes, Solo48):
    icon_id = 'exposed-brain-above-open-head'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'body/brain'
    categories = ('body', 'education')
    aliases = ('open mind', 'brain skill')
    keywords = ('brain', 'open', 'head', 'skill', 'mind', 'thinking', 'intelligence')

    def build(self):
        cut = 20
        a = self.add_arc
        a('lobe-1', (6, cut), (12, 14), radius_x=6)
        a('lobe-2', (12, 14), (16, 10), radius_x=4)
        a('lobe-3', (16, 10), (32, 10), radius_x=10)
        a('lobe-4', (32, 10), (36, 14), radius_x=4)
        a('lobe-5', (36, 14), (42, cut), radius_x=6)
        self.add_line('cut-1', (42, cut), (34, cut))
        self.add_line('cut-2', (34, cut), (10, cut))
        self.add_line('cut-4', (10, cut), (6, cut))
        self.add_contour('brain', 'lobe-1', 'lobe-2', 'lobe-3', 'lobe-4', 'lobe-5',
                         'cut-1', 'cut-2', 'cut-4', closed=True)
        # head in profile, facing right
        self.add_bezier('back', (10, cut), ((9, 27), (10, 33), (16, 36)))
        self.add_line('neck-back', (16, 36), (16, 42))
        self.add_contour('head-back', 'back', 'neck-back')
        self.add_bezier('forehead', (34, cut), ((35, 24), (36, 26), (40, 30)))
        self.add_line('nose-under', (40, 30), (36, 32))
        self.add_bezier('chin', (36, 32), ((37, 35), (35, 38), (31, 38)))
        self.add_line('jaw', (31, 38), (28, 38))
        self.add_line('neck-front', (28, 38), (28, 42))
        self.add_contour('face', 'forehead', 'nose-under', 'chin', 'jaw', 'neck-front')
        self.relate('connect', 'brain', 'head-back')
        self.relate('connect', 'brain', 'face')
