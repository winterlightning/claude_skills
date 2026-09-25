"""Independent 32px profile of cargo-ship.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '1b1d9d6c-194c-5757-b0b8-4299a625eaaa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/shipping/cargo boat_1b1d9d6c-194c-5757-b0b8-4299a625eaaa.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1b1d9d6c-194c-5757-b0b8-4299a625eaaa', 'pictographic-primitives/shipping/cargo boat_1b1d9d6c-194c-5757-b0b8-4299a625eaaa.svg'),)
PROFILE_SOURCE_KEYS = ('solo/cargo-ship',)
SOLO_SOURCE_ICON_IDS = ('cargo-ship',)
REFERENCE_EXPORT_SHA256 = 'd5f58e07738e0d621e1ea16e28b9d357c769a39e443b5f5dc7293197bd7979d0'

class DrawingVariant2(Sub32):
    icon_id = 'cargo-ship-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'shipping'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Cargo ship with two deck blocks, rear mast, stepped top edge, sloping hull sides and continuous wave waterline. Construction reference: none."""
        self.add_polyline('deck', (2, 18), (12, 18), (16, 20), (30, 20))
        self.add_line('hull-l', (2, 18), (6, 28))
        self.add_line('hull-r', (30, 20), (26, 28))
        self.relate('connect', 'hull-l', 'deck')
        self.relate('connect', 'hull-r', 'deck')
        self.add_polyline('cargo', (4, 18), (4, 6), (12, 6), (12, 18))
        self.relate('connect', 'cargo', 'deck')
        self.add_polyline('cabin', (20, 20), (20, 12), (28, 12), (28, 20))
        self.relate('connect', 'cabin', 'deck')
        self.add_line('mast', (24, 2), (24, 12))
        self.relate('connect', 'mast', 'cabin')
        for i in range(7):
            x = 2 + 4 * i
            y = 26 if i % 2 == 0 else 30
            self.add_bezier(f'wave-{i}-a', (x, 28), ((x + 1, y), (x + 1, y), (x + 2, y)))
            self.add_bezier(f'wave-{i}-b', (x + 2, y), ((x + 3, y), (x + 3, y), (x + 4, 28)))
        self.add_contour('water', *[f'wave-{i}-{s}' for i in range(7) for s in ('a', 'b')])
        self.relate('connect', 'water', 'hull-l')
        self.relate('connect', 'water', 'hull-r')

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
