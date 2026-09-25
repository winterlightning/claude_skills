# Independent repair; parent preserved.
"""Independent 32px profile of beaker.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'f1cab2ea-f7f8-47a0-972d-7983402b29a8'
SOURCE_PATH = 'pictographic-primitives/symbol/beaker_f1cab2ea-f7f8-47a0-972d-7983402b29a8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f1cab2ea-f7f8-47a0-972d-7983402b29a8', 'pictographic-primitives/symbol/beaker_f1cab2ea-f7f8-47a0-972d-7983402b29a8.svg'),)
PROFILE_SOURCE_KEYS = ('solo/beaker',)
SOLO_SOURCE_ICON_IDS = ('beaker',)
REFERENCE_EXPORT_SHA256 = '95b7b20a8d78444cd276bad327e730c6f1de876b8d4e59019a9e377f9632ea9c'

class RepairVariant(Sub32):
    variant_label = 'Centerline and source fidelity repair'
    icon_id = 'beaker-sub32-v2'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('neck-left', (12, 2), (12, 7))
        self.add_bezier('shoulder-left', (12, 7), ((12, 11), (4, 11), (4, 18)))
        self.add_arc('bowl', (4, 18), (28, 18), radius_x=12, sweep=False)
        self.add_bezier('shoulder-right', (28, 18), ((28, 11), (20, 11), (20, 7)))
        self.add_line('neck-right', (20, 7), (20, 2))
        self.add_contour('flask', 'neck-left', 'shoulder-left', 'bowl', 'shoulder-right', 'neck-right')
        self.add_line('rim', (9, 2), (23, 2))
        self.relate('connect', 'flask', 'rim')

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
REPAIR_PLAN = 'Round-bottom flask with symmetric flowing shoulders and eight-unit neck.'
CONSTRUCTION_REFERENCE = 'flask-round'
