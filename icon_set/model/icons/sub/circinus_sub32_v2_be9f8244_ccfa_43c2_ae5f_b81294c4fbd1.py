"""Independent 32px profile of circinus.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'be9f8244-ccfa-43c2-ae5f-b81294c4fbd1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/circinus_be9f8244-ccfa-43c2-ae5f-b81294c4fbd1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('be9f8244-ccfa-43c2-ae5f-b81294c4fbd1', 'pictographic-primitives/state/circinus_be9f8244-ccfa-43c2-ae5f-b81294c4fbd1.svg'), ('f18957c4-d496-4dcc-baef-4934631bc063', 'pictographic-primitives/state/circinus_f18957c4-d496-4dcc-baef-4934631bc063.svg'))
PROFILE_SOURCE_KEYS = ('solo/circinus', 'solo/circinus-state')
SOLO_SOURCE_ICON_IDS = ('circinus', 'circinus-state')
REFERENCE_EXPORT_SHA256 = '61055bf0f80c248bfafae792ce040276c3b0d47254c65e00b81e9a868d56b903'

class DrawingVariant2(Sub32):
    icon_id = 'circinus-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Drafting compass with circular pivot, short top stem, two spreading legs and cross brace. Construction reference: drafting-compass."""
        circle(self, 'pivot', 22, 9, 5)
        self.add_line('cap', (25, 5), (30, 2))
        self.relate('connect', 'cap', 'pivot')
        self.add_line('left-leg', (18, 12), (2, 24))
        self.relate('connect', 'left-leg', 'pivot')
        self.add_line('right-leg', (22, 14), (18, 30))
        self.relate('connect', 'right-leg', 'pivot')
        self.add_line('brace', (10, 18), (25, 24))
        self.relate('connect', 'brace', 'left-leg')
        self.relate('connect', 'brace', 'right-leg')

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
