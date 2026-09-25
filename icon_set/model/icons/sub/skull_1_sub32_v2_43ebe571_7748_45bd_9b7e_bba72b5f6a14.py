"""Independent 32px profile of skull-1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '43ebe571-7748-45bd-9b7e-bba72b5f6a14'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/skull 1_43ebe571-7748-45bd-9b7e-bba72b5f6a14.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('43ebe571-7748-45bd-9b7e-bba72b5f6a14', 'pictographic-primitives/interface-essential/skull 1_43ebe571-7748-45bd-9b7e-bba72b5f6a14.svg'), ('b6589244-b5a7-49bf-bf40-d9b773c9d505', 'pictographic-primitives/interface-essential/skull_b6589244-b5a7-49bf-bf40-d9b773c9d505.svg'))
PROFILE_SOURCE_KEYS = ('solo/skull-1', 'solo/skull-b6589244')
SOLO_SOURCE_ICON_IDS = ('skull-1', 'skull-b6589244')
REFERENCE_EXPORT_SHA256 = '9a19ed7d7844278ce16ea59f45ebc1cddf3d27fe12a9273c5bd5d4701a6dee52'

class DrawingVariant2(Sub32):
    icon_id = 'skull-1-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    categories = ('interface-essential', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Open skull with domed cranium, two slanted eyes, cheek transitions and three lower tooth strokes. Construction reference: skull."""
        self.add_line('jaw-l', (8, 30), (8, 27))
        self.add_bezier('cheek-l', (8, 27), ((8, 23), (2, 25), (2, 18)))
        self.add_line('side-l', (2, 18), (2, 16))
        self.add_arc('crown', (2, 16), (30, 16), radius_x=14)
        self.add_line('side-r', (30, 16), (30, 18))
        self.add_bezier('cheek-r', (30, 18), ((30, 25), (24, 23), (24, 27)))
        self.add_line('jaw-r', (24, 27), (24, 30))
        self.add_contour('skull', 'jaw-l', 'cheek-l', 'side-l', 'crown', 'side-r', 'cheek-r', 'jaw-r')
        self.add_line('tooth', (16, 28), (16, 30))
        self.add_line('eye-l', (10, 15), (12, 16))
        self.add_line('eye-r', (22, 15), (20, 16))

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
