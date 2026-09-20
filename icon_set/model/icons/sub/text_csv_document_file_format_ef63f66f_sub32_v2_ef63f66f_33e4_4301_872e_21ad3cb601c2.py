"""Independent 32px profile of text-csv-document-file-format-ef63f66f.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = 'ef63f66f-33e4-4301-872e-21ad3cb601c2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/dist/text32/text-csv-document-file-format-ef63f66f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ef63f66f-33e4-4301-872e-21ad3cb601c2', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/CSV (text)_ef63f66f-33e4-4301-872e-21ad3cb601c2.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-csv-document-file-format-ef63f66f',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '472712d2f4953bd4249facf4d238de99cc84129ab0ee66a6601ffa68d56e4458'

class DrawingVariant2(TextSub32):
    icon_id = 'text-csv-document-file-format-ef63f66f-sub32-v2'
    variant_of = 'text-csv-document-file-format-ef63f66f-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 81
    text_ink_bounds = (0, 0, 80, 32)

    def build(self):
        """Shared typeface letter-c-uppercase, letter-s-uppercase, letter-v-uppercase; natural proportions, 32-unit ink height and integer fitted layout. Construction reference: icon_set/typeface/glyphs.json."""
        self.add_bezier('p1-r1-1', (19, 6), ((17, 3), (15, 2), (12, 2)))
        self.add_bezier('p1-r1-2', (12, 2), ((7, 2), (2, 8), (2, 16)))
        self.add_bezier('p1-r1-3', (2, 16), ((2, 24), (7, 30), (12, 30)))
        self.add_bezier('p1-r1-4', (12, 30), ((15, 30), (17, 29), (19, 26)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_bezier('p2-r1-1', (47, 6), ((46, 3), (42, 2), (39, 2)))
        self.add_bezier('p2-r1-2', (39, 2), ((35, 2), (31, 4), (30, 9)))
        self.add_bezier('p2-r1-3', (30, 9), ((30, 9), (30, 9), (30, 10)))
        self.add_bezier('p2-r1-4', (30, 10), ((30, 17), (47, 13), (47, 22)))
        self.add_bezier('p2-r1-5', (47, 22), ((47, 22), (47, 22), (47, 23)))
        self.add_bezier('p2-r1-6', (47, 23), ((47, 28), (43, 30), (38, 30)))
        self.add_bezier('p2-r1-7', (38, 30), ((34, 30), (31, 29), (29, 26)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', closed=False)
        self.add_line('p3-r1-1', (57, 2), (66, 28))
        self.add_bezier('p3-r1-2', (66, 28), ((66.66666666666667, 29.333333333333332), (67.33333333333333, 30), (68, 30)))
        self.add_bezier('p3-r1-3', (68, 30), ((68, 30), (68.33333333333333, 29.333333333333332), (69, 28)))
        self.add_line('p3-r1-4', (69, 28), (78, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)

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
TYPEFACE_GLYPH_IDS = ('letter-c-uppercase', 'letter-s-uppercase', 'letter-v-uppercase')
