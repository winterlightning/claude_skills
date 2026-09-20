"""Independent 32px profile of british-pound-invoice-document-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._tall_base import SideSub32Exception
SOURCE_ICON_ID = 'd540aa9a-0088-4ba3-b31e-9f6965432001'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/pound bill_d540aa9a-0088-4ba3-b31e-9f6965432001.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d540aa9a-0088-4ba3-b31e-9f6965432001', 'pictographic-primitives/other/pound bill_d540aa9a-0088-4ba3-b31e-9f6965432001.svg'),)
PROFILE_SOURCE_KEYS = ('solo/british-pound-invoice-document-solo',)
SOLO_SOURCE_ICON_IDS = ('british-pound-invoice-document-solo',)
REFERENCE_EXPORT_SHA256 = 'a88b439195a4f7689ddfeb8aa6c25e178b5856f4fa7fed53300c21d04acb9e32'

class DrawingVariant4(SideSub32Exception):
    icon_id = 'british-pound-invoice-document-solo-profile32-v4'
    variant_of = 'british-pound-invoice-document-solo-profile32-v3'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/finance'
    profile_source_keys = PROFILE_SOURCE_KEYS
    canvas_width = 44
    canvas_height = 32
    canvas_width = 44
    canvas_height = 32
    canvas_width = 44
    canvas_height = 32
    canvas_width = 32
    canvas_height = 40
    canvas_width = 32
    canvas_height = 44
    canvas_width = 32
    canvas_height = 44
    canvas_width = 32
    canvas_height = 44
    canvas_width = 32
    canvas_height = 44

    def build(self):
        """Pound invoice: rounded clipped-corner page, pound on the left and both right-hand text lines restored. Construction reference: Original source composition; clean contour construction."""
        self.add_line('top', (6, 2), (20, 2))
        self.add_line('fold', (20, 2), (30, 12))
        self.add_line('right', (30, 12), (30, 38))
        self.add_arc('br', (30, 38), (26, 42), radius_x=4)
        self.add_line('bottom', (26, 42), (6, 42))
        self.add_arc('bl', (6, 42), (2, 38), radius_x=4)
        self.add_line('left', (2, 38), (2, 6))
        self.add_arc('tl', (2, 6), (6, 2), radius_x=4)
        self.add_contour('page', 'top', 'fold', 'right', 'br', 'bottom', 'bl', 'left', 'tl')
        for n, y in [('line-one', 20), ('line-two', 28)]:
            self.add_line(n, (21, y), (23, y))
        from icon_set.typeface.reference_forms import draw_narrow_pound
        draw_narrow_pound(self)

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

TYPEFACE_PROFILE_VARIANTS = ('symbol-pound-portrait-source32',)
