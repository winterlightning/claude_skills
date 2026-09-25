"""Independent 32px profile of square-barcode-scanning-icon-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '2d49d0f6-d1d8-4784-9532-65114f883c0c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/shopping/barcode_2d49d0f6-d1d8-4784-9532-65114f883c0c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2d49d0f6-d1d8-4784-9532-65114f883c0c', 'pictographic-primitives/shopping/barcode_2d49d0f6-d1d8-4784-9532-65114f883c0c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/square-barcode-scanning-icon-solo',)
SOLO_SOURCE_ICON_IDS = ('square-barcode-scanning-icon-solo',)
REFERENCE_EXPORT_SHA256 = '9c5a50472323fbff80f02b4c27bfa82552864fe4384c4c6bd9597436b3381566'

class DrawingVariant2(Sub32):
    icon_id = 'square-barcode-scanning-icon-solo-profile32-v2'
    variant_of = 'square-barcode-scanning-icon-solo-profile32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'shopping'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Rounded enclosing square with all 5 vertical barcode bars. Small-size treatment: Reduced the barcode to three bars and opened the enclosure into four scan corners. Construction reference: scan-barcode: closed frame and repeated vertical strokes."""
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
