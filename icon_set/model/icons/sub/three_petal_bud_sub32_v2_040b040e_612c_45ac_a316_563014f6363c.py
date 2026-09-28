"""Independent 32px profile of three-petal-bud.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '040b040e-612c-45ac-a316-563014f6363c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/nature/plant_040b040e-612c-45ac-a316-563014f6363c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('040b040e-612c-45ac-a316-563014f6363c', 'pictographic-primitives/nature/plant_040b040e-612c-45ac-a316-563014f6363c.svg'), ('a1b3fc44-cc28-4906-bcdc-64d15a515143', 'pictographic-primitives/nature/plant_a1b3fc44-cc28-4906-bcdc-64d15a515143.svg'))
PROFILE_SOURCE_KEYS = ('solo/three-petal-bud', 'solo/three-petal-bud-alternate')
SOLO_SOURCE_ICON_IDS = ('three-petal-bud', 'three-petal-bud-alternate')
REFERENCE_EXPORT_SHA256 = 'ca34f41c0fa1a193fbea671268c7ff351a91c65cb473e17c65027700acc98b7f'

class DrawingVariant2(Sub32):
    icon_id = 'three-petal-bud-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'nature'
    categories = ('nature', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Three-petal bud with pointed center leaf, two side petals, visible internal boundaries and short stem. Construction reference: flower-2."""
        self.add_bezier('center-l-top', (16, 2), ((13, 5), (11, 8), (11, 12)))
        self.add_bezier('center-l-base', (11, 12), ((11, 18), (13, 22), (16, 25)))
        self.add_bezier('center-r-base', (16, 25), ((19, 22), (21, 18), (21, 12)))
        self.add_bezier('center-r-top', (21, 12), ((21, 8), (19, 5), (16, 2)))
        self.add_contour('center', 'center-l-top', 'center-l-base', 'center-r-base', 'center-r-top', closed=True)
        for name, a, c1, c2, b, c3, c4 in [('left', (4, 6), (4, 15), (6, 21), (16, 25), (7, 8), (9, 10)), ('right', (28, 6), (28, 15), (26, 21), (16, 25), (25, 8), (23, 10))]:
            self.add_bezier(name + '-outer', a, (c1, c2, b))
            self.add_bezier(name + '-upper', a, (c3, c4, (11 if name == 'left' else 21, 12)))
            self.relate('connect', name + '-outer', name + '-upper')
            self.relate('connect', name + '-outer', 'center')
            self.relate('connect', name + '-upper', 'center')
        self.relate('connect', 'left-outer', 'right-outer')
        self.add_line('stem', (16, 25), (16, 30))
        self.relate('connect', 'stem', 'center')
        self.relate('connect', 'stem', 'left-outer')
        self.relate('connect', 'stem', 'right-outer')

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
