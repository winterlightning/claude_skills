# Independent repair; parent preserved.
"""Independent 32px profile of arrow-counterclockwise-around-circle.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'dd05972e-63bf-5995-a2f2-388ee81ff8fb'
SOURCE_PATH = 'pictographic-primitives/arrows/rotate back_dd05972e-63bf-5995-a2f2-388ee81ff8fb.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('dd05972e-63bf-5995-a2f2-388ee81ff8fb', 'pictographic-primitives/arrows/rotate back_dd05972e-63bf-5995-a2f2-388ee81ff8fb.svg'), ('0b53a87a-e04b-4e3c-adfd-dcf1fbf284e1', 'pictographic-primitives/arrows/rotate_0b53a87a-e04b-4e3c-adfd-dcf1fbf284e1.svg'), ('f16056b7-da9d-4235-8ea0-1437b5422e2d', 'pictographic-primitives/arrows/rotate_f16056b7-da9d-4235-8ea0-1437b5422e2d.svg'))
PROFILE_SOURCE_KEYS = ('solo/arrow-counterclockwise-around-circle',)
SOLO_SOURCE_ICON_IDS = ('arrow-counterclockwise-around-circle',)
REFERENCE_EXPORT_SHA256 = '633f158385c05f040c0b56e524b71d8345ad9deb2eb53ea8284260b9a175c5c9'

class RepairVariant(Sub32):
    variant_label = 'Centerline and source fidelity repair'
    icon_id = 'arrow-counterclockwise-around-circle-sub32-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'arrows'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('lower-left', (2, 16), (16, 30), radius_x=14, sweep=False)
        self.add_arc('right', (16, 30), (16, 2), radius_x=14, sweep=False)
        self.add_bezier('upper-left', (16, 2), ((12, 2), (9, 3), (6, 5)))
        self.add_contour('return', 'lower-left', 'right', 'upper-left')
        self.add_polyline('head', (10, 2), (6, 5), (11, 9))
        self.relate('connect', 'return', 'head')

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
REPAIR_PLAN = 'Smooth circular return arrow with original left-facing arrowhead.'
CONSTRUCTION_REFERENCE = 'rotate-ccw'
