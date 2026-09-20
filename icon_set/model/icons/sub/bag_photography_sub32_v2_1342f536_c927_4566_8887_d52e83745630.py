"""Independent 32px profile of bag-photography.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '1342f536-c927-4566-8887-d52e83745630'
SOURCE_PATH = 'pictographic-primitives/photography/bag_1342f536-c927-4566-8887-d52e83745630.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1342f536-c927-4566-8887-d52e83745630', 'pictographic-primitives/photography/bag_1342f536-c927-4566-8887-d52e83745630.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bag-photography',)
SOLO_SOURCE_ICON_IDS = ('bag-photography',)
REFERENCE_EXPORT_SHA256 = '7ff31929be22397b73923723917f01cad39286b6ea9c7199944b177063c95000'

class RepairVariant(Sub32):
    variant_label = 'Centerline and source fidelity repair'
    variant_of = 'bag-photography-sub32'
    icon_id = 'bag-photography-sub32-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'photography'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('top', (4, 12), (28, 12))
        self.add_bezier('right', (28, 12), ((28, 17), (30, 22), (30, 26)))
        self.add_arc('corner-r', (30, 26), (26, 30), radius_x=4)
        self.add_line('base', (26, 30), (6, 30))
        self.add_arc('corner-l', (6, 30), (2, 26), radius_x=4)
        self.add_bezier('left', (2, 26), ((2, 22), (4, 17), (4, 12)))
        self.add_contour('bag', 'top', 'right', 'corner-r', 'base', 'corner-l', 'left', closed=True)
        self.add_line('handle-left', (11, 16), (11, 7))
        self.add_arc('handle-top', (11, 7), (21, 7), radius_x=5)
        self.add_line('handle-right', (21, 7), (21, 16))
        self.add_contour('handle', 'handle-left', 'handle-top', 'handle-right')
        self.relate('connect', 'bag', 'handle')

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
REPAIR_PLAN = 'Rounded source shopping bag and arched handle; remove invented flap.'
CONSTRUCTION_REFERENCE = 'shopping-bag'
