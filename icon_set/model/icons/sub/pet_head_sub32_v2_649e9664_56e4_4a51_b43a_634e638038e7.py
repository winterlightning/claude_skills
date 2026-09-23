"""Independent 32px profile of pet-head.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '649e9664-56e4-4a51-b43a-634e638038e7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/pet head_649e9664-56e4-4a51-b43a-634e638038e7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('649e9664-56e4-4a51-b43a-634e638038e7', 'pictographic-primitives/symbol/pet head_649e9664-56e4-4a51-b43a-634e638038e7.svg'),)
PROFILE_SOURCE_KEYS = ('solo/pet-head',)
SOLO_SOURCE_ICON_IDS = ('pet-head',)
REFERENCE_EXPORT_SHA256 = '8bb3ceb9ae8d85e969d74979fd0e772cd4c403faa7da43c62bdc07698df8640b'

class DrawingVariant2(Sub32):
    icon_id = 'pet-head-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Round pet head with two rounded ears and a shallow crown between them. Construction reference: none."""
        self.add_bezier('ear-l-top', (6, 14), ((2, 13), (2, 11), (2, 9)))
        self.add_arc('ear-l-crown', (2, 9), (7, 4), radius_x=5)
        self.add_bezier('ear-l-in', (7, 4), ((11, 4), (11, 7), (12, 8)))
        self.add_bezier('crown', (12, 8), ((15, 7), (17, 7), (20, 8)))
        self.add_bezier('ear-r-in', (20, 8), ((21, 7), (21, 4), (25, 4)))
        self.add_arc('ear-r-crown', (25, 4), (30, 9), radius_x=5)
        self.add_bezier('ear-r-top', (30, 9), ((30, 11), (30, 13), (26, 14)))
        self.add_bezier('cheek-r', (26, 14), ((28, 24), (23, 28), (16, 28)))
        self.add_bezier('cheek-l', (16, 28), ((9, 28), (4, 24), (6, 14)))
        self.add_contour('head', 'ear-l-top', 'ear-l-crown', 'ear-l-in', 'crown', 'ear-r-in', 'ear-r-crown', 'ear-r-top', 'cheek-r', 'cheek-l', closed=True)

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
