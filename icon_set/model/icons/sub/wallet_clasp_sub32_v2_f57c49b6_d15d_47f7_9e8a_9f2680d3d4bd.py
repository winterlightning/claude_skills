"""Independent 32px profile of wallet-clasp.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'f57c49b6-d15d-47f7-9e8a-9f2680d3d4bd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/wallet_f57c49b6-d15d-47f7-9e8a-9f2680d3d4bd.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f57c49b6-d15d-47f7-9e8a-9f2680d3d4bd', 'pictographic-primitives/symbol/wallet_f57c49b6-d15d-47f7-9e8a-9f2680d3d4bd.svg'),)
PROFILE_SOURCE_KEYS = ('solo/wallet-clasp',)
SOLO_SOURCE_ICON_IDS = ('wallet-clasp',)
REFERENCE_EXPORT_SHA256 = 'b4723a46cd93b18bf5fb5fcf0dad6e9c2d424c06fcc22e72c7947aefc9339692'

class DrawingVariant2(Sub32):
    icon_id = 'wallet-clasp-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Wallet outline, upper lining, rounded clasp and original clasp dot restored. Construction reference: wallet."""
        box(self, 'wallet', 2, 2, 30, 30, 3)
        self.add_line('lining', (2, 10), (10, 10))
        self.relate('connect', 'lining', 'wallet')
        self.add_line('clasp-top', (30, 10), (20, 10))
        self.add_arc('clasp-end', (20, 10), (20, 22), radius_x=6, sweep=False)
        self.add_line('clasp-bottom', (20, 22), (30, 22))
        self.relate('connect', 'clasp-top', 'clasp-end')
        self.relate('connect', 'clasp-end', 'clasp-bottom')
        self.relate('connect', 'clasp-top', 'wallet')
        self.relate('connect', 'clasp-bottom', 'wallet')
        self.add_dot('button', (23, 16))

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
