# Independent repair; parent preserved.
"""Independent 32px profile of chat-bubble-smile.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '19c6ef7d-2a4a-4b02-ab2f-cc87d97f7e58'
SOURCE_PATH = 'pictographic-primitives/symbol/messages bubble round smile_19c6ef7d-2a4a-4b02-ab2f-cc87d97f7e58.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('19c6ef7d-2a4a-4b02-ab2f-cc87d97f7e58', 'pictographic-primitives/symbol/messages bubble round smile_19c6ef7d-2a4a-4b02-ab2f-cc87d97f7e58.svg'),)
PROFILE_SOURCE_KEYS = ('solo/chat-bubble-smile',)
SOLO_SOURCE_ICON_IDS = ('chat-bubble-smile',)
REFERENCE_EXPORT_SHA256 = '8923ba53661b908a7f96607eef4c0e70762b0897a21ef7e8d2b08956c4d888fd'

class RepairVariant(Sub32):
    variant_label = 'Centerline and source fidelity repair'
    icon_id = 'chat-bubble-smile-sub32-v2'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('top', (2, 15), (30, 15), radius_x=14, radius_y=11)
        self.add_bezier('bottom-right', (30, 15), ((30, 22), (23, 28), (16, 28)))
        self.add_bezier('bottom-left', (16, 28), ((12, 28), (10, 27), (8, 25)))
        self.add_polyline('tail', (8, 25), (2, 28), (4, 21))
        self.add_bezier('left', (4, 21), ((3, 20), (2, 17), (2, 15)))
        self.add_contour('round', 'top', 'bottom-right', 'bottom-left')
        self.relate('connect', 'round', 'tail')
        self.relate('connect', 'round', 'left')
        self.relate('connect', 'tail', 'left')
        for x in (12, 20):
            self.add_line(f'eye-{x}', (x, 11), (x, 13))
        self.add_arc('smile', (12, 20), (20, 20), radius_x=4, radius_y=1, sweep=False)

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
REPAIR_PLAN = 'Smiling bubble with two short vertical eyes, oval outline and pointed tail.'
CONSTRUCTION_REFERENCE = 'message-circle'
