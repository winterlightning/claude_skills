# Independent repair; parent preserved.
"""Independent 32px profile of book-open-1421392c.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '1421392c-5884-4c7e-bf5c-1082165dfba9'
SOURCE_PATH = 'pictographic-primitives/content/book open_1421392c-5884-4c7e-bf5c-1082165dfba9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1421392c-5884-4c7e-bf5c-1082165dfba9', 'pictographic-primitives/content/book open_1421392c-5884-4c7e-bf5c-1082165dfba9.svg'), ('df25e3f8-0308-43ac-83b9-5a03a38cf7f5', 'pictographic-primitives/content/book open 1_df25e3f8-0308-43ac-83b9-5a03a38cf7f5.svg'), ('a147931e-057f-4518-b391-cf08f66084de', 'pictographic-primitives/content/book open_a147931e-057f-4518-b391-cf08f66084de.svg'))
PROFILE_SOURCE_KEYS = ('solo/book-open-1421392c', 'solo/book-open-1-df25e3f8', 'solo/book-open-a147931e')
SOLO_SOURCE_ICON_IDS = ('book-open-1421392c', 'book-open-1-df25e3f8', 'book-open-a147931e')
REFERENCE_EXPORT_SHA256 = '1bae9a15dc9fe7fdec94acae5090512df80fbbba3b114ec69ff3eeeda1a1eec5'

class RepairVariant(Sub32):
    variant_label = 'Centerline and source fidelity repair'
    variant_of = 'book-open-1421392c-sub32'
    icon_id = 'book-open-1421392c-sub32-v2'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'content'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('left-top', (2, 7), (16, 7), radius_x=7, radius_y=3)
        self.add_arc('right-top', (16, 7), (30, 7), radius_x=7, radius_y=3)
        self.add_line('right-edge', (30, 7), (30, 28))
        self.add_arc('right-bottom', (30, 28), (16, 28), radius_x=7, radius_y=3, sweep=False)
        self.add_arc('left-bottom', (16, 28), (2, 28), radius_x=7, radius_y=3, sweep=False)
        self.add_line('left-edge', (2, 28), (2, 7))
        self.add_contour('pages', 'left-top', 'right-top', 'right-edge', 'right-bottom', 'left-bottom', 'left-edge', closed=True)
        self.add_line('fold', (16, 7), (16, 28))
        self.relate('connect', 'pages', 'fold')

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
REPAIR_PLAN = 'Open book with two equal bowed pages and one fold; extremes at arc crests.'
CONSTRUCTION_REFERENCE = 'book-open'
