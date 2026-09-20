"""Independent 32px profile of won.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = '18f047b9-f81e-571a-a3ea-2c4af962bcb7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/money/won_18f047b9-f81e-571a-a3ea-2c4af962bcb7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('18f047b9-f81e-571a-a3ea-2c4af962bcb7', 'pictographic-primitives/money/won_18f047b9-f81e-571a-a3ea-2c4af962bcb7.svg'),)
PROFILE_SOURCE_KEYS = ('solo/won',)
SOLO_SOURCE_ICON_IDS = ('won',)
REFERENCE_EXPORT_SHA256 = 'de0fbfba3c299a969fc32ad65dc01421b6802e8876ad59f63f4e61aaf4b08c9c'

class DrawingVariant2(TextSub32):
    icon_id = 'won-sub32-v2'
    variant_of = 'won-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'money'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 48
    text_ink_bounds = (0, 0, 48, 32)

    def build(self):
        """Shared glyphs symbol-won-one-bar at 32px ink height and natural width. Construction reference: shared typeface / geometric source construction."""
        self.add_line('g0-p1-r1-1', (2, 2), (13, 30))
        self.add_line('g0-p1-r1-2', (13, 30), (24, 4))
        self.add_line('g0-p1-r1-3', (24, 4), (35, 30))
        self.add_line('g0-p1-r1-4', (35, 30), (46, 2))
        self.add_contour('g0-path-1-1', 'g0-p1-r1-1', 'g0-p1-r1-2', 'g0-p1-r1-3', 'g0-p1-r1-4', closed=False)
        self.add_line('g0-p2-r1-1', (2, 17), (46, 17))
        self.add_contour('g0-path-2-1', 'g0-p2-r1-1', closed=False)
        self.relate('connect', 'g0-path-2-1', 'g0-path-1-1')

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
TYPEFACE_GLYPH_IDS = ('symbol-won-one-bar',)
