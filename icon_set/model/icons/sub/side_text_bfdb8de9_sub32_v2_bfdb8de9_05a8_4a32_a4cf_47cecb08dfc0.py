"""Independent 32px profile of side-text-bfdb8de9.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = 'bfdb8de9-05a8-4a32-a4cf-47cecb08dfc0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/dist/text32/side-text-bfdb8de9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bfdb8de9-05a8-4a32-a4cf-47cecb08dfc0', 'icon_set/dist/gallery/combination-originals/bfdb8de9-05a8-4a32-a4cf-47cecb08dfc0.svg'),)
PROFILE_SOURCE_KEYS = ('text/side-text-bfdb8de9',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'ecffe1ed2f8f656c3322c409cc2a94b2e3e17dd1ab9092606cec7857b39c0dda'

class DrawingVariant2(TextSub32):
    icon_id = 'side-text-bfdb8de9-sub32-v2'
    variant_of = 'side-text-bfdb8de9-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 105
    text_ink_bounds = (0, 0, 105, 32)

    def build(self):
        """Shared typeface letter-c-uppercase, letter-c-uppercase, letter-p-uppercase, letter-a-uppercase; natural proportions, 32-unit ink height and grid-fitted layout. Construction reference: icon_set/typeface/glyphs.json."""
        self.add_bezier('p1-r1-1', (19, 6), ((17, 3), (15, 2), (12, 2)))
        self.add_bezier('p1-r1-2', (12, 2), ((7, 2), (2, 8), (2, 16)))
        self.add_bezier('p1-r1-3', (2, 16), ((2, 24), (7, 30), (12, 30)))
        self.add_bezier('p1-r1-4', (12, 30), ((15, 30), (17, 29), (19, 26)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_bezier('p2-r1-1', (45, 6), ((43, 3), (41, 2), (38, 2)))
        self.add_bezier('p2-r1-2', (38, 2), ((33, 2), (28, 8), (28, 16)))
        self.add_bezier('p2-r1-3', (28, 16), ((28, 24), (33, 30), (38, 30)))
        self.add_bezier('p2-r1-4', (38, 30), ((41, 30), (43, 29), (45, 26)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (54, 30), (54, 2))
        self.add_line('p3-r1-2', (54, 2), (64, 2))
        self.add_bezier('p3-r1-3', (64, 2), ((70, 2), (73, 6), (73, 9)))
        self.add_bezier('p3-r1-4', (73, 9), ((73, 13), (70, 17), (64, 17)))
        self.add_line('p3-r1-5', (64, 17), (54, 17))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.add_line('p4-r1-1', (82, 30), (91, 3))
        self.add_bezier('p4-r1-2', (91, 3), ((91.66666666666667, 2.3333333333333335), (92, 2), (92, 2)))
        self.add_bezier('p4-r1-3', (92, 2), ((92.66666666666667, 2), (93.33333333333333, 2.3333333333333335), (94, 3)))
        self.add_line('p4-r1-4', (94, 3), (103, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.add_line('p5-r1-1', (86, 18), (99, 18))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)

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
TYPEFACE_GLYPH_IDS = ('letter-c-uppercase', 'letter-c-uppercase', 'letter-p-uppercase', 'letter-a-uppercase')
