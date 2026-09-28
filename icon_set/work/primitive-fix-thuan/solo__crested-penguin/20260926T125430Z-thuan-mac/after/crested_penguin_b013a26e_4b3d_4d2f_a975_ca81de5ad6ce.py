"""Crested penguin, front view: an upright egg-shaped body with a feather
crest on the crown, two eyes, a small beak and a white front.
Review (meaning): the earlier side-on body with a slash read as a chick. This
revision uses the reference's frontal pose: symmetric body, eyes either side
of a V beak, a white belly bounded by an arch over the lower body, and the crest
sweeping off the crown to the right as in the reference.
Keyshape SQUARE (6,6)-(42,42): the flippers need the width.
Symbol plan: body contour = two flattened crown cubics (so the eyes clear
them), straight flanks, and a four-cubic bottom whose (13,40)/(35,40) knots
anchor the belly arch; eyes, beak and belly mirror about x=24 with 8+ units
between rows; the crest cubic leaves the crown node and ends level at y=4,
setting the top extreme.
Lucide construction: bird/egg outlines; human_ref not applicable.
Omissions: flippers and feet (no 8-unit room outside a 28-wide body).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b013a26e-4b3d-4d2f-a975-ca81de5ad6ce'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__crested-penguin/20260926T125430Z-thuan-mac/reference/penguin crested_b013a26e-4b3d-4d2f-a975-ca81de5ad6ce.svg'
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

class CrestedPenguin(_Shapes, Solo48):
    icon_id = 'crested-penguin'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals/birds'
    categories = ('animals',)
    aliases = ('penguin crested', 'rockhopper penguin')
    keywords = ('penguin', 'crested', 'bird', 'rockhopper', 'antarctic', 'animal')

    def build(self):
        L, R, crown, flank, wing, low, B = 10, 38, 8, 20, 24, 32, 42
        b = self.add_bezier
        b('crown-l', (L, flank), ((L, 12), (15, crown), (24, crown)))
        b('crown-r', (24, crown), ((33, crown), (R, 12), (R, flank)))
        self.add_line('flank-r1', (R, flank), (R, wing))
        self.add_line('flank-r2', (R, wing), (R, low))
        b('bottom-r', (R, low), ((R, 38), (32, B), (24, B)))
        b('bottom-l', (24, B), ((16, B), (L, 38), (L, low)))
        self.add_line('flank-l2', (L, low), (L, wing))
        self.add_line('flank-l1', (L, wing), (L, flank))
        self.add_contour('body', 'crown-l', 'crown-r', 'flank-r1', 'flank-r2', 'bottom-r',
                         'bottom-l', 'flank-l2', 'flank-l1', closed=True)
        self.add_line('flipper-l', (L, wing), (6, 30))
        self.add_line('flipper-r', (R, wing), (42, 30))
        b('crest', (24, crown), ((27, 6), (30, 6), (33, 6)))
        self.add_dot('eye-l', (19, 17))
        self.add_dot('eye-r', (29, 17))
        self.lines('beak', (22, 25), (24, 27), (26, 25))
        for part in ('crest', 'flipper-l', 'flipper-r'):
            self.relate('connect', 'body', part)
