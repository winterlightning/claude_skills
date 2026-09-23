"""Independent 32px profile of calculator-wide-display-four-keys.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '824b90e9-b86e-4354-b20c-7de8579c1c3b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/finance/calculator_824b90e9-b86e-4354-b20c-7de8579c1c3b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('824b90e9-b86e-4354-b20c-7de8579c1c3b', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/finance/calculator_824b90e9-b86e-4354-b20c-7de8579c1c3b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/calculator-wide-display-four-keys',)
SOLO_SOURCE_ICON_IDS = ('calculator-wide-display-four-keys',)
REFERENCE_EXPORT_SHA256 = '96f55966fc1f89e2376e26daac3d1b363c26e15194c11492a1c9af2a43adedc5'

class DrawingVariant2(Sub32):
    icon_id = 'calculator-wide-display-four-keys-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/finance'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Calculator frame, separate closed display and four horizontal keys in two rows. Small-size treatment: Simplified the display to a horizontal indicator and retained all four keys as round marks. Construction reference: calculator: display and repeated key grid."""
        box(self, 'body', 4, 2, 28, 30, 4)
        self.add_line('display', (11, 10), (21, 10))
        for i, (x, y) in enumerate(((11, 17), (21, 17), (11, 23), (21, 23))):
            self.add_line(f'key-{i}', (x, y), (x, y))

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
