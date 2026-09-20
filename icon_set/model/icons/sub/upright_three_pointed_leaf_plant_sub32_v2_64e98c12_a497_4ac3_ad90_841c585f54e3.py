"""Independent 32px profile of upright-three-pointed-leaf-plant.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '64e98c12-a497-4ac3-ad90-841c585f54e3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/decoration/batch-03/indoor plant_64e98c12-a497-4ac3-ad90-841c585f54e3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('64e98c12-a497-4ac3-ad90-841c585f54e3', 'pictographic-primitives/decoration/batch-03/indoor plant_64e98c12-a497-4ac3-ad90-841c585f54e3.svg'),)
PROFILE_SOURCE_KEYS = ('solo/upright-three-pointed-leaf-plant',)
SOLO_SOURCE_ICON_IDS = ('upright-three-pointed-leaf-plant',)
REFERENCE_EXPORT_SHA256 = '021c1106539d742f8906013ce84045fb696103114735549b1217d548397eff2f'

class DrawingVariant2(Sub32):
    icon_id = 'upright-three-pointed-leaf-plant-sub32-v2'
    variant_of = 'upright-three-pointed-leaf-plant-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'nature/plants'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Three pointed upright leaves seated in a tapered flowerpot with a shared rim. Construction reference: sprout."""
        self.add_bezier('left-outer', (9, 22), ((5, 18), (4, 13), (4, 8)))
        self.add_bezier('left-inner', (4, 8), ((8, 9), (10, 12), (12, 15)))
        self.add_bezier('center-l', (12, 15), ((12, 9), (14, 4), (16, 2)))
        self.add_bezier('center-r', (16, 2), ((18, 4), (20, 9), (20, 15)))
        self.add_bezier('right-inner', (20, 15), ((22, 12), (24, 9), (28, 8)))
        self.add_bezier('right-outer', (28, 8), ((28, 13), (27, 18), (23, 22)))
        self.add_contour('plant', 'left-outer', 'left-inner', 'center-l', 'center-r', 'right-inner', 'right-outer')
        self.add_polyline('pot', (8, 22), (24, 22), (22, 30), (10, 30), closed=True)
        self.relate('connect', 'plant', 'pot')

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
