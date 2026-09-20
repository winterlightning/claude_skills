"""Independent 32px profile of wheeled-suitcase-container.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'b77cece9-c086-4a13-b1b9-cef4e798e9a6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/travel/baggage_b77cece9-c086-4a13-b1b9-cef4e798e9a6.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b77cece9-c086-4a13-b1b9-cef4e798e9a6', 'pictographic-primitives/travel/baggage_b77cece9-c086-4a13-b1b9-cef4e798e9a6.svg'),)
PROFILE_SOURCE_KEYS = ('container/wheeled-suitcase-container',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '6e45995adf1f85635ba3fa0c3d979a7e6e8888f1b76951102cf44cf2de0f8d2b'

class DrawingVariant2(Sub32):
    icon_id = 'wheeled-suitcase-container-sub32-v2'
    variant_of = 'wheeled-suitcase-container-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'containers'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Rounded suitcase, raised rectangular handle and two short straight wheel stems. Construction reference: luggage."""
        box(self, 'case', 2, 10, 30, 26, 3)
        self.add_polyline('handle', (11, 10), (11, 2), (21, 2), (21, 10))
        self.relate('connect', 'handle', 'case')
        for i, x in enumerate((9, 23)):
            self.add_line(f'wheel-{i}', (x, 26), (x, 30))
            self.relate('connect', f'wheel-{i}', 'case')

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
