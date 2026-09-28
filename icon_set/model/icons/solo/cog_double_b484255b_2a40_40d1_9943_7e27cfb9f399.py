"""Double cog: a large and a small gear side by side on a diagonal.
Review (meaning, "gears"): the earlier plus-shaped octagons read as frames, not
gears. This revision draws each gear the Lucide `cog` way - a large hub ring
with eight short radial teeth - so both read as gears at 48 px.
Keyshape SQUARE (6,6)-(42,42).
Symbol plan: one gear definition reused at two sizes. The hub is a ring of
eight arcs through the integer node (u,v) mirrored into all eight octants
(nodes about 45 degrees apart, full mirror symmetry); a short tooth leaves each
node radially. Big gear: centre (15,33), hub nodes (7,3), teeth to (9,4) so
the tips set the left/bottom extremes. Small gear: centre (35,13), hub (5,2),
teeth to (7,3) for the top/right extremes.
Lucide construction: cog (hub circle + radial tooth strokes).
Omissions: meshing; interlocked teeth would sit closer than the 8-unit
clearance, so the gears stand apart on the diagonal (about 10 units).
"""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID='b484255b-2a40-40d1-9943-7e27cfb9f399'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cog-double/20260926T125430Z-thuan-mac/reference/cog double_b484255b-2a40-40d1-9943-7e27cfb9f399.svg'
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

class CogDouble(_Shapes, Solo48):
    icon_id = 'cog-double'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/tools'
    categories = ('objects', 'technology')
    aliases = ('gears', 'cogs', 'settings')
    keywords = ('cog', 'double', 'gear', 'gears', 'settings', 'mechanism', 'machine')

    def gear(self, n, cx, cy, hub, arc_r, tips):
        """Hub ring through eight mirrored integer nodes, one short tooth per node."""
        ids = []
        for i, (a, b) in enumerate(zip(hub, hub[1:] + hub[:1])):
            self.add_arc(f'{n}-hub-{i}', (cx + a[0], cy + a[1]), (cx + b[0], cy + b[1]), radius_x=arc_r)
            ids.append(f'{n}-hub-{i}')
        self.add_contour(f'{n}-hub', *ids, closed=True)
        for i, ((a, b), (tx, ty)) in enumerate(zip(hub, tips)):
            self.add_line(f'{n}-tooth-{i}', (cx + a, cy + b), (cx + tx, cy + ty))
            self.relate('connect', f'{n}-hub', f'{n}-tooth-{i}')

    @staticmethod
    def octet(u, v):
        """(u,v) mirrored into all eight octants, in angular order."""
        return [(u, v), (v, u), (-v, u), (-u, v), (-u, -v), (-v, -u), (v, -u), (u, -v)]

    def build(self):
        self.gear('big', 15, 33, self.octet(7, 3), 8, self.octet(9, 4))
        self.gear('small', 35, 13, self.octet(5, 2), 6, self.octet(7, 3))
