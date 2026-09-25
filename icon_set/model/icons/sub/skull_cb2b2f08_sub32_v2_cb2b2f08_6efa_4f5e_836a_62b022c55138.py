"""Independent 32px profile of skull-cb2b2f08.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'cb2b2f08-6efa-4f5e-836a-62b022c55138'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/skull_cb2b2f08-6efa-4f5e-836a-62b022c55138.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('cb2b2f08-6efa-4f5e-836a-62b022c55138', 'pictographic-primitives/interface-essential/skull_cb2b2f08-6efa-4f5e-836a-62b022c55138.svg'),)
PROFILE_SOURCE_KEYS = ('solo/skull-cb2b2f08',)
SOLO_SOURCE_ICON_IDS = ('skull-cb2b2f08',)
REFERENCE_EXPORT_SHA256 = '52150fccc150717127a6ce745013d819258f1bd0fadf2055b41c84a09f006ed2'

class DrawingVariant2(Sub32):
    icon_id = 'skull-cb2b2f08-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    categories = ('interface-essential', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Domed skull, two eye dots, paired jaw shoulders and central tooth division. Construction reference: skull."""
        self.add_arc('crown', (2, 16), (30, 16), radius_x=14)
        self.add_bezier('right-cheek', (30, 16), ((30, 21), (25, 20), (25, 24)))
        self.add_line('right-jaw', (25, 24), (25, 27))
        self.add_arc('right-corner', (25, 27), (22, 30), radius_x=3)
        self.add_line('chin', (22, 30), (10, 30))
        self.add_arc('left-corner', (10, 30), (7, 27), radius_x=3)
        self.add_line('left-jaw', (7, 27), (7, 24))
        self.add_bezier('left-cheek', (7, 24), ((7, 20), (2, 21), (2, 16)))
        self.add_contour('skull', 'crown', 'right-cheek', 'right-jaw', 'right-corner', 'chin', 'left-corner', 'left-jaw', 'left-cheek', closed=True)
        for x in (10, 22):
            self.add_dot(f'eye-{x}', (x, 15))
        self.add_line('tooth', (16, 24), (16, 30))
        self.relate('connect', 'tooth', 'skull')

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
