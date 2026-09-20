"""Independent 32px profile of dollar.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = '2c47b147-c2f7-4c49-8513-824a167aa784'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/dollar_2c47b147-c2f7-4c49-8513-824a167aa784.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2c47b147-c2f7-4c49-8513-824a167aa784', 'pictographic-primitives/symbol/dollar_2c47b147-c2f7-4c49-8513-824a167aa784.svg'), ('7930e153-2438-44ec-8db7-960bb9aa10cc', 'pictographic-primitives/state/dollar sign_7930e153-2438-44ec-8db7-960bb9aa10cc.svg'))
PROFILE_SOURCE_KEYS = ('solo/dollar', 'solo/dollar-sign')
SOLO_SOURCE_ICON_IDS = ('dollar', 'dollar-sign')
REFERENCE_EXPORT_SHA256 = 'eec24736fc812de2d9f5ca8cd10e1c2dcdd65a51e04f3ae8065466bebe6bfca7'

class DrawingVariant2(TextSub32):
    icon_id = 'dollar-sub32-v2'
    variant_of = 'dollar-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 20
    text_ink_bounds = (0, 0, 19, 32)

    def build(self):
        """Shared typeface symbol-dollar; natural proportions, 32-unit ink height and grid-fitted layout. Construction reference: icon_set/typeface/glyphs.json."""
        self.add_bezier('p1-r1-1', (17, 8), ((16, 6), (13, 5), (10, 5)))
        self.add_bezier('p1-r1-2', (10, 5), ((7, 5), (3, 7), (3, 11)))
        self.add_bezier('p1-r1-3', (3, 11), ((3, 11), (3, 11), (3, 11)))
        self.add_bezier('p1-r1-4', (3, 11), ((3, 18), (17, 14), (17, 21)))
        self.add_bezier('p1-r1-5', (17, 21), ((17, 22), (17, 22), (17, 22)))
        self.add_bezier('p1-r1-6', (17, 22), ((17, 26), (13, 28), (10, 28)))
        self.add_bezier('p1-r1-7', (10, 28), ((6, 28), (3, 27), (2, 25)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (10, 2), (10, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate('connect', 'path-1-1', 'path-2-1')

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
TYPEFACE_GLYPH_IDS = ('symbol-dollar',)
