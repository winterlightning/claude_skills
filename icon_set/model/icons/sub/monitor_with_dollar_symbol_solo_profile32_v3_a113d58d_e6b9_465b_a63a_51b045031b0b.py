"""Independent 32px profile of monitor-with-dollar-symbol-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'a113d58d-e6b9-465b-a63a-51b045031b0b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/monitor dollar sign_a113d58d-e6b9-465b-a63a-51b045031b0b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a113d58d-e6b9-465b-a63a-51b045031b0b', 'pictographic-primitives/symbol/monitor dollar sign_a113d58d-e6b9-465b-a63a-51b045031b0b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/monitor-with-dollar-symbol-solo',)
SOLO_SOURCE_ICON_IDS = ('monitor-with-dollar-symbol-solo',)
REFERENCE_EXPORT_SHA256 = '9ba5df7fdc87988260ad6ce87b3597e491efb20dcfef355330b225846ed0fa97'

class DrawingVariant3(Sub32):
    icon_id = 'monitor-with-dollar-symbol-solo-profile32-v3'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Monitor with the lighter dollar and a simple central stand. Construction reference: source composition; shared small-size character construction."""
        box(self, 'screen', 2, 2, 30, 26, 3)
        self.add_line('stand', (16, 26), (16, 30))
        self.relate('connect', 'stand', 'screen')
        from icon_set.typeface.sub32 import draw_dollar
        draw_dollar(self, 10, 1)

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

TYPEFACE_PROFILE_VARIANTS = ('symbol-dollar-compact32-short-tick',)
