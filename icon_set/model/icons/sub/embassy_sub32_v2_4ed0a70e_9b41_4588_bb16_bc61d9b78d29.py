"""Independent 32px profile of embassy.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '4ed0a70e-9b41-4588-bb16-bc61d9b78d29'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/embassy_4ed0a70e-9b41-4588-bb16-bc61d9b78d29.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4ed0a70e-9b41-4588-bb16-bc61d9b78d29', 'pictographic-primitives/symbol/embassy_4ed0a70e-9b41-4588-bb16-bc61d9b78d29.svg'),)
PROFILE_SOURCE_KEYS = ('solo/embassy',)
SOLO_SOURCE_ICON_IDS = ('embassy',)
REFERENCE_EXPORT_SHA256 = '2d184c606668088db58c4615fae1e8702aaef16f72c63e50e853b9674d2964a4'

class DrawingVariant2(Sub32):
    icon_id = 'embassy-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Domed embassy and four equally spaced columns on common base. Construction reference: landmark."""
        self.add_arc('dome', (4, 14), (28, 14), radius_x=12)
        self.add_line('lintel', (28, 14), (4, 14))
        self.add_contour('roof', 'dome', 'lintel', closed=True)
        self.add_line('base', (2, 30), (30, 30))
        for x in (4, 12, 20, 28):
            self.add_line(f'column-{x}', (x, 14), (x, 30))
            self.relate('connect', f'column-{x}', 'roof')
            self.relate('connect', f'column-{x}', 'base')

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
