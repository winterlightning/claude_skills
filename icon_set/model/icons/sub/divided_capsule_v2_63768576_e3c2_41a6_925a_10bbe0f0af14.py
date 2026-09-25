"""SIM-card outline with clipped upper-right corner and divided inner capsule. Complete-source repair; previous variant preserved."""
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'SIM-card outline with clipped upper-right corner and divided inner capsule. Complete-source repair; previous variant preserved.'
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Divided Capsule: An upright rounded capsule is divided into equal upper and lower halves by a horizontal line. Generate this component alone; exclude Cut-Corner Document Frame.\n\nConstruction: An upright rounded capsule is divided halfway by a horizontal line.\nKeyshape: VRECT_L; authored to the SUB32 envelope.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '63768576-e3c2-41a6-925a-10bbe0f0af14'
SOURCE_PATH = 'pictographic-primitives/state/rtf format_63768576-e3c2-41a6-925a-10bbe0f0af14.svg'
AUTHOR = 'gpt-6'

class DividedCapsuleVariant2(SourceFaithfulSideSub):
    icon_id = 'divided-capsule-v2'
    variant_of = 'divided-capsule'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('divided', 'capsule', 'upright', 'rounded', 'equal', 'upper', 'lower', 'halves')
    keyshape = Keyshape.SQUARE
    canvas_width = 40
    canvas_height = 48

    def build(self):
        """SIM-card outline with clipped upper-right corner and divided inner capsule."""
        self.add_line('edge-1', (6, 2), (28, 2))
        self.add_line('edge-2', (28, 2), (38, 12))
        self.add_line('edge-3', (38, 12), (38, 42))
        self.add_arc('br', (38, 42), (34, 46), radius_x=4)
        self.add_line('bottom', (34, 46), (6, 46))
        self.add_arc('bl', (6, 46), (2, 42), radius_x=4)
        self.add_line('left', (2, 42), (2, 6))
        self.add_arc('tl', (2, 6), (6, 2), radius_x=4)
        self.add_contour('frame', 'edge-1', 'edge-2', 'edge-3', 'br', 'bottom', 'bl', 'left', 'tl', closed=True)
        box(self, 'chip', 12, 14, 28, 36, 3)
        self.add_line('division', (12, 25), (28, 25))
        self.relate('connect', 'chip', 'division')

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
