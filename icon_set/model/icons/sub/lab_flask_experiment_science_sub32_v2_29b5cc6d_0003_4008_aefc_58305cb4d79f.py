"""Independent 32px profile of lab-flask-experiment-science.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '29b5cc6d-0003-4008-aefc-58305cb4d79f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/science/lab flask experiment_29b5cc6d-0003-4008-aefc-58305cb4d79f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('29b5cc6d-0003-4008-aefc-58305cb4d79f', 'pictographic-primitives/science/lab flask experiment_29b5cc6d-0003-4008-aefc-58305cb4d79f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/lab-flask-experiment-science',)
SOLO_SOURCE_ICON_IDS = ('lab-flask-experiment-science',)
REFERENCE_EXPORT_SHA256 = 'a7804f8928e3355216fab37ef608b0b62b7975848ef0d27e353d308545abd057'

class DrawingVariant2(Sub32):
    icon_id = 'lab-flask-experiment-science-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'science'
    categories = ('science', 'state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Flat-neck flask, tapered shoulders, rounded base and straight liquid line. Construction reference: flask-conical."""
        self.add_polyline('neck', (12, 12), (12, 2), (20, 2), (20, 12), (28, 25))
        self.add_bezier('br', (28, 25), ((28, 28), (26, 30), (24, 30)))
        self.add_line('base', (24, 30), (8, 30))
        self.add_bezier('bl', (8, 30), ((6, 30), (4, 28), (4, 25)))
        self.add_line('shoulder', (4, 25), (12, 12))
        self.add_contour('flask', 'br', 'base', 'bl', 'shoulder')
        self.relate('connect', 'flask', 'neck')
        self.add_line('liquid', (7, 20), (25, 20))
        self.relate('connect', 'flask', 'liquid')
        self.relate('connect', 'neck', 'liquid')

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
