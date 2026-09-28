"""Interrupted document, all three original internal marks and rising diagonal slash. Complete-source repair; previous variant preserved."""
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Interrupted document, all three original internal marks and rising diagonal slash. Complete-source repair; previous variant preserved.'
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Diagonal Slash: A long rising diagonal stroke extends from lower-left to upper-right. Generate this component alone; exclude Document.\n\nConstruction: One rising diagonal slash preserves the source angle and excludes the document.\nKeyshape: VRECT_L; authored to the SUB32 envelope.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'bcec186a-7cb0-4c7c-9e2b-c1241cc798a2'
SOURCE_PATH = 'pictographic-primitives/state/rectangle slash_bcec186a-7cb0-4c7c-9e2b-c1241cc798a2.svg'
AUTHOR = 'gpt-6'

class DiagonalSlashVariant2(SourceFaithfulSideSub):
    icon_id = 'diagonal-slash-v2'
    variant_of = 'diagonal-slash'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('diagonal', 'slash', 'long', 'rising', 'stroke', 'extends', 'lower', 'left')
    keyshape = Keyshape.SQUARE
    canvas_width = 36
    canvas_height = 48

    def build(self):
        """Interrupted document, all three original internal marks and rising diagonal slash."""
        self.add_line('slash', (2, 46), (34, 2))
        self.add_line('left', (6, 40), (6, 10))
        self.add_arc('tl', (6, 10), (10, 6), radius_x=4)
        self.add_line('top', (10, 6), (31, 6))
        self.add_contour('upper', 'left', 'tl', 'top')
        self.add_line('right', (34, 14), (34, 38))
        self.add_arc('br', (34, 38), (30, 42), radius_x=4)
        self.add_line('bottom', (30, 42), (14, 42))
        self.add_contour('lower', 'right', 'br', 'bottom')
        self.add_dot('dot', (14, 13))
        self.add_line('mark', (28, 24), (34, 24))
        self.relate('connect', 'mark', 'lower')
        self.add_line('short', (22, 34), (27, 34))
        self.relate('connect', 'slash', 'upper')

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
