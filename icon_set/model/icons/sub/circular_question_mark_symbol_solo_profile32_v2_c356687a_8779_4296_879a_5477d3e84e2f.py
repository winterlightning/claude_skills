"""Independent 32px profile of circular-question-mark-symbol-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = 'c356687a-8779-4296-879a-5477d3e84e2f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/circle question_c356687a-8779-4296-879a-5477d3e84e2f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c356687a-8779-4296-879a-5477d3e84e2f', 'pictographic-primitives/other/circle question_c356687a-8779-4296-879a-5477d3e84e2f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/circular-question-mark-symbol-solo',)
SOLO_SOURCE_ICON_IDS = ('circular-question-mark-symbol-solo',)
REFERENCE_EXPORT_SHA256 = '649c1cb2e5085a00f0d0f65ad90be035bff07303f8385f5838e5310aeba585c9'

class DrawingVariant2(TextSub32):
    icon_id = 'circular-question-mark-symbol-solo-profile32-v2'
    variant_of = 'circular-question-mark-symbol-solo-profile32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/finance'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 22
    text_ink_bounds = (0, 0, 22, 32)

    def build(self):
        """Shared question mark at natural proportions. Construction reference: shared typeface."""
        self.add_bezier('g0-p1-r1-1', (2, 9), ((2, 4), (6, 2), (11, 2)))
        self.add_bezier('g0-p1-r1-2', (11, 2), ((15, 2), (20, 4), (20, 9)))
        self.add_bezier('g0-p1-r1-3', (20, 9), ((20, 16), (11, 16), (11, 22)))
        self.add_contour('g0-path-1-1', 'g0-p1-r1-1', 'g0-p1-r1-2', 'g0-p1-r1-3', closed=False)
        self.add_line('g0-p2-r1-1', (11, 30), (11, 30))
        self.add_contour('g0-path-2-1', 'g0-p2-r1-1', closed=False)

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
TYPEFACE_GLYPH_IDS = ('symbol-question',)
