"""Code version control and branching: a commit graph - a main line of commits
with a branch curving off to a second commit.
Review (meaning): the earlier broken strokes did not read as anything. The
reference is a git graph (commits on a vertical line, a branch curve to
another commit); this revision draws it with the canonical Lucide
`git-branch` construction at 2x, which lands exactly on the SQUARE box.
Keyshape SQUARE (6,6)-(42,42).
Symbol plan: two r6 commit rings, the main line ending on the lower ring's top
node, the r18 branch arc running from the upper ring's bottom node to the
lower ring's right node, so every join is a shared cardinal node.
Lucide construction: git-branch (line 6,3-6,15; circles r3 at 18,6 and 6,18;
arc r9) scaled by 2.
Omissions: the reference's third commit, arrow and code document; three commits
on a 36-unit line leave no 8-unit gaps, and the branch graph alone carries
"version control and branching".
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "e3ffb6e8-3bc2-43d5-82fe-ae251b7b7f41"
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__code-version-control-and-branching/20260926T125430Z-thuan-mac/reference/amazon web service code commit_e3ffb6e8-3bc2-43d5-82fe-ae251b7b7f41.svg'
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

class CodeVersionControlAndBranching(_Shapes, Solo48):
    icon_id = 'code-version-control-and-branching'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology/code'
    categories = ('technology',)
    aliases = ('git branch', 'code commit', 'amazon web service code commit')
    keywords = ('git', 'branch', 'commit', 'version', 'control', 'code', 'repository', 'merge')

    def build(self):
        self.circle('commit-branch', 36, 12, 6)
        self.circle('commit-main', 12, 36, 6)
        self.add_line('main-line', (12, 6), (12, 30))
        self.add_arc('branch', (36, 18), (18, 36), radius_x=18)
        self.relate('connect', 'main-line', 'commit-main')
        self.relate('connect', 'branch', 'commit-branch')
        self.relate('connect', 'branch', 'commit-main')
