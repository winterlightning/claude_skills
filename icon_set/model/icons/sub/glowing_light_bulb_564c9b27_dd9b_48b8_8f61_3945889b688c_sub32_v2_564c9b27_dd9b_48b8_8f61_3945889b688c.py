"""Independent 32px profile of glowing-light-bulb-564c9b27-dd9b-48b8-8f61-3945889b688c.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '564c9b27-dd9b-48b8-8f61-3945889b688c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/lights/light bulb 1_564c9b27-dd9b-48b8-8f61-3945889b688c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('564c9b27-dd9b-48b8-8f61-3945889b688c', 'pictographic-primitives/lights/light bulb 1_564c9b27-dd9b-48b8-8f61-3945889b688c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/glowing-light-bulb-564c9b27-dd9b-48b8-8f61-3945889b688c',)
SOLO_SOURCE_ICON_IDS = ('glowing-light-bulb-564c9b27-dd9b-48b8-8f61-3945889b688c',)
REFERENCE_EXPORT_SHA256 = 'b70d54d9fde4151a94a831f8c44d9ec9d8445f885cb4a5a8b8bbe7e4352a158d'

class DrawingVariant2(Sub32):
    icon_id = 'glowing-light-bulb-564c9b27-dd9b-48b8-8f61-3945889b688c-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/lighting'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Light bulb with closed rounded base, base divider and five separate rays. Construction reference: lightbulb."""
        self.add_arc('bulb-top', (9, 17), (23, 17), radius_x=7)
        self.add_bezier('bulb-r', (23, 17), ((23, 20), (20, 21), (20, 24)))
        self.add_line('base-r', (20, 24), (20, 26))
        self.add_arc('base-bottom', (20, 26), (12, 26), radius_x=4)
        self.add_line('base-l', (12, 26), (12, 24))
        self.add_bezier('bulb-l', (12, 24), ((12, 21), (9, 20), (9, 17)))
        self.add_contour('bulb', 'bulb-top', 'bulb-r', 'base-r', 'base-bottom', 'base-l', 'bulb-l', closed=True)
        self.add_line('divider', (12, 22), (20, 22))
        self.relate('connect', 'divider', 'bulb')
        for n, a, b in [('up', (16, 2), (16, 3)), ('ul', (4, 5), (5, 6)), ('ur', (28, 5), (27, 6)), ('left', (2, 14), (3, 14)), ('right', (29, 14), (30, 14))]:
            self.add_line(n, a, b)

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
