"""Cooking pot with lid: a pot body with side handles, a domed lid resting on
the rim and a round knob on top.
Review (meaning): the earlier flat drum with a stick read as a pie or a drum.
This revision follows the reference and Lucide `cooking-pot`: the rim line
runs past the walls as handles, the lid is a clear dome over the rim, and the
knob is a small ring rather than a pole.
Keyshape HRECT_L (4,8)-(44,40).
Symbol plan: rim line 4..44 split at the wall and lid nodes (8,24)/(40,24);
lid = two elliptical quarter arcs (rx16, ry10) meeting at the top node where
the r3 knob ring sits; body walls with r4 bottom corners; mirrored about x=24.
Lucide construction: cooking-pot (h-line rim with handle overhang, U body)
at 2x.
Omissions: steam.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6696729f-6eb0-4c03-96db-99c8e1e23356'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cooking-pot-with-lid/20260926T125430Z-thuan-mac/reference/lid_6696729f-6eb0-4c03-96db-99c8e1e23356.svg'
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

class CookingPotWithLid(_Shapes, Solo48):
    icon_id = 'cooking-pot-with-lid'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/kitchen'
    categories = ('food', 'objects')
    aliases = ('lid', 'pot', 'saucepan', 'casserole')
    keywords = ('lid', 'pot', 'cooking', 'kitchen', 'saucepan', 'casserole', 'cookware')

    def build(self):
        rim, Lw, Rw, B = 24, 8, 40, 40
        self.lines('rim', (4, rim), (Lw, rim), (Rw, rim), (44, rim))
        a = self.add_arc
        a('lid-l', (Lw, rim), (24, 14), radius_x=16, radius_y=10)
        a('lid-r', (24, 14), (Rw, rim), radius_x=16, radius_y=10)
        self.add_contour('lid', 'lid-l', 'lid-r')
        a('knob-0', (24, 14), (21, 11), radius_x=3)
        a('knob-1', (21, 11), (24, 8), radius_x=3)
        a('knob-2', (24, 8), (27, 11), radius_x=3)
        a('knob-3', (27, 11), (24, 14), radius_x=3)
        self.add_contour('knob', 'knob-0', 'knob-1', 'knob-2', 'knob-3', closed=True)
        self.add_line('wall-l', (Lw, rim), (Lw, B - 4))
        a('corner-l', (Lw, B - 4), (Lw + 4, B), radius_x=4, sweep=False)
        self.add_line('base', (Lw + 4, B), (Rw - 4, B))
        a('corner-r', (Rw - 4, B), (Rw, B - 4), radius_x=4, sweep=False)
        self.add_line('wall-r', (Rw, B - 4), (Rw, rim))
        self.add_contour('body', 'wall-l', 'corner-l', 'base', 'corner-r', 'wall-r')
        self.relate('connect', 'rim', 'lid')
        self.relate('connect', 'lid', 'knob')
        self.relate('connect', 'rim', 'body')
