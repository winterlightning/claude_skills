"""Independent 32px profile of text-capital-letter-a-37012d29.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = '37012d29-357d-4e7a-9788-4fe102b86097'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/dist/text32/text-capital-letter-a-37012d29.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('37012d29-357d-4e7a-9788-4fe102b86097', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/a (text)_37012d29-357d-4e7a-9788-4fe102b86097.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-capital-letter-a-37012d29',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '25cf18d5525249db4d9a534bc3a4c2b9ea361a1f824dc3d4b7245e14ba7d9ab6'

class DrawingVariant2(TextSub32):
    icon_id = 'text-capital-letter-a-37012d29-sub32-v2'
    variant_of = 'text-capital-letter-a-37012d29-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 25
    text_ink_bounds = (0, 0, 24, 32)

    def build(self):
        """Shared typeface letter-a-uppercase; natural proportions, 32-unit ink height and integer fitted layout. Construction reference: icon_set/typeface/glyphs.json."""
        self.add_line('p1-r1-1', (2, 30), (11, 3))
        self.add_bezier('p1-r1-2', (11, 3), ((11.666666666666666, 1.6666666666666667), (12.333333333333334, 1.6666666666666667), (13, 3)))
        self.add_line('p1-r1-3', (13, 3), (22, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (6, 18), (18, 18))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)

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
TYPEFACE_GLYPH_IDS = ('letter-a-uppercase',)
