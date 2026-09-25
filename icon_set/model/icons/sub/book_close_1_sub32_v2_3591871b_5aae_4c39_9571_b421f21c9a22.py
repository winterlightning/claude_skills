"""Independent 32px profile of book-close-1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '3591871b-5aae-4c39-9571-b421f21c9a22'
SOURCE_PATH = 'pictographic-primitives/content/book close 1_3591871b-5aae-4c39-9571-b421f21c9a22.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3591871b-5aae-4c39-9571-b421f21c9a22', 'pictographic-primitives/content/book close 1_3591871b-5aae-4c39-9571-b421f21c9a22.svg'),)
PROFILE_SOURCE_KEYS = ('solo/book-close-1',)
SOLO_SOURCE_ICON_IDS = ('book-close-1',)
REFERENCE_EXPORT_SHA256 = 'da04cf885b588700eb7fe32ffd72f7d489223e86f01904d9c2881b245b04d36f'

class RepairVariant(Sub32):
    variant_label = 'Centerline and source fidelity repair'
    icon_id = 'book-close-1-sub32-v2'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'content'
    categories = ('content', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('cover-top', (8, 2), (28, 2))
        self.add_line('cover-right', (28, 2), (28, 22))
        self.add_arc('pages-right', (28, 22), (28, 30), radius_x=8, sweep=False)
        self.add_line('bottom', (28, 30), (8, 30))
        self.add_arc('lower-binding', (8, 30), (4, 26), radius_x=4)
        self.add_line('spine', (4, 26), (4, 6))
        self.add_arc('cover-corner', (4, 6), (8, 2), radius_x=4)
        self.add_contour('outline', 'cover-top', 'cover-right', 'pages-right', 'bottom', 'lower-binding', 'spine', 'cover-corner', closed=True)
        self.add_arc('binding', (4, 26), (8, 22), radius_x=4)
        self.add_line('page-top', (8, 22), (28, 22))
        self.add_contour('seam', 'binding', 'page-top')
        self.relate('connect', 'outline', 'seam')

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
REPAIR_PLAN = 'Closed book from source: cover, curved lower binding, no invented vertical divider.'
CONSTRUCTION_REFERENCE = 'book'
