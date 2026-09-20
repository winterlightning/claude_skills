"""Independent 32px profile of side-text-259c0878.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = '259c0878-528e-42fb-8d9f-56fe04a84b03'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/dist/text32/side-text-259c0878.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('259c0878-528e-42fb-8d9f-56fe04a84b03', 'icon_set/dist/gallery/combination-originals/259c0878-528e-42fb-8d9f-56fe04a84b03.svg'),)
PROFILE_SOURCE_KEYS = ('text/side-text-259c0878',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '7d73023e55ea0339c8806a39d5a0673a19066453881a7bcd0ab8904f4e188d50'

class DrawingVariant2(TextSub32):
    icon_id = 'side-text-259c0878-sub32-v2'
    variant_of = 'side-text-259c0878-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 51
    text_ink_bounds = (0, 0, 50, 32)

    def build(self):
        """Shared typeface letter-c-uppercase, digit-5; natural proportions, 32-unit ink height and integer fitted layout. Construction reference: icon_set/typeface/glyphs.json."""
        self.add_bezier('p1-r1-1', (19, 6), ((17, 3), (15, 2), (12, 2)))
        self.add_bezier('p1-r1-2', (12, 2), ((7, 2), (2, 8), (2, 16)))
        self.add_bezier('p1-r1-3', (2, 16), ((2, 24), (7, 30), (12, 30)))
        self.add_bezier('p1-r1-4', (12, 30), ((15, 30), (17, 29), (19, 26)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (46, 2), (30, 2))
        self.add_bezier('p2-r1-2', (30, 2), ((29, 2), (29, 2), (29, 3)))
        self.add_line('p2-r1-3', (29, 3), (29, 13))
        self.add_bezier('p2-r1-4', (29, 13), ((29, 13), (29, 14), (30, 14)))
        self.add_line('p2-r1-5', (30, 14), (40, 14))
        self.add_bezier('p2-r1-6', (40, 14), ((45, 14), (48, 18), (48, 22)))
        self.add_bezier('p2-r1-7', (48, 22), ((48, 24), (48, 26), (46, 28)))
        self.add_bezier('p2-r1-8', (46, 28), ((45, 29), (42, 30), (40, 30)))
        self.add_line('p2-r1-9', (40, 30), (30, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', closed=False)

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
TYPEFACE_GLYPH_IDS = ('letter-c-uppercase', 'digit-5')
