"""Circle enclosing a complete playback triangle and separate directional chevron. Complete-source repair; previous variant preserved."""
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Circle enclosing a complete playback triangle and separate directional chevron. Complete-source repair; previous variant preserved.'
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Next Playback: An outlined right-pointing triangle is followed by a detached right chevron of similar height. Generate this component alone; exclude Circle Frame.\n\nConstruction: A right triangle precedes a detached right chevron.\nKeyshape: HRECT_XL; authored to the SUB32 envelope.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '97e55857-e9a6-4c5f-83bf-abfd96b372ad'
SOURCE_PATH = 'pictographic-primitives/state/circle play forward_97e55857-e9a6-4c5f-83bf-abfd96b372ad.svg'
AUTHOR = 'gpt-6'

class NextPlaybackVariant2(SourceFaithfulSideSub):
    icon_id = 'next-playback-v2'
    variant_of = 'next-playback'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('next', 'playback', 'outlined', 'right', 'pointing', 'triangle', 'followed', 'detached')
    keyshape = Keyshape.SQUARE
    canvas_width = 48
    canvas_height = 48

    def build(self):
        """Circle enclosing a complete playback triangle and separate directional chevron."""
        circle(self, 'frame', 24, 24, 22)
        self.add_polyline('triangle', (13, 15), (25, 24), (13, 33), closed=True)
        self.add_polyline('chevron', (29, 15), (39, 24), (29, 33))

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
