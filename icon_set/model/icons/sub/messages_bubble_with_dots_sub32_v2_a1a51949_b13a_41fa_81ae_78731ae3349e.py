"""Independent 32px profile of messages-bubble-with-dots.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'a1a51949-b13a-41fa-81ae-78731ae3349e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/messages bubble with dots_a1a51949-b13a-41fa-81ae-78731ae3349e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a1a51949-b13a-41fa-81ae-78731ae3349e', 'pictographic-primitives/symbol/messages bubble with dots_a1a51949-b13a-41fa-81ae-78731ae3349e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/messages-bubble-with-dots',)
SOLO_SOURCE_ICON_IDS = ('messages-bubble-with-dots',)
REFERENCE_EXPORT_SHA256 = '39f8291b05f35e684ddf67feec2714d56e71bdfd75efac63617f290be00c2909'

class DrawingVariant2(Sub32):
    icon_id = 'messages-bubble-with-dots-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Oval chat bubble with curved tail and three equally spaced dots. Construction reference: message-circle."""
        self.add_bezier('top-l', (2, 15), ((2, 9), (8, 4), (16, 4)))
        self.add_bezier('top-r', (16, 4), ((24, 4), (30, 9), (30, 15)))
        self.add_bezier('bottom-r', (30, 15), ((30, 22), (23, 27), (12, 24)))
        self.add_bezier('tail-bottom', (12, 24), ((9, 27), (5, 28), (2, 28)))
        self.add_bezier('tail-top', (2, 28), ((5, 27), (6, 25), (6, 23)))
        self.add_bezier('bottom-l', (6, 23), ((4, 21), (2, 18), (2, 15)))
        self.add_contour('bubble', 'top-l', 'top-r', 'bottom-r', 'tail-bottom', 'tail-top', 'bottom-l', closed=True)
        for x in (9, 16, 23):
            self.add_dot(f'dot-{x}', (x, 15))

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
