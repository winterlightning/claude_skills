"""Independent 32px profile of thumbs-up-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '159051f0-87aa-4c05-9b9f-53abd2ca05ef'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/thumbs up_159051f0-87aa-4c05-9b9f-53abd2ca05ef.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('159051f0-87aa-4c05-9b9f-53abd2ca05ef', 'pictographic-primitives/symbol/thumbs up_159051f0-87aa-4c05-9b9f-53abd2ca05ef.svg'), ('5680cb28-5cf7-4d7c-98be-ae372bac6440', 'pictographic-primitives/symbol/thumbs up_5680cb28-5cf7-4d7c-98be-ae372bac6440.svg'))
PROFILE_SOURCE_KEYS = ('solo/thumbs-up-symbol', 'solo/thumbs-up-5680cb28')
SOLO_SOURCE_ICON_IDS = ('thumbs-up-symbol', 'thumbs-up-5680cb28')
REFERENCE_EXPORT_SHA256 = 'fef39793b900339390a7f350b1a8d2cf9da5c5ce4dded16bb603b2155ee5e562'

class DrawingVariant2(Sub32):
    icon_id = 'thumbs-up-symbol-sub32-v2'
    variant_of = 'thumbs-up-symbol-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Thumbs-up hand with cuff, raised rounded thumb and three knuckle scallops. Construction reference: thumbs-up."""
        self.add_polyline('cuff', (2, 16), (10, 16), (10, 30), (2, 30), closed=True)
        self.add_bezier('palm-rise', (10, 16), ((14, 12), (17, 8), (17, 4)))
        self.add_bezier('thumb', (17, 4), ((17, 2), (18, 2), (19, 2)))
        self.add_bezier('thumb-round', (19, 2), ((21, 2), (22, 3), (22, 5)))
        self.add_bezier('thumb-tip', (22, 5), ((24, 7), (22, 10), (21, 12)))
        self.add_line('fingers-top', (21, 12), (27, 12))
        self.add_arc('knuckle-1', (27, 12), (27, 18), radius_x=3)
        self.add_arc('knuckle-2', (27, 18), (27, 24), radius_x=3)
        self.add_arc('knuckle-3', (27, 24), (24, 30), radius_x=5)
        self.add_line('base', (24, 30), (10, 30))
        self.add_contour('hand', 'palm-rise', 'thumb', 'thumb-round', 'thumb-tip', 'fingers-top', 'knuckle-1', 'knuckle-2', 'knuckle-3', 'base')
        self.relate('connect', 'hand', 'cuff')

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
