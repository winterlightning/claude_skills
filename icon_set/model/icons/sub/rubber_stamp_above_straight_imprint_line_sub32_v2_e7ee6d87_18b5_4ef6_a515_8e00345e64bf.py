"""Independent 32px profile of rubber-stamp-above-straight-imprint-line.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'e7ee6d87-18b5-4ef6-a515-8e00345e64bf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/design/stamp_e7ee6d87-18b5-4ef6-a515-8e00345e64bf.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e7ee6d87-18b5-4ef6-a515-8e00345e64bf', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/stamp_e7ee6d87-18b5-4ef6-a515-8e00345e64bf.svg'),)
PROFILE_SOURCE_KEYS = ('solo/rubber-stamp-above-straight-imprint-line',)
SOLO_SOURCE_ICON_IDS = ('rubber-stamp-above-straight-imprint-line',)
REFERENCE_EXPORT_SHA256 = 'a154add09c811f63c87104e772c980c7d620f676cde61db262ff14b391d7a9c7'

class DrawingVariant2(Sub32):
    icon_id = 'rubber-stamp-above-straight-imprint-line-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/design'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Rounded rubber-stamp grip, curved shoulders, thick base and separate imprint line. Construction reference: stamp."""
        self.add_arc('grip-top', (10, 8), (22, 8), radius_x=6)
        self.add_bezier('grip-r', (22, 8), ((22, 12), (20, 13), (20, 14)))
        self.add_line('shoulder-r', (20, 14), (24, 14))
        self.add_arc('base-r', (24, 14), (28, 18), radius_x=4)
        self.add_polyline('base', (28, 18), (28, 22), (4, 22), (4, 18))
        self.add_arc('base-l', (4, 18), (8, 14), radius_x=4)
        self.add_line('shoulder-l', (8, 14), (12, 14))
        self.add_bezier('grip-l', (12, 14), ((12, 13), (10, 12), (10, 8)))
        self.add_contour('top', 'grip-top', 'grip-r', 'shoulder-r', 'base-r')
        self.add_contour('left', 'base-l', 'shoulder-l', 'grip-l')
        for a, b in [('base', 'top'), ('base', 'left'), ('left', 'top')]:
            self.relate('connect', a, b)
        self.add_line('imprint', (4, 30), (28, 30))

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
