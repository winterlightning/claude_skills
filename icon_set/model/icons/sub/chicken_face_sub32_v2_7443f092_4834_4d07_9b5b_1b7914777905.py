# Independent repair; parent preserved.
"""Independent 32px profile of chicken-face.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '7443f092-4834-4d07-9b5b-1b7914777905'
SOURCE_PATH = 'pictographic-primitives/animals/chicken_7443f092-4834-4d07-9b5b-1b7914777905.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7443f092-4834-4d07-9b5b-1b7914777905', 'pictographic-primitives/animals/chicken_7443f092-4834-4d07-9b5b-1b7914777905.svg'),)
PROFILE_SOURCE_KEYS = ('solo/chicken-face',)
SOLO_SOURCE_ICON_IDS = ('chicken-face',)
REFERENCE_EXPORT_SHA256 = '9bbc5a9688cae7020358725b5ea130c8ae8e847164c2006b396f805bd598484b'

class RepairVariant(Sub32):
    variant_label = 'Centerline and source fidelity repair'
    variant_of = 'chicken-face-sub32'
    icon_id = 'chicken-face-sub32-v2'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'animals'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('head-top', (4, 20), (28, 20), radius_x=12, radius_y=10)
        self.add_line('right', (28, 20), (28, 30))
        self.add_line('left', (4, 30), (4, 20))
        self.add_contour('head', 'left', 'head-top', 'right')
        self.add_bezier('comb-left', (14, 10), ((12, 7), (12, 2), (16, 2)))
        self.add_bezier('comb-right', (16, 2), ((20, 2), (19, 7), (18, 10)))
        self.add_contour('comb', 'comb-left', 'comb-right')
        self.relate('connect', 'head', 'comb')
        for x in (11, 21):
            self.add_dot(f'eye-{x}', (x, 18))
        self.add_polyline('beak', (16, 18), (22, 24), (16, 30), (10, 24), closed=True)

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
REPAIR_PLAN = 'Chicken head with original closed diamond beak, both eyes and comb.'
CONSTRUCTION_REFERENCE = 'baby'
