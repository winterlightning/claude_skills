"""Independent 32px profile of laptop-with-rounded-base.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'b3a5c634-3ab7-4cf8-9707-160623df0758'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/computers/batch-03/laptop_b3a5c634-3ab7-4cf8-9707-160623df0758.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b3a5c634-3ab7-4cf8-9707-160623df0758', 'pictographic-primitives/computers/batch-03/laptop_b3a5c634-3ab7-4cf8-9707-160623df0758.svg'), ('f99926f6-12c0-4ba6-aff3-e7bf08c23a81', 'pictographic-primitives/computers/batch-03/laptop_f99926f6-12c0-4ba6-aff3-e7bf08c23a81.svg'))
PROFILE_SOURCE_KEYS = ('solo/laptop-with-rounded-base',)
SOLO_SOURCE_ICON_IDS = ('laptop-with-rounded-base',)
REFERENCE_EXPORT_SHA256 = '075b9a342b75464a6f337a52bb11e757968334c1b3fc02351d60afa626ae1999'

class DrawingVariant2(Sub32):
    icon_id = 'laptop-with-rounded-base-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'computers'
    categories = ('computers', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Laptop screen with rounded upper corners and rounded base; one shared screen/base seam. Construction reference: laptop."""
        self.add_line('screen-l', (4, 20), (4, 7))
        self.add_arc('tl', (4, 7), (7, 4), radius_x=3)
        self.add_line('screen-top', (7, 4), (25, 4))
        self.add_arc('tr', (25, 4), (28, 7), radius_x=3)
        self.add_line('screen-r', (28, 7), (28, 20))
        self.add_contour('screen', 'screen-l', 'tl', 'screen-top', 'tr', 'screen-r')
        self.add_line('base-top', (2, 20), (30, 20))
        self.add_bezier('base-r', (30, 20), ((30, 25), (28, 28), (24, 28)))
        self.add_line('base-bottom', (24, 28), (8, 28))
        self.add_bezier('base-l', (8, 28), ((4, 28), (2, 25), (2, 20)))
        self.add_contour('base', 'base-top', 'base-r', 'base-bottom', 'base-l', closed=True)
        self.relate('connect', 'base', 'screen')

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
