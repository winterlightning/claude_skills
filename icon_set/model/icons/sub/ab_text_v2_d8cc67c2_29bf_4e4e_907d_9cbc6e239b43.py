from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'AB lettering: preserve the original A followed by a rounded B.\nConstruction: The A uses a broader open counter and crossbar; two rounded B bowls retain the original letter ordering.\nKeyshape: HRECT_XL; authored to the SUB32 envelope.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'd8cc67c2-29bf-4e4e-907d-9cbc6e239b43'
SOURCE_PATH = 'pictographic-primitives/state/ab text in circle_d8cc67c2-29bf-4e4e-907d-9cbc6e239b43.svg'
AUTHOR = 'gpt-6'

class AbTextVariant2(SourceFaithfulSideSub):
    icon_id = 'ab-text-v2'
    variant_of = 'ab-text'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('a', 'b', 'letters', 'text')
    keyshape = Keyshape.SQUARE
    canvas_width = 96
    canvas_height = 96

    def build(self):
        """Complete circle enclosing the original uppercase AB in order, reusing shared letters."""
        circle(self, 'frame', 48, 48, 46)
        self.add_line('a-p1-r1-1', (18, 64), (29, 33))
        self.add_bezier('a-p1-r1-2', (29, 33), ((29.666666666666668, 31.480000000000004), (30.333333333333332, 31.480000000000004), (31, 33)))
        self.add_line('a-p1-r1-3', (31, 33), (42, 64))
        self.add_contour('a-path-1-1', 'a-p1-r1-1', 'a-p1-r1-2', 'a-p1-r1-3', closed=False)
        self.add_line('a-p2-r1-1', (23, 50), (37, 50))
        self.add_contour('a-path-2-1', 'a-p2-r1-1', closed=False)
        self.relate('connect', 'a-path-2-1', 'a-path-1-1')
        self.add_line('b-p1-r1-1', (54, 64), (54, 32))
        self.add_line('b-p1-r1-2', (54, 32), (65, 32))
        self.add_bezier('b-p1-r1-3', (65, 32), ((78.33333333333333, 32), (78.33333333333333, 48), (65, 48)))
        self.add_line('b-p1-r1-4', (65, 48), (54, 48))
        self.add_contour('b-path-1-1', 'b-p1-r1-1', 'b-p1-r1-2', 'b-p1-r1-3', 'b-p1-r1-4', closed=False)
        self.add_bezier('b-p2-r1-1', (65, 48), ((79.22222222222221, 48), (79.22222222222221, 63.999999999999986), (65, 64)))
        self.add_line('b-p2-r1-2', (65, 64), (54, 64))
        self.add_contour('b-path-2-1', 'b-p2-r1-1', 'b-p2-r1-2', closed=False)
        self.relate('connect', 'b-p1-r1-1', 'b-p2-r1-2')
        self.relate('connect', 'b-p1-r1-3', 'b-p2-r1-1')
        self.relate('connect', 'b-p1-r1-4', 'b-p2-r1-1')
        self.relate('connect', 'b-path-2-1', 'b-path-1-1')
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub

def box(s, n, l, t, r, b, k=3):
    points = [(l + k, t), (r - k, t), (r, t + k), (r, b - k), (r - k, b), (l + k, b), (l, b - k), (l, t + k)]
    members = []
    for i, p in enumerate(points):
        q = points[(i + 1) % 8]
        name = f'{n}-{i}'
        if i % 2:
            s.add_arc(name, p, q, radius_x=k)
        else:
            s.add_line(name, p, q)
        members.append(name)
    s.add_contour(n, *members, closed=True)

def circle(s, n, cx, cy, r):
    s.add_arc(n + '-top', (cx - r, cy), (cx + r, cy), radius_x=r)
    s.add_arc(n + '-bottom', (cx + r, cy), (cx - r, cy), radius_x=r)
    s.add_contour(n, n + '-top', n + '-bottom', closed=True)
TYPEFACE_GLYPH_IDS = ('letter-a-uppercase', 'letter-b-uppercase')
