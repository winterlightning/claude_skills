"""Independent 32px profile of trash-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '65adbc02-2e53-460d-8ac2-44fa49dbce5f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/trash_65adbc02-2e53-460d-8ac2-44fa49dbce5f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('65adbc02-2e53-460d-8ac2-44fa49dbce5f', 'pictographic-primitives/symbol/trash_65adbc02-2e53-460d-8ac2-44fa49dbce5f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/trash-symbol',)
SOLO_SOURCE_ICON_IDS = ('trash-symbol',)
REFERENCE_EXPORT_SHA256 = '30f99f07168d104c199b39cacd2d0d504c301df1dcc5f3ce655639c3cecd3879'

class DrawingVariant2(Sub32):
    icon_id = 'trash-symbol-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Tapered trash bin, projecting straight lid and rounded open handle. Construction reference: trash."""
        self.add_line('lid', (4, 10), (28, 10))
        self.add_polyline('bin', (6, 10), (9, 30), (23, 30), (26, 10))
        self.relate('connect', 'bin', 'lid')
        self.add_line('handle-l', (11, 10), (11, 6))
        self.add_arc('handle-top', (11, 6), (15, 2), radius_x=4)
        self.add_line('handle-roof', (15, 2), (17, 2))
        self.add_arc('handle-tr', (17, 2), (21, 6), radius_x=4)
        self.add_line('handle-r', (21, 6), (21, 10))
        self.add_contour('handle', 'handle-l', 'handle-top', 'handle-roof', 'handle-tr', 'handle-r')
        self.relate('connect', 'handle', 'lid')

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
