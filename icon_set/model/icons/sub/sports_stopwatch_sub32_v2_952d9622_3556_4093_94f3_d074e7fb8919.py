"""Independent 32px profile of sports-stopwatch.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '952d9622-3556-4093-94f3-d074e7fb8919'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/sports/timer_952d9622-3556-4093-94f3-d074e7fb8919.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('952d9622-3556-4093-94f3-d074e7fb8919', 'pictographic-primitives/sports/timer_952d9622-3556-4093-94f3-d074e7fb8919.svg'),)
PROFILE_SOURCE_KEYS = ('solo/sports-stopwatch',)
SOLO_SOURCE_ICON_IDS = ('sports-stopwatch',)
REFERENCE_EXPORT_SHA256 = 'a39008e26511f672ab6d5c2915c526f363e0b6ca61e7ef1459604e80e3f6b971'

class DrawingVariant2(Sub32):
    icon_id = 'sports-stopwatch-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'sports'
    categories = ('sports', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Round stopwatch with connected stem and cap, preserving the single diagonal hand. Construction reference: timer."""
        circle(self, 'dial', 16, 20, 10)
        self.add_line('stem', (16, 2), (16, 10))
        self.relate('connect', 'stem', 'dial')
        self.add_line('cap', (12, 2), (20, 2))
        self.relate('connect', 'cap', 'stem')
        self.add_line('hand', (16, 20), (18, 18))

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
