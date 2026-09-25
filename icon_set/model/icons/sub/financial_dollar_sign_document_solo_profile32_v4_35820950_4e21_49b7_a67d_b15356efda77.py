"""Independent 32px profile of financial-dollar-sign-document-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._tall_base import SideSub32Exception
SOURCE_ICON_ID = '35820950-4e21-49b7-a67d-b15356efda77'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/dollar bill_35820950-4e21-49b7-a67d-b15356efda77.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('35820950-4e21-49b7-a67d-b15356efda77', 'pictographic-primitives/other/dollar bill_35820950-4e21-49b7-a67d-b15356efda77.svg'),)
PROFILE_SOURCE_KEYS = ('solo/financial-dollar-sign-document-solo',)
SOLO_SOURCE_ICON_IDS = ('financial-dollar-sign-document-solo',)
REFERENCE_EXPORT_SHA256 = '6d5b6d721f6bdede00fd4d9d02872bc8992658ea250d9fe293a9c8809019ba41'

class DrawingVariant4(SideSub32Exception):
    icon_id = 'financial-dollar-sign-document-solo-profile32-v4'
    variant_of = 'financial-dollar-sign-document-solo-profile32-v3'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
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
    canvas_height = 40
    canvas_width = 32
    canvas_height = 40
    canvas_width = 32
    canvas_height = 40
    canvas_width = 32
    canvas_height = 40

    def build(self):
        """Dollar document: rounded clipped-corner page, original open dollar on the left and both right-hand text lines restored. Construction reference: Original source composition; clean contour construction."""
        self.add_line('top', (6, 2), (20, 2))
        self.add_line('fold', (20, 2), (30, 12))
        self.add_line('right', (30, 12), (30, 34))
        self.add_arc('br', (30, 34), (26, 38), radius_x=4)
        self.add_line('bottom', (26, 38), (6, 38))
        self.add_arc('bl', (6, 38), (2, 34), radius_x=4)
        self.add_line('left', (2, 34), (2, 6))
        self.add_arc('tl', (2, 6), (6, 2), radius_x=4)
        self.add_contour('page', 'top', 'fold', 'right', 'br', 'bottom', 'bl', 'left', 'tl')
        for n, y in [('line-one', 20), ('line-two', 28)]:
            self.add_line(n, (21, y), (23, y))
        from icon_set.typeface.reference_forms import draw_small_open_dollar
        draw_small_open_dollar(self, 12, 16)

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
TYPEFACE_GLYPH_IDS = ('symbol-dollar',)

TYPEFACE_PROFILE_VARIANTS = ('symbol-dollar-open-small-source32',)
