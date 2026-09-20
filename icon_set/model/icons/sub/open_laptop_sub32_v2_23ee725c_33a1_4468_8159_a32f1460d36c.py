"""Independent 32px profile of open-laptop.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '23ee725c-33a1-4468-8159-a32f1460d36c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/computers/batch-01/laptop 1_23ee725c-33a1-4468-8159-a32f1460d36c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('23ee725c-33a1-4468-8159-a32f1460d36c', 'pictographic-primitives/computers/batch-01/laptop 1_23ee725c-33a1-4468-8159-a32f1460d36c.svg'), ('9c785f9a-558d-4793-8f09-218c477d8c84', 'pictographic-primitives/computers/batch-01/laptop 1_9c785f9a-558d-4793-8f09-218c477d8c84.svg'), ('0eca8bb8-75fe-4501-aa58-53ce337798cc', 'pictographic-primitives/computers/batch-01/laptop_0eca8bb8-75fe-4501-aa58-53ce337798cc.svg'), ('4679969c-dfb9-4a03-ab57-4d2eded56e5a', 'pictographic-primitives/computers/batch-01/laptop_4679969c-dfb9-4a03-ab57-4d2eded56e5a.svg'), ('7a7343f1-5eae-443d-b8b7-d063758ee85e', 'pictographic-primitives/computers/batch-01/laptop_7a7343f1-5eae-443d-b8b7-d063758ee85e.svg'), ('96bd0a70-5265-56a5-8f8c-7df6339b6c49', 'pictographic-primitives/computers/batch-01/laptop_96bd0a70-5265-56a5-8f8c-7df6339b6c49.svg'))
PROFILE_SOURCE_KEYS = ('solo/open-laptop',)
SOLO_SOURCE_ICON_IDS = ('open-laptop',)
REFERENCE_EXPORT_SHA256 = '0323f1e773042f851a32389933df851e2b550da0f626642f2fb36f5d7c5454a8'

class DrawingVariant2(Sub32):
    icon_id = 'open-laptop-sub32-v2'
    variant_of = 'open-laptop-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/device'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Open laptop with rounded screen top, sloping base sides and single shared hinge. Construction reference: laptop."""
        self.add_line('left', (4, 20), (4, 7))
        self.add_arc('tl', (4, 7), (7, 4), radius_x=3)
        self.add_line('top', (7, 4), (25, 4))
        self.add_arc('tr', (25, 4), (28, 7), radius_x=3)
        self.add_line('right', (28, 7), (28, 20))
        self.add_line('hinge', (28, 20), (4, 20))
        self.add_contour('screen', 'left', 'tl', 'top', 'tr', 'right', 'hinge', closed=True)
        self.add_polyline('base', (4, 20), (2, 28), (30, 28), (28, 20))
        self.relate('connect', 'base', 'screen')

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
