"""Independent 32px profile of user-profile-with-plus-symbol-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '5c48e4cd-7e6c-4903-8a9d-8562b0e49909'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/doctor_5c48e4cd-7e6c-4903-8a9d-8562b0e49909.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5c48e4cd-7e6c-4903-8a9d-8562b0e49909', 'pictographic-primitives/other/doctor_5c48e4cd-7e6c-4903-8a9d-8562b0e49909.svg'),)
PROFILE_SOURCE_KEYS = ('solo/user-profile-with-plus-symbol-solo',)
SOLO_SOURCE_ICON_IDS = ('user-profile-with-plus-symbol-solo',)
REFERENCE_EXPORT_SHA256 = '4f7bb313309b9583c1e9623fba4d8e56c0a25d7fb79e80859cf9a17af233ddcd'

class DrawingVariant2(Sub32):
    icon_id = 'user-profile-with-plus-symbol-solo-profile32-v2'
    variant_of = 'user-profile-with-plus-symbol-solo-profile32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Circular user head, smooth shoulders and central plus; shared human reference with exact four-unit head-to-shoulder ink gap. Construction reference: user."""
        circle(self, 'head', 16, 7, 5)
        self.add_bezier('shoulder-l', (4, 30), ((4, 23), (10, 20), (16, 20)))
        self.add_bezier('shoulder-r', (16, 20), ((22, 20), (28, 23), (28, 30)))
        self.add_contour('shoulders', 'shoulder-l', 'shoulder-r')
        self.add_line('plus-h', (13, 28), (19, 28))
        self.add_line('plus-v', (16, 26), (16, 30))
        self.relate('connect', 'plus-h', 'plus-v')

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
