"""Independent 32px profile of side-text-4fd52187.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = '4fd52187-1c97-4d8d-8d4a-93db88e7190c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/dist/text32/side-text-4fd52187.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4fd52187-1c97-4d8d-8d4a-93db88e7190c', 'icon_set/dist/gallery/combination-originals/4fd52187-1c97-4d8d-8d4a-93db88e7190c.svg'),)
PROFILE_SOURCE_KEYS = ('text/side-text-4fd52187',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'd4fb5af9e3e61ada488adc671a16034c63a8c62efdb9df0d630ada62ed80e35c'

class DrawingVariant2(TextSub32):
    icon_id = 'side-text-4fd52187-sub32-v2'
    variant_of = 'side-text-4fd52187-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 52
    text_ink_bounds = (0, 0, 51, 32)

    def build(self):
        """Shared typeface digit-0, symbol-percent; natural proportions, 32-unit ink height and grid-fitted layout. Construction reference: icon_set/typeface/glyphs.json."""
        self.add_bezier('p1-r1-1', (2, 10), ((2, 6), (6, 3), (11, 3)))
        self.add_bezier('p1-r1-2', (11, 3), ((17, 3), (21, 6), (21, 10)))
        self.add_line('p1-r1-3', (21, 10), (21, 22))
        self.add_bezier('p1-r1-4', (21, 22), ((21, 26), (17, 29), (11, 29)))
        self.add_bezier('p1-r1-5', (11, 29), ((6, 29), (2, 26), (2, 22)))
        self.add_line('p1-r1-6', (2, 22), (2, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (29, 30), (49, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_bezier('p3-r1-1', (29, 7), ((29, 4), (31, 2), (33, 2)))
        self.add_bezier('p3-r1-2', (33, 2), ((35, 2), (37, 4), (37, 7)))
        self.add_bezier('p3-r1-3', (37, 7), ((37, 10), (35, 13), (33, 13)))
        self.add_bezier('p3-r1-4', (33, 13), ((31, 13), (29, 10), (29, 7)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_bezier('p4-r1-1', (41, 25), ((41, 22), (43, 19), (45, 19)))
        self.add_bezier('p4-r1-2', (45, 19), ((47, 19), (49, 22), (49, 25)))
        self.add_bezier('p4-r1-3', (49, 25), ((49, 28), (47, 30), (45, 30)))
        self.add_bezier('p4-r1-4', (45, 30), ((43, 30), (41, 28), (41, 25)))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)

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
TYPEFACE_GLYPH_IDS = ('digit-0', 'symbol-percent')
