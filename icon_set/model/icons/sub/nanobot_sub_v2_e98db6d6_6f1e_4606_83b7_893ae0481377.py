"""Circle, six-sided nanobot with central dot and two curved appendages. Complete-source repair; previous variant preserved."""
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Circle, six-sided nanobot with central dot and two curved appendages. Complete-source repair; previous variant preserved.'
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Nanobot: A hexagonal robot body has a tiny central dot and two curved claw-like legs extending from its lower sides. Generate this component alone; exclude Circle Frame.\n\nConstruction: A hexagonal body with one dot has two open curved appendages attached low on its sides.\nKeyshape: SQUARE; authored to the SUB32 envelope.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'e98db6d6-6f1e-4606-83b7-893ae0481377'
SOURCE_PATH = 'pictographic-primitives/state/circle nanobot_e98db6d6-6f1e-4606-83b7-893ae0481377.svg'
AUTHOR = 'gpt-6'

class NanobotSubVariant2(SourceFaithfulSideSub):
    icon_id = 'nanobot-sub-v2'
    variant_of = 'nanobot-sub'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('nanobot', 'hexagonal', 'robot', 'body', 'tiny', 'central', 'dot', 'curved')
    keyshape = Keyshape.SQUARE
    canvas_width = 48
    canvas_height = 48

    def build(self):
        """Circle, six-sided nanobot with central dot and two curved appendages."""
        circle(self, 'frame', 24, 24, 22)
        self.add_polyline('body', (16, 15), (24, 10), (32, 15), (32, 27), (24, 32), (16, 27), closed=True)
        self.add_dot('core', (24, 21))
        self.add_bezier('leg-left', (16, 27), ((12, 32), (14, 35), (16, 37)))
        self.add_bezier('leg-right', (32, 27), ((36, 32), (34, 35), (32, 37)))
        self.relate('connect', 'body', 'leg-left')
        self.relate('connect', 'body', 'leg-right')

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
