# Independent repair; parent preserved.
"""Independent 32px profile of blind.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '5dce7e9a-2184-434a-9e94-71138d2b612d'
SOURCE_PATH = 'pictographic-primitives/interface-essential/blind_5dce7e9a-2184-434a-9e94-71138d2b612d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5dce7e9a-2184-434a-9e94-71138d2b612d', 'pictographic-primitives/interface-essential/blind_5dce7e9a-2184-434a-9e94-71138d2b612d.svg'),)
PROFILE_SOURCE_KEYS = ('solo/blind',)
SOLO_SOURCE_ICON_IDS = ('blind',)
REFERENCE_EXPORT_SHA256 = 'de5bd426cf9070e4f9280e10ff9493847089e546ec1fd1352c5e39b2a582fe4b'

class RepairVariant(Sub32):
    variant_label = 'Centerline and source fidelity repair'
    icon_id = 'blind-sub32-v2'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('top-left', (2, 16), ((6, 10), (10, 8), (16, 8)))
        self.add_bezier('top-right-a', (16, 8), ((19, 8), (21, 9), (23, 10)))
        self.add_bezier('top-right-b', (23, 10), ((25, 11), (28, 13), (30, 16)))
        self.add_bezier('bottom-right', (30, 16), ((26, 22), (22, 24), (16, 24)))
        self.add_bezier('bottom-left-a', (16, 24), ((13, 24), (11, 23), (9, 22)))
        self.add_bezier('bottom-left-b', (9, 22), ((7, 21), (4, 19), (2, 16)))
        self.add_contour('eye', 'top-left', 'top-right-a', 'top-right-b', 'bottom-right', 'bottom-left-a', 'bottom-left-b', closed=True)
        self.add_line('slash', (9, 22), (23, 10))
        self.relate('connect', 'eye', 'slash')

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
REPAIR_PLAN = 'Almond eye with ascending slash as in source, joined exactly to outline.'
CONSTRUCTION_REFERENCE = 'eye-off'
