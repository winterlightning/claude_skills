"""Independent 32px profile of user-profile.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '3352ce5f-f0e1-4497-86c8-0c433016cab6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/profile_3352ce5f-f0e1-4497-86c8-0c433016cab6.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3352ce5f-f0e1-4497-86c8-0c433016cab6', 'pictographic-primitives/symbol/profile_3352ce5f-f0e1-4497-86c8-0c433016cab6.svg'),)
PROFILE_SOURCE_KEYS = ('solo/user-profile',)
SOLO_SOURCE_ICON_IDS = ('user-profile',)
REFERENCE_EXPORT_SHA256 = '8ff20e505b1112f40db5c43684fe6c3818fac4cce051ee76f31656a1c12c378c'

class DrawingVariant2(Sub32):
    icon_id = 'user-profile-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Circular user head and open curved shoulders with exact four-unit ink gap. Construction reference: user."""
        head_cy = 8
        head_radius = 6
        body_top = head_cy + head_radius + 8
        circle(self, 'head', 16, head_cy, head_radius)
        self.add_arc('shoulders', (4, 30), (28, 30), radius_x=12, radius_y=30 - body_top)

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
