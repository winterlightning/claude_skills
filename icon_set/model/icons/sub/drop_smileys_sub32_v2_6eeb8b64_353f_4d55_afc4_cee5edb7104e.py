"""Independent 32px profile of drop-smileys.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '6eeb8b64-353f-4d55-afc4-cee5edb7104e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/smileys/drop_6eeb8b64-353f-4d55-afc4-cee5edb7104e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6eeb8b64-353f-4d55-afc4-cee5edb7104e', 'pictographic-primitives/smileys/drop_6eeb8b64-353f-4d55-afc4-cee5edb7104e.svg'), ('a1bd3645-c186-44d1-a3a2-2ec8e3d10a1b', 'pictographic-primitives/smileys/drop_a1bd3645-c186-44d1-a3a2-2ec8e3d10a1b.svg'))
PROFILE_SOURCE_KEYS = ('solo/drop-smileys', 'solo/drop-a1bd3645')
SOLO_SOURCE_ICON_IDS = ('drop-smileys', 'drop-a1bd3645')
REFERENCE_EXPORT_SHA256 = 'afc6655d1a83856b44a22f8f0b018899ae899d9fad8607c25ca680fd7e862457'

class DrawingVariant2(Sub32):
    icon_id = 'drop-smileys-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'smileys'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Water drop with curved lower highlight; mirrored outer sides. Construction reference: droplet."""
        self.add_bezier('upper-r', (16, 2), ((21, 7), (28, 15), (28, 20)))
        self.add_arc('bottom', (28, 20), (4, 20), radius_x=12, radius_y=10)
        self.add_bezier('upper-l', (4, 20), ((4, 15), (11, 7), (16, 2)))
        self.add_contour('drop', 'upper-r', 'bottom', 'upper-l', closed=True)
        self.add_arc('highlight', (21, 18), (16, 23), radius_x=5)

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
