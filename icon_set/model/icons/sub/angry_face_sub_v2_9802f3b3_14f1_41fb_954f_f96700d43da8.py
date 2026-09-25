"""Outer face circle, two sloping eyebrows, two eyes, and the open downturned mouth. Complete-source repair; previous variant preserved."""
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Outer face circle, two sloping eyebrows, two eyes, and the open downturned mouth. Complete-source repair; previous variant preserved.'
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Angry Face: A circular face has sharply inward-slanting eyebrows above tiny eyes and a small downturned mouth. The brows form the strongest interior marks, giving the balanced face a stern expression.\n\nConstruction: Circular expression with inward angled eye strokes and an arched frown; paired features mirror.\nKeyshape: CIRCLE; the four extrema follow the SUB32 contract.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '9802f3b3-14f1-41fb-954f-f96700d43da8'
SOURCE_PATH = 'pictographic-primitives/state/face angry_9802f3b3-14f1-41fb-954f-f96700d43da8.svg'
AUTHOR = 'gpt-6'

class AngryFaceSubVariant2(SourceFaithfulSideSub):
    icon_id = 'angry-face-sub-v2'
    variant_of = 'angry-face-sub'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('angry', 'face', 'circular', 'sharply', 'inward', 'slanting', 'eyebrows', 'tiny')
    keyshape = Keyshape.SQUARE
    canvas_width = 48
    canvas_height = 48

    def build(self):
        """Outer face circle, two sloping eyebrows, two eyes, and the open downturned mouth."""
        circle(self, 'frame', 24, 24, 22)
        self.add_line('brow-left', (12, 15), (19, 19))
        self.add_line('brow-right', (29, 19), (36, 15))
        self.add_dot('eye-left', (17, 25))
        self.add_dot('eye-right', (31, 25))
        self.add_bezier('frown', (16, 36), ((21, 30), (27, 30), (32, 36)))

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
