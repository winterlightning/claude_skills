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

class DrawingVariant3(TextSub32):
    icon_id = 'side-text-4fd52187-sub32-v3'
    variant_of = 'side-text-4fd52187-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 53
    text_ink_bounds = (0, 0, 53, 32)

    def build(self):
        """Zero percent from the existing shared glyphs. Construction reference: shared typeface."""
        self.add_bezier('g0-p1-r1-1', (2, 10), ((2, 6), (6, 3), (11, 3)))
        self.add_bezier('g0-p1-r1-2', (11, 3), ((17, 3), (21, 6), (21, 10)))
        self.add_line('g0-p1-r1-3', (21, 10), (21, 22))
        self.add_bezier('g0-p1-r1-4', (21, 22), ((21, 26), (17, 29), (11, 29)))
        self.add_bezier('g0-p1-r1-5', (11, 29), ((6, 29), (2, 26), (2, 22)))
        self.add_line('g0-p1-r1-6', (2, 22), (2, 10))
        self.add_contour('g0-path-1-1', 'g0-p1-r1-1', 'g0-p1-r1-2', 'g0-p1-r1-3', 'g0-p1-r1-4', 'g0-p1-r1-5', 'g0-p1-r1-6', closed=False)
        self.add_line('g1-p1-r1-1', (30, 30), (50, 2))
        self.add_contour('g1-path-1-1', 'g1-p1-r1-1', closed=False)
        self.add_bezier('g1-p2-r1-1', (29, 7), ((29, 4), (31, 2), (33, 2)))
        self.add_bezier('g1-p2-r1-2', (33, 2), ((35, 2), (37, 4), (37, 7)))
        self.add_bezier('g1-p2-r1-3', (37, 7), ((37, 10), (35, 13), (33, 13)))
        self.add_bezier('g1-p2-r1-4', (33, 13), ((31, 13), (29, 10), (29, 7)))
        self.add_contour('g1-path-2-1', 'g1-p2-r1-1', 'g1-p2-r1-2', 'g1-p2-r1-3', 'g1-p2-r1-4', closed=False)
        self.add_bezier('g1-p3-r1-1', (43, 25), ((43, 22), (45, 19), (47, 19)))
        self.add_bezier('g1-p3-r1-2', (47, 19), ((49, 19), (51, 22), (51, 25)))
        self.add_bezier('g1-p3-r1-3', (51, 25), ((51, 28), (49, 30), (47, 30)))
        self.add_bezier('g1-p3-r1-4', (47, 30), ((45, 30), (43, 28), (43, 25)))
        self.add_contour('g1-path-3-1', 'g1-p3-r1-1', 'g1-p3-r1-2', 'g1-p3-r1-3', 'g1-p3-r1-4', closed=False)

def box(s, n, l, t, r, b, k=3):
    if k == 0:
        s.add_polyline(n, (l, t), (r, t), (r, b), (l, b), (l, t))
        return
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
