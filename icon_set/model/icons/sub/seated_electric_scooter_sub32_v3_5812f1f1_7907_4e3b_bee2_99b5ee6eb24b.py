"""Independent 32px profile of seated-electric-scooter.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '5812f1f1-7907-4e3b-bee2-99b5ee6eb24b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/transportation/scooter_5812f1f1-7907-4e3b-bee2-99b5ee6eb24b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5812f1f1-7907-4e3b-bee2-99b5ee6eb24b', 'pictographic-primitives/transportation/scooter_5812f1f1-7907-4e3b-bee2-99b5ee6eb24b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/seated-electric-scooter',)
SOLO_SOURCE_ICON_IDS = ('seated-electric-scooter',)
REFERENCE_EXPORT_SHA256 = '6d9e39f55b062cd667d346f1fd91bafc3e674d4168b6f5979154ec0d22408440'

class DrawingVariant3(Sub32):
    icon_id = 'seated-electric-scooter-sub32-v3'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'transportation'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Seated scooter with two open wheels, seat, chassis and upright handle. Construction reference: bike: external wheel connections and coherent frame."""
        circle(self, 'rear', 7, 25, 5)
        circle(self, 'front', 25, 25, 5)
        self.add_line('deck', (7, 20), (7, 16))
        self.add_bezier('rise', (7, 16), ((7, 12), (13, 12), (16, 15)))
        self.add_line('upper-frame', (16, 15), (22, 10))
        self.add_contour('frame', 'deck', 'rise', 'upper-frame')
        self.relate('connect', 'frame', 'rear')
        self.add_polyline('steering', (16, 2), (20, 2), (22, 10), (25, 20))
        self.relate('connect', 'steering', 'frame')
        self.relate('connect', 'steering', 'front')
        self.add_line('seat-post', (12, 4), (16, 15))
        self.relate('connect', 'seat-post', 'frame')
        self.add_line('seat', (8, 4), (16, 4))
        self.relate('connect', 'seat', 'seat-post')

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
