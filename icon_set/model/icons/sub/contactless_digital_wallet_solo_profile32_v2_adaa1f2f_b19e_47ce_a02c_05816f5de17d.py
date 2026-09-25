"""Independent 32px profile of contactless-digital-wallet-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'adaa1f2f-b19e-47ce-a02c-05816f5de17d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/wallet wifi_adaa1f2f-b19e-47ce-a02c-05816f5de17d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('adaa1f2f-b19e-47ce-a02c-05816f5de17d', 'pictographic-primitives/other/wallet wifi_adaa1f2f-b19e-47ce-a02c-05816f5de17d.svg'),)
PROFILE_SOURCE_KEYS = ('solo/contactless-digital-wallet-solo',)
SOLO_SOURCE_ICON_IDS = ('contactless-digital-wallet-solo',)
REFERENCE_EXPORT_SHA256 = '71692d2dc6d94ba391143845826aa618d6359c6e0703f34b97aee8ed7169f685'

class DrawingVariant2(Sub32):
    icon_id = 'contactless-digital-wallet-solo-profile32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Contactless wallet: two Wi-Fi arcs above an open folded wallet with its diagonal flap. Construction reference: wallet."""
        self.add_bezier('wifi-l', (2, 6), ((6, 3), (11, 2), (16, 2)))
        self.add_bezier('wifi-r', (16, 2), ((21, 2), (26, 3), (30, 6)))
        self.add_contour('wifi', 'wifi-l', 'wifi-r')
        self.add_bezier('signal', (10, 11), ((14, 8), (18, 8), (22, 11)))
        self.add_line('top', (8, 18), (24, 18))
        self.add_arc('tr', (24, 18), (27, 21), radius_x=3)
        self.add_line('back', (27, 21), (27, 27))
        self.add_contour('back-leaf', 'top', 'tr', 'back')
        self.add_bezier('fold-top', (8, 18), ((5, 18), (5, 20), (5, 22)))
        self.add_line('fold-left', (5, 22), (5, 25))
        self.add_bezier('fold-base', (5, 25), ((5, 27), (11, 30), (14, 30)))
        self.add_bezier('fold-tip', (14, 30), ((17, 30), (17, 29), (17, 27)))
        self.add_line('fold-right', (17, 27), (17, 23))
        self.add_bezier('fold-diagonal', (17, 23), ((17, 21), (11, 19), (8, 18)))
        self.add_contour('fold', 'fold-top', 'fold-left', 'fold-base', 'fold-tip', 'fold-right', 'fold-diagonal', closed=True)
        self.relate('connect', 'fold', 'back-leaf')

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
