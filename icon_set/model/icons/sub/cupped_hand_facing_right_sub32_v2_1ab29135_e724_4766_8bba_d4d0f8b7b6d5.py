"""Independent 32px profile of cupped-hand-facing-right.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '1ab29135-e724-4766-8bba-d4d0f8b7b6d5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/business/begging hand ask_1ab29135-e724-4766-8bba-d4d0f8b7b6d5.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1ab29135-e724-4766-8bba-d4d0f8b7b6d5', 'pictographic-primitives/business/begging hand ask_1ab29135-e724-4766-8bba-d4d0f8b7b6d5.svg'),)
PROFILE_SOURCE_KEYS = ('solo/cupped-hand-facing-right',)
SOLO_SOURCE_ICON_IDS = ('cupped-hand-facing-right',)
REFERENCE_EXPORT_SHA256 = 'b826b683ec4ccced4119d52af613d4e90985586549ee2795fd3c8791e94c61e6'

class DrawingVariant2(Sub32):
    icon_id = 'cupped-hand-facing-right-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'business'
    categories = ('business', 'state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Cupped hand with rounded thumb, raised fingertips, palm and wrist; branch at the thumb extreme prevents crossing centerlines. Construction reference: hand-coins."""
        self.add_bezier('upper-wrist', (2, 10), ((6, 8), (8, 4), (12, 4)))
        self.add_bezier('thumb-top', (12, 4), ((15, 4), (16, 7), (18, 8)))
        self.add_arc('thumb-upper', (18, 8), (22, 12), radius_x=4)
        self.add_line('fingers', (22, 12), (28, 10))
        self.add_bezier('finger-tip', (28, 10), ((29, 9), (30, 10), (30, 13)))
        self.add_bezier('palm-right', (30, 13), ((30, 20), (23, 28), (16, 28)))
        self.add_bezier('palm-left', (16, 28), ((10, 28), (8, 22), (2, 22)))
        self.add_line('wrist', (2, 22), (2, 10))
        self.add_contour('outline', 'upper-wrist', 'thumb-top', 'thumb-upper', 'fingers', 'finger-tip', 'palm-right', 'palm-left', 'wrist', closed=True)
        self.add_arc('thumb-lower', (22, 12), (18, 16), radius_x=4)
        self.add_line('crease', (18, 16), (12, 13))
        self.add_contour('thumb', 'thumb-lower', 'crease')
        self.relate('connect', 'outline', 'thumb')

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
