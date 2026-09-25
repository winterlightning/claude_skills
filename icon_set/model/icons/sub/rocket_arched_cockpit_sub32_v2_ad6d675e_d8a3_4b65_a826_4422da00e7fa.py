"""Independent 32px profile of rocket-arched-cockpit.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'ad6d675e-d8a3-4b65-a826-4422da00e7fa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/science/rocket base_ad6d675e-d8a3-4b65-a826-4422da00e7fa.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ad6d675e-d8a3-4b65-a826-4422da00e7fa', 'pictographic-primitives/science/rocket base_ad6d675e-d8a3-4b65-a826-4422da00e7fa.svg'),)
PROFILE_SOURCE_KEYS = ('solo/rocket-arched-cockpit',)
SOLO_SOURCE_ICON_IDS = ('rocket-arched-cockpit',)
REFERENCE_EXPORT_SHA256 = 'f6eac61df5c8a817c1883d5a14b1caadca7e83cd081424725738b914aa04f748'

class DrawingVariant2(Sub32):
    icon_id = 'rocket-arched-cockpit-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'science'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Pointed rocket body with integrated fins, cockpit mark and exhaust stem. Construction reference: rocket: pointed nose and broad integrated fins."""
        self.add_bezier('nose-right', (16, 2), ((20, 4), (26, 8), (26, 13)))
        self.add_polyline('lower', (26, 13), (26, 17), (30, 26), (2, 26), (6, 17), (6, 13))
        self.add_bezier('nose-left', (6, 13), ((6, 8), (12, 4), (16, 2)))
        self.relate('connect', 'nose-right', 'lower')
        self.relate('connect', 'nose-left', 'lower')
        self.relate('connect', 'nose-left', 'nose-right')
        self.add_line('cockpit', (16, 12), (16, 12))
        self.add_line('exhaust', (16, 26), (16, 30))
        self.relate('connect', 'exhaust', 'lower')

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
