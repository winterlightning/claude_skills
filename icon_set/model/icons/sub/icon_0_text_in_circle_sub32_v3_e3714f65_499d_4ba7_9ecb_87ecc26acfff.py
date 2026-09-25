"""Independent 32px profile of icon-0-text-in-circle.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'e3714f65-499d-4ba7-9ecb-87ecc26acfff'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/0 text in circle_e3714f65-499d-4ba7-9ecb-87ecc26acfff.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e3714f65-499d-4ba7-9ecb-87ecc26acfff', 'pictographic-primitives/state/0 text in circle_e3714f65-499d-4ba7-9ecb-87ecc26acfff.svg'),)
PROFILE_SOURCE_KEYS = ('solo/icon-0-text-in-circle',)
SOLO_SOURCE_ICON_IDS = ('icon-0-text-in-circle',)
REFERENCE_EXPORT_SHA256 = '9a2a96442fa40bccaacddc40c716e980385c1b298dc4244b115d220e57fde623'

class DrawingVariant3(Sub32):
    icon_id = 'icon-0-text-in-circle-sub32-v3'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Circular frame around the shared digit-zero glyph, proportionally fitted to the interior. Construction reference: circle."""
        circle(self, 'frame', 16, 16, 14)
        self.add_bezier('p1-r1-1', (11, 13), ((11, 11), (13, 9), (16, 9)))
        self.add_bezier('p1-r1-2', (16, 9), ((19, 9), (21, 11), (21, 13)))
        self.add_line('p1-r1-3', (21, 13), (21, 19))
        self.add_bezier('p1-r1-4', (21, 19), ((21, 21), (19, 23), (16, 23)))
        self.add_bezier('p1-r1-5', (16, 23), ((13, 23), (11, 21), (11, 19)))
        self.add_line('p1-r1-6', (11, 19), (11, 13))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)

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
TYPEFACE_GLYPH_IDS = ('digit-0',)
