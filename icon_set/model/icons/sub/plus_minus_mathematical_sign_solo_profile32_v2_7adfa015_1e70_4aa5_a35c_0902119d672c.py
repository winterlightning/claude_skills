"""Independent 32px profile of plus-minus-mathematical-sign-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '7adfa015-1e70-4aa5-a35c-0902119d672c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/circle plus minus_7adfa015-1e70-4aa5-a35c-0902119d672c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7adfa015-1e70-4aa5-a35c-0902119d672c', 'pictographic-primitives/other/circle plus minus_7adfa015-1e70-4aa5-a35c-0902119d672c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/plus-minus-mathematical-sign-solo',)
SOLO_SOURCE_ICON_IDS = ('plus-minus-mathematical-sign-solo',)
REFERENCE_EXPORT_SHA256 = 'aa2095a0d08ddb7850de28a17e9ed9c92085ba2a4dc15064d4a5f0d1a4faf854'

class DrawingVariant2(Sub32):
    icon_id = 'plus-minus-mathematical-sign-solo-profile32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Circular frame, shared upper-left plus and lower-right minus, with rising diagonal slash. Construction reference: circle."""
        circle(self, 'frame', 16, 16, 14)
        self.add_line('plus-p1-r1-1', (10, 11), (12, 11))
        self.add_contour('plus-path-1-1', 'plus-p1-r1-1', closed=False)
        self.add_line('plus-p2-r1-1', (11, 10), (11, 12))
        self.add_contour('plus-path-2-1', 'plus-p2-r1-1', closed=False)
        self.add_line('minus-p1-r1-1', (20, 21), (22, 21))
        self.add_contour('minus-path-1-1', 'minus-p1-r1-1', closed=False)
        self.add_line('slash', (11, 21), (21, 11))

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
TYPEFACE_GLYPH_IDS = ('symbol-plus', 'symbol-hyphen')
