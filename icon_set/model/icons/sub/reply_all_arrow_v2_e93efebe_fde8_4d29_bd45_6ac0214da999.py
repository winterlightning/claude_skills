"""Circle, detached left chevron, second arrowhead and curved return shaft. Complete-source repair; previous variant preserved."""
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Circle, detached left chevron, second arrowhead and curved return shaft. Complete-source repair; previous variant preserved.'
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Reply All Arrow: A curved arrow rises from lower right into a left-facing head, with a second left chevron beside its tip. Generate this component alone; exclude Circle Frame.\n\nConstruction: Two left heads precede one rounded return shaft; no extra arrow is introduced.\nKeyshape: HRECT_XL; authored to the SUB32 envelope.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'e93efebe-fde8-4d29-bd45-6ac0214da999'
SOURCE_PATH = 'pictographic-primitives/state/circle reply all_e93efebe-fde8-4d29-bd45-6ac0214da999.svg'
AUTHOR = 'gpt-6'

class ReplyAllArrowVariant2(SourceFaithfulSideSub):
    icon_id = 'reply-all-arrow-v2'
    variant_of = 'reply-all-arrow'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('reply', 'all', 'arrow', 'curved', 'rises', 'lower', 'right', 'left')
    keyshape = Keyshape.SQUARE
    canvas_width = 48
    canvas_height = 48

    def build(self):
        """Circle, detached left chevron, second arrowhead and curved return shaft."""
        circle(self, 'frame', 24, 24, 22)
        self.add_polyline('first', (15, 15), (9, 21), (15, 27))
        self.add_polyline('second', (27, 15), (21, 21), (27, 27))
        self.add_bezier('shaft', (21, 21), ((33, 21), (36, 25), (36, 32)))
        self.relate('connect', 'second', 'shaft')

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
