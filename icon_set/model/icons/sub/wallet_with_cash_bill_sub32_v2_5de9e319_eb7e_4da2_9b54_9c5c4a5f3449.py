"""Independent 32px profile of wallet-with-cash-bill-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '5de9e319-eb7e-4da2-9b54-9c5c4a5f3449'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/wallet_5de9e319-eb7e-4da2-9b54-9c5c4a5f3449.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5de9e319-eb7e-4da2-9b54-9c5c4a5f3449', 'pictographic-primitives/state/wallet_5de9e319-eb7e-4da2-9b54-9c5c4a5f3449.svg'),)
PROFILE_SOURCE_KEYS = ('solo/wallet-with-cash-bill-solo',)
SOLO_SOURCE_ICON_IDS = ('wallet-with-cash-bill-solo',)
REFERENCE_EXPORT_SHA256 = '8039d2f55f827a1ceedd38c4f74323eb316677fdc305c3fb9d1e3722c90cf3eb'

class DrawingVariant2(Sub32):
    icon_id = 'wallet-with-cash-bill-sub32-v2'
    variant_of = 'wallet-with-cash-bill-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Rounded wallet with right fastening tab and angled protruding cash bill. Construction reference: wallet."""
        self.add_line('left', (2, 27), (2, 13))
        self.add_arc('tl', (2, 13), (5, 10), radius_x=3)
        self.add_line('top', (5, 10), (25, 10))
        self.add_arc('tr', (25, 10), (28, 13), radius_x=3)
        self.add_line('right-top', (28, 13), (28, 18))
        self.add_contour('upper', 'left', 'tl', 'top', 'tr', 'right-top')
        self.add_line('right-base', (28, 26), (28, 27))
        self.add_arc('br', (28, 27), (25, 30), radius_x=3)
        self.add_line('base', (25, 30), (5, 30))
        self.add_arc('bl', (5, 30), (2, 27), radius_x=3)
        self.add_contour('lower', 'right-base', 'br', 'base', 'bl')
        self.relate('connect', 'upper', 'lower')
        box(self, 'tab', 20, 18, 30, 26, 3)
        self.relate('connect', 'tab', 'upper')
        self.relate('connect', 'tab', 'lower')
        self.add_polyline('cash', (8, 10), (22, 2), (25, 10))
        self.relate('connect', 'cash', 'upper')

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
