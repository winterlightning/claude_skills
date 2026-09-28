"""Independent 32px profile of t-shirt.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '2de22ab7-b36e-43f7-805d-727e72c62f15'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/clothes/t shirt_2de22ab7-b36e-43f7-805d-727e72c62f15.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2de22ab7-b36e-43f7-805d-727e72c62f15', 'pictographic-primitives/clothes/t shirt_2de22ab7-b36e-43f7-805d-727e72c62f15.svg'), ('5f0ac9bd-d1ec-43e8-ba78-79f54033a5b7', 'pictographic-primitives/clothes/t shirt_5f0ac9bd-d1ec-43e8-ba78-79f54033a5b7.svg'), ('9aa1a37e-7127-4719-8aeb-03b09b01c294', 'pictographic-primitives/clothes/t shirt_9aa1a37e-7127-4719-8aeb-03b09b01c294.svg'), ('45dc1629-c2e7-477c-80d5-ad5686c1271e', 'pictographic-primitives/clothes/t shirt_45dc1629-c2e7-477c-80d5-ad5686c1271e.svg'), ('bc825952-a086-4761-9814-673ca2bec10b', 'pictographic-primitives/clothes/t shirt_bc825952-a086-4761-9814-673ca2bec10b.svg'))
PROFILE_SOURCE_KEYS = ('solo/t-shirt', 'solo/crew-neck-t-shirt-with-angled-sleeves', 'solo/t-shirt-45dc1629', 'solo/t-shirt-bc825952')
SOLO_SOURCE_ICON_IDS = ('t-shirt', 'crew-neck-t-shirt-with-angled-sleeves', 't-shirt-45dc1629', 't-shirt-bc825952')
REFERENCE_EXPORT_SHA256 = '3b3df99942fcef6e2f4e2e59018e775771aba262055235c6b1ceb0db3006c20d'

class DrawingVariant2(Sub32):
    icon_id = 't-shirt-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'clothes'
    categories = ('clothes', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """T-shirt with round collar, curved shoulders, two sleeve hems, side slits and straight lower hem. Construction reference: shirt."""
        self.add_arc('collar', (10, 2), (22, 2), radius_x=6, sweep=False)
        self.add_bezier('shoulder-r', (22, 2), ((27, 2), (30, 6), (30, 10)))
        pts = ((30, 10), (30, 18), (22, 18), (22, 30), (10, 30), (10, 18), (2, 18), (2, 10))
        for i, (a, b) in enumerate(zip(pts, pts[1:])):
            self.add_line(f'edge-{i}', a, b)
        self.add_bezier('shoulder-l', (2, 10), ((2, 6), (5, 2), (10, 2)))
        self.add_contour('shirt', 'collar', 'shoulder-r', *[f'edge-{i}' for i in range(7)], 'shoulder-l', closed=True)
        for name, x in [('slit-l', 10), ('slit-r', 22)]:
            self.add_line(name, (x, 18), (x, 14))
            self.relate('connect', name, 'shirt')

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
