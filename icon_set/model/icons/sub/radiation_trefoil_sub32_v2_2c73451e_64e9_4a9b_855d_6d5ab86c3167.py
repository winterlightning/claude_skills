"""Independent 32px profile of radiation-trefoil.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '2c73451e-64e9-4a9b-855d-6d5ab86c3167'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/nuclear energy_2c73451e-64e9-4a9b-855d-6d5ab86c3167.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2c73451e-64e9-4a9b-855d-6d5ab86c3167', 'pictographic-primitives/symbol/nuclear energy_2c73451e-64e9-4a9b-855d-6d5ab86c3167.svg'), ('db4b8c72-f358-486f-9136-75181808b594', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/radioactive_db4b8c72-f358-486f-9136-75181808b594.svg'))
PROFILE_SOURCE_KEYS = ('solo/radiation-trefoil', 'solo/radiation-trefoil-with-center-stroke')
SOLO_SOURCE_ICON_IDS = ('radiation-trefoil', 'radiation-trefoil-with-center-stroke')
REFERENCE_EXPORT_SHA256 = '03ce75d6b3cec85b8419b496dfcfa9a6c5846028180055c5fbc33b0e971713c8'

class DrawingVariant2(Sub32):
    icon_id = 'radiation-trefoil-sub32-v2'
    variant_of = 'radiation-trefoil-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Three separate rounded annular radiation sectors and one central dot. Construction reference: radiation."""
        self.add_bezier('left-outer', (8, 2), ((4, 5), (2, 10), (2, 16)))
        self.add_line('left-base', (2, 16), (9, 16))
        self.add_arc('left-inner', (9, 16), (12, 10), radius_x=7)
        self.add_line('left-tip', (12, 10), (8, 2))
        self.add_contour('left', 'left-outer', 'left-base', 'left-inner', 'left-tip', closed=True)
        self.add_bezier('right-outer', (30, 16), ((30, 10), (28, 5), (24, 2)))
        self.add_line('right-tip', (24, 2), (20, 10))
        self.add_arc('right-inner', (20, 10), (23, 16), radius_x=7)
        self.add_line('right-base', (23, 16), (30, 16))
        self.add_contour('right', 'right-outer', 'right-tip', 'right-inner', 'right-base', closed=True)
        self.add_bezier('lower-inner', (12, 22), ((14, 23), (18, 23), (20, 22)))
        self.add_line('lower-right', (20, 22), (24, 27))
        self.add_arc('lower-outer', (24, 27), (8, 27), radius_x=8, radius_y=3)
        self.add_line('lower-left', (8, 27), (12, 22))
        self.add_contour('lower', 'lower-inner', 'lower-right', 'lower-outer', 'lower-left', closed=True)
        self.add_dot('center', (16, 16))

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
