from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Bell: A bell has a rounded crown with a small top knob, widening sides, and a flared straight lower rim. A tiny detached horizontal clapper appears beneath the centre.\n\nConstruction: The source bell keeps its crown knob, flared rim and detached short clapper.\nKeyshape: SQUARE; the four extrema follow the SUB32 contract.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '14b2c83a-b6f9-4186-8a3b-4d7a1895c6ec'
SOURCE_PATH = 'pictographic-primitives/state/notification_14b2c83a-b6f9-4186-8a3b-4d7a1895c6ec.svg'
AUTHOR = 'gpt-6'

class BellSubState187Variant3(SourceFaithfulSideSub):
    icon_id = 'bell-sub-state-187-v3'
    variant_of = 'bell-sub-state-187'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('bell', 'rounded', 'crown', 'small', 'top', 'knob', 'widening', 'sides')
    keyshape = Keyshape.SQUARE
    canvas_width = 32
    canvas_height = 32

    def build(self):
        """Bell with the original rounded top bump, flared lower rim and detached clapper."""
        self.add_bezier('bell-left', (2, 22), ((6, 18), (6, 17), (6, 12)))
        self.add_bezier('shoulder-left', (6, 12), ((6, 8), (9, 6), (12, 6)))
        self.add_arc('rounded-top', (12, 6), (20, 6), radius_x=4, sweep=True)
        self.add_bezier('shoulder-right', (20, 6), ((23, 6), (26, 8), (26, 12)))
        self.add_bezier('bell-right', (26, 12), ((26, 17), (26, 18), (30, 22)))
        self.add_line('rim', (30, 22), (2, 22))
        self.add_contour('bell', 'bell-left', 'shoulder-left', 'rounded-top', 'shoulder-right', 'bell-right', 'rim')
        self.add_line('clapper', (14, 30), (18, 30))

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
