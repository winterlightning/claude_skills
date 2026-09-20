"""Rectangular speech bubble with tail, lock body, shackle and keyhole dot. Complete-source repair; previous variant preserved."""
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Rectangular speech bubble with tail, lock body, shackle and keyhole dot. Complete-source repair; previous variant preserved.'
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Padlock: A rounded rectangular lock body supports a tall arched shackle, with a tiny keyhole dot centred on the body. Generate this component alone; exclude Speech Bubble.\n\nConstruction: The source closed padlock keeps its arched shackle, rounded body and tiny central keyhole dot.\nKeyshape: VRECT_L; the four extrema follow the SUB32 contract.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'ea7c167c-f5f4-4220-ad13-315cf015097a'
SOURCE_PATH = 'pictographic-primitives/state/message lock_ea7c167c-f5f4-4220-ad13-315cf015097a.svg'
AUTHOR = 'gpt-6'

class PadlockState167Variant2(SourceFaithfulSideSub):
    icon_id = 'padlock-state-167-v2'
    variant_of = 'padlock-state-167'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('padlock', 'rounded', 'rectangular', 'lock', 'body', 'supports', 'tall', 'arched')
    keyshape = Keyshape.SQUARE
    canvas_width = 48
    canvas_height = 52

    def build(self):
        """Rectangular speech bubble with tail, lock body, shackle and keyhole dot."""
        self.add_line('top', (6, 2), (42, 2))
        self.add_arc('tr', (42, 2), (46, 6), radius_x=4)
        self.add_line('right', (46, 6), (46, 38))
        self.add_arc('br', (46, 38), (42, 42), radius_x=4)
        self.add_line('tail-1', (42, 42), (20, 42))
        self.add_line('tail-2', (20, 42), (10, 50))
        self.add_line('tail-3', (10, 50), (10, 42))
        self.add_line('tail-4', (10, 42), (6, 42))
        self.add_arc('bl', (6, 42), (2, 38), radius_x=4)
        self.add_line('left', (2, 38), (2, 6))
        self.add_arc('tl', (2, 6), (6, 2), radius_x=4)
        self.add_contour('frame', 'top', 'tr', 'right', 'br', 'tail-1', 'tail-2', 'tail-3', 'tail-4', 'bl', 'left', 'tl', closed=True)
        box(self, 'lock', 15, 20, 33, 34, 2)
        self.add_line('sl', (19, 20), (19, 14))
        self.add_arc('shackle', (19, 14), (29, 14), radius_x=5)
        self.add_line('sr', (29, 14), (29, 20))
        self.add_contour('arch', 'sl', 'shackle', 'sr')
        self.relate('connect', 'arch', 'lock')
        self.add_dot('hole', (24, 27))

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
