"""Independent 32px profile of shield-check.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '35439928-bf3d-41d0-ac20-63c8b05f2354'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/apps/shield check_35439928-bf3d-41d0-ac20-63c8b05f2354.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('35439928-bf3d-41d0-ac20-63c8b05f2354', 'pictographic-primitives/apps/shield check_35439928-bf3d-41d0-ac20-63c8b05f2354.svg'),)
PROFILE_SOURCE_KEYS = ('solo/shield-check',)
SOLO_SOURCE_ICON_IDS = ('shield-check',)
REFERENCE_EXPORT_SHA256 = '3c5eb57a8110eceb8f7e75e4e68dc9706319263a1dcf8f15d8b792878c03d30d'

class DrawingVariant2(Sub32):
    icon_id = 'shield-check-sub32-v2'
    variant_of = 'shield-check-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'apps'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Pointed shield crown, paired smooth lower sides and check. Construction reference: shield-check."""
        self.add_polyline('crown', (4, 7), (16, 2), (28, 7), (28, 17))
        self.add_bezier('bottom-r', (28, 17), ((28, 23), (22, 28), (16, 30)))
        self.add_bezier('bottom-l', (16, 30), ((10, 28), (4, 23), (4, 17)))
        self.add_line('left', (4, 17), (4, 7))
        self.add_contour('shield', 'bottom-r', 'bottom-l', 'left')
        self.relate('connect', 'shield', 'crown')
        self.add_polyline('check', (11, 16), (15, 20), (22, 13))

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
