"""Independent 32px profile of flame.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '949214a5-cd3d-46da-8416-617e71942aa0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/fire/flame_949214a5-cd3d-46da-8416-617e71942aa0.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('949214a5-cd3d-46da-8416-617e71942aa0', 'pictographic-primitives/fire/flame_949214a5-cd3d-46da-8416-617e71942aa0.svg'),)
PROFILE_SOURCE_KEYS = ('solo/flame',)
SOLO_SOURCE_ICON_IDS = ('flame',)
REFERENCE_EXPORT_SHA256 = '02bd12553efd78629895b3a8335281f6168608b2ee89ce0610a24695ceb51fe9'

class DrawingVariant2(Sub32):
    icon_id = 'flame-sub32-v2'
    variant_of = 'flame-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'fire'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """One continuous flame outline with curled crown and inward side notch. Construction reference: flame."""
        self.add_bezier('left-top', (4, 20), ((4, 11), (18, 11), (15, 2)))
        self.add_bezier('crown', (15, 2), ((25, 8), (25, 12), (22, 17)))
        self.add_bezier('notch', (22, 17), ((19, 22), (24, 22), (27, 17)))
        self.add_bezier('right', (27, 17), ((28, 20), (28, 21), (28, 23)))
        self.add_bezier('bottom-r', (28, 23), ((28, 27), (22, 30), (16, 30)))
        self.add_bezier('bottom-l', (16, 30), ((9, 30), (4, 26), (4, 20)))
        self.add_contour('flame', 'left-top', 'crown', 'notch', 'right', 'bottom-r', 'bottom-l', closed=True)

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
