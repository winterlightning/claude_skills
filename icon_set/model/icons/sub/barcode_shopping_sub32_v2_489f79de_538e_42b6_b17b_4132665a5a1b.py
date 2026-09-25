"""Independent 32px profile of barcode-shopping.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '489f79de-538e-42b6-b17b-4132665a5a1b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/shopping/barcode_489f79de-538e-42b6-b17b-4132665a5a1b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('489f79de-538e-42b6-b17b-4132665a5a1b', 'pictographic-primitives/shopping/barcode_489f79de-538e-42b6-b17b-4132665a5a1b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/barcode-shopping',)
SOLO_SOURCE_ICON_IDS = ('barcode-shopping',)
REFERENCE_EXPORT_SHA256 = 'f60bec9fb1ed24ae0f22bb9e0851ed4348efb649ba0533f2d9f75e86d83c92dd'

class DrawingVariant2(Sub32):
    icon_id = 'barcode-shopping-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'shopping'
    categories = ('shopping', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Rounded enclosing square with all 4 vertical barcode bars. Small-size treatment: Reduced the barcode to three bars and opened the enclosure into four scan corners. Construction reference: scan-barcode: closed frame and repeated vertical strokes."""
        for name, pts in [('tl', ((2, 6), (2, 2), (6, 2))), ('tr', ((26, 2), (30, 2), (30, 6))), ('bl', ((2, 26), (2, 30), (6, 30))), ('br', ((26, 30), (30, 30), (30, 26)))]:
            self.add_polyline(name, *pts)
        for i, (x, top, bottom) in enumerate(((8, 10, 22), (16, 8, 24), (24, 10, 22))):
            self.add_line(f'bar-{i}', (x, top), (x, bottom))

def box(s, n, l, t, r, b, k=3):
    if k == 0:
        s.add_polyline(n, (l, t), (r, t), (r, b), (l, b), (l, t))
        return
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
