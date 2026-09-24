"""Independent 32px profile of mobile-phone-control-pause.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'b4668e9a-a445-4547-ab4c-3cab57aef111'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/mobile phone control pause_b4668e9a-a445-4547-ab4c-3cab57aef111.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b4668e9a-a445-4547-ab4c-3cab57aef111', 'pictographic-primitives/state/mobile phone control pause_b4668e9a-a445-4547-ab4c-3cab57aef111.svg'),)
PROFILE_SOURCE_KEYS = ('solo/mobile-phone-control-pause',)
SOLO_SOURCE_ICON_IDS = ('mobile-phone-control-pause',)
REFERENCE_EXPORT_SHA256 = 'fc287b2033f1f997471d2a1565723715760e86edebee783467b4c541f1728693'

class DrawingVariant2(Sub32):
    icon_id = 'mobile-phone-control-pause-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Rounded smartphone with two pause bars and complete footer divider. Construction reference: smartphone."""
        box(self, 'phone', 4, 2, 28, 30, 3)
        self.add_line('footer', (4, 22), (28, 22))
        self.relate('connect', 'phone', 'footer')
        for i, x in enumerate((12, 20)):
            self.add_line(f'pause-{i}', (x, 10), (x, 14))

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
