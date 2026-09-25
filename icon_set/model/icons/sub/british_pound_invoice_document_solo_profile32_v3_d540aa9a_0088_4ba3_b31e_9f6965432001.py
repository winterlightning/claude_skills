"""Independent 32px profile of british-pound-invoice-document-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._tall_base import TallSideSub32
SOURCE_ICON_ID = 'd540aa9a-0088-4ba3-b31e-9f6965432001'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/pound bill_d540aa9a-0088-4ba3-b31e-9f6965432001.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d540aa9a-0088-4ba3-b31e-9f6965432001', 'pictographic-primitives/other/pound bill_d540aa9a-0088-4ba3-b31e-9f6965432001.svg'),)
PROFILE_SOURCE_KEYS = ('solo/british-pound-invoice-document-solo',)
SOLO_SOURCE_ICON_IDS = ('british-pound-invoice-document-solo',)
REFERENCE_EXPORT_SHA256 = 'a88b439195a4f7689ddfeb8aa6c25e178b5856f4fa7fed53300c21d04acb9e32'

class DrawingVariant3(TallSideSub32):
    icon_id = 'british-pound-invoice-document-solo-profile32-v3'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Tall clipped-corner invoice with the shared pound glyph. Construction reference: source composition; shared small-size character construction."""
        self.add_polyline('page', (2, 2), (20, 2), (30, 12), (30, 46), (2, 46), (2, 2))

        class Offset:

            def add_line(_, n, a, b):
                return self.add_line(n, (a[0], a[1] + 10), (b[0], b[1] + 10))

            def add_bezier(_, n, a, ps):
                return self.add_bezier(n, (a[0], a[1] + 10), tuple(((x, y + 10) for x, y in ps)))

            def __getattr__(_, n):
                return getattr(self, n)
        g = Offset()
        g.add_bezier('pound-p1-r1-1', (22, 10), ((22, 8), (20, 7), (17, 7)))
        g.add_bezier('pound-p1-r1-2', (17, 7), ((14, 7), (12, 8), (12, 11)))
        g.add_line('pound-p1-r1-3', (12, 11), (12, 19))
        g.add_bezier('pound-p1-r1-4', (12, 19), ((12, 23), (11, 25), (9, 25)))
        g.add_line('pound-p1-r1-5', (9, 25), (23, 25))
        g.add_contour('pound-path-1-1', 'pound-p1-r1-1', 'pound-p1-r1-2', 'pound-p1-r1-3', 'pound-p1-r1-4', 'pound-p1-r1-5', closed=False)
        g.add_line('pound-p2-r1-1', (9, 17), (18, 17))
        g.add_contour('pound-path-2-1', 'pound-p2-r1-1', closed=False)
        g.relate('connect', 'pound-path-2-1', 'pound-path-1-1')

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
TYPEFACE_GLYPH_IDS = ('symbol-pound',)
