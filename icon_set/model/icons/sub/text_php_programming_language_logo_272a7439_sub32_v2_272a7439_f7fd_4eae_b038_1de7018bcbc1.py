"""Independent 32px profile of text-php-programming-language-logo-272a7439.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = '272a7439-f7fd-4eae-b038-1de7018bcbc1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/dist/text32/text-php-programming-language-logo-272a7439.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('272a7439-f7fd-4eae-b038-1de7018bcbc1', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/php (text)_272a7439-f7fd-4eae-b038-1de7018bcbc1.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-php-programming-language-logo-272a7439',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'fe9665d95e2417283d4432f4d60d105a00ca834e4d373ca62654af0f0a5d0158'

class DrawingVariant2(TextSub32):
    icon_id = 'text-php-programming-language-logo-272a7439-sub32-v2'
    variant_of = 'text-php-programming-language-logo-272a7439-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 83
    text_ink_bounds = (0, 0, 82, 32)

    def build(self):
        """Shared typeface letter-p-uppercase, letter-h-uppercase, letter-p-uppercase; natural proportions, 32-unit ink height and integer fitted layout. Construction reference: icon_set/typeface/glyphs.json."""
        self.add_line('p1-r1-1', (2, 30), (2, 2))
        self.add_line('p1-r1-2', (2, 2), (12, 2))
        self.add_bezier('p1-r1-3', (12, 2), ((18, 2), (21, 6), (21, 9)))
        self.add_bezier('p1-r1-4', (21, 9), ((21, 13), (18, 17), (12, 17)))
        self.add_line('p1-r1-5', (12, 17), (2, 17))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (31, 2), (31, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (51, 2), (51, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (31, 16), (51, 16))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (61, 30), (61, 2))
        self.add_line('p5-r1-2', (61, 2), (71, 2))
        self.add_bezier('p5-r1-3', (71, 2), ((77, 2), (80, 6), (80, 9)))
        self.add_bezier('p5-r1-4', (80, 9), ((80, 13), (77, 17), (71, 17)))
        self.add_line('p5-r1-5', (71, 17), (61, 17))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', 'p5-r1-5', closed=False)

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
TYPEFACE_GLYPH_IDS = ('letter-p-uppercase', 'letter-h-uppercase', 'letter-p-uppercase')
