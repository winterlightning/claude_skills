"""Independent 32px profile of text-dwg-cad-file-format-26e20867.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = '26e20867-fec6-496d-91f2-39291a2d0fc6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/dwg (text)_26e20867-fec6-496d-91f2-39291a2d0fc6.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('26e20867-fec6-496d-91f2-39291a2d0fc6', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/dwg (text)_26e20867-fec6-496d-91f2-39291a2d0fc6.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-dwg-cad-file-format-26e20867',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '04e95afdc2e5b7af22d65df1e2229ad17bda8bb5cdb8fa98a77ae6b3f6ae7130'

class DrawingVariant2(TextSub32):
    icon_id = 'text-dwg-cad-file-format-26e20867-sub32-v2'
    variant_of = 'text-dwg-cad-file-format-26e20867-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 93
    text_ink_bounds = (0, 0, 92, 32)

    def build(self):
        """Shared typeface letter-d-uppercase, letter-w-uppercase, letter-g-uppercase at 32px ink height and natural width. Construction reference: shared typeface."""
        self.add_line('p1-r1-1', (2, 2), (10, 2))
        self.add_bezier('p1-r1-2', (10, 2), ((18, 2), (21, 9), (21, 16)))
        self.add_bezier('p1-r1-3', (21, 16), ((21, 23), (18, 30), (10, 30)))
        self.add_line('p1-r1-4', (10, 30), (2, 30))
        self.add_line('p1-r1-5', (2, 30), (2, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (31, 2), (37, 28))
        self.add_bezier('p2-r1-2', (37, 28), ((37.666666666666664, 30.666666666666668), (38.333333333333336, 30.666666666666668), (39, 28)))
        self.add_line('p2-r1-3', (39, 28), (45, 4))
        self.add_bezier('p2-r1-4', (45, 4), ((45.666666666666664, 2), (46.333333333333336, 2), (47, 4)))
        self.add_line('p2-r1-5', (47, 4), (53, 28))
        self.add_bezier('p2-r1-6', (53, 28), ((53.666666666666664, 30.666666666666668), (54.333333333333336, 30.666666666666668), (55, 28)))
        self.add_line('p2-r1-7', (55, 28), (61, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', closed=False)
        self.add_bezier('p3-r1-1', (87, 6), ((85, 4), (83, 2), (81, 2)))
        self.add_bezier('p3-r1-2', (81, 2), ((75, 2), (70, 9), (70, 17)))
        self.add_bezier('p3-r1-3', (70, 17), ((70, 18), (70, 20), (71, 21)))
        self.add_bezier('p3-r1-4', (71, 21), ((72, 27), (76, 29), (80, 29)))
        self.add_bezier('p3-r1-5', (80, 29), ((85, 29), (90, 24), (90, 16)))
        self.add_line('p3-r1-6', (90, 16), (82, 16))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', closed=False)

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
TYPEFACE_GLYPH_IDS = ('letter-d-uppercase', 'letter-w-uppercase', 'letter-g-uppercase')
