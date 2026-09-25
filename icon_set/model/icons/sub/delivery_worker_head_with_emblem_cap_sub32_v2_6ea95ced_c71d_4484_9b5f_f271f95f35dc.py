"""Independent 32px profile of delivery-worker-head-with-emblem-cap.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '6ea95ced-c71d-4484-9b5f-f271f95f35dc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/delivery/delivery man give_6ea95ced-c71d-4484-9b5f-f271f95f35dc.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6ea95ced-c71d-4484-9b5f-f271f95f35dc', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/delivery/delivery man give_6ea95ced-c71d-4484-9b5f-f271f95f35dc.svg'),)
PROFILE_SOURCE_KEYS = ('solo/delivery-worker-head-with-emblem-cap',)
SOLO_SOURCE_ICON_IDS = ('delivery-worker-head-with-emblem-cap',)
REFERENCE_EXPORT_SHA256 = 'f5ca168663e039620b80c906f20a62deceb074fe5e3512a8f339cbdac76408eb'

class DrawingVariant2(Sub32):
    icon_id = 'delivery-worker-head-with-emblem-cap-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'delivery'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Delivery-worker cap with emblem, two eyes and open curved cheeks. Construction reference: human_ref/user.svg: circular cheek arcs; source cap retained."""
        self.add_polyline('cap', (6, 16), (8, 4), (16, 2), (24, 4), (26, 16))
        self.add_line('brim', (2, 16), (30, 16))
        self.relate('connect', 'cap', 'brim')
        self.add_line('emblem', (16, 9), (16, 9))
        for name, x, end in [('left', 4, (10, 30)), ('right', 28, (22, 30))]:
            self.add_line(name + '-side', (x, 16), (x, 20))
            self.add_arc(name + '-cheek', (x, 20), end, radius_x=12, sweep=name == 'right')
            self.add_contour(name, name + '-side', name + '-cheek')
            self.relate('connect', name, 'brim')
        for n, x in [('left', 12), ('right', 20)]:
            self.add_line(n + '-eye', (x, 23), (x, 23))

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
