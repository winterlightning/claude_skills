"""Independent 32px profile of british-pound-invoice-document-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'd540aa9a-0088-4ba3-b31e-9f6965432001'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/pound bill_d540aa9a-0088-4ba3-b31e-9f6965432001.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d540aa9a-0088-4ba3-b31e-9f6965432001', 'pictographic-primitives/other/pound bill_d540aa9a-0088-4ba3-b31e-9f6965432001.svg'),)
PROFILE_SOURCE_KEYS = ('solo/british-pound-invoice-document-solo',)
SOLO_SOURCE_ICON_IDS = ('british-pound-invoice-document-solo',)
REFERENCE_EXPORT_SHA256 = 'a88b439195a4f7689ddfeb8aa6c25e178b5856f4fa7fed53300c21d04acb9e32'

class DrawingVariant2(Sub32):
    icon_id = 'british-pound-invoice-document-solo-profile32-v2'
    variant_of = 'british-pound-invoice-document-solo-profile32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/finance'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Invoice page with a shared pound sign. Construction reference: shared typeface / geometric source construction."""
        box(self, 'page', 2, 2, 30, 30, 3)
        self.add_bezier('char8-p1-r1-1', (21, 11), ((21, 10), (19, 8), (17, 8)))
        self.add_bezier('char8-p1-r1-2', (17, 8), ((15, 8), (12, 10), (12, 12)))
        self.add_line('char8-p1-r1-3', (12, 12), (12, 19))
        self.add_bezier('char8-p1-r1-4', (12, 19), ((12, 21), (12, 23), (10, 24)))
        self.add_line('char8-p1-r1-5', (10, 24), (22, 24))
        self.add_contour('char8-path-1-1', 'char8-p1-r1-1', 'char8-p1-r1-2', 'char8-p1-r1-3', 'char8-p1-r1-4', 'char8-p1-r1-5', closed=False)
        self.add_line('char8-p2-r1-1', (10, 17), (18, 17))
        self.add_contour('char8-path-2-1', 'char8-p2-r1-1', closed=False)
        self.relate('connect', 'char8-path-2-1', 'char8-path-1-1')

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
