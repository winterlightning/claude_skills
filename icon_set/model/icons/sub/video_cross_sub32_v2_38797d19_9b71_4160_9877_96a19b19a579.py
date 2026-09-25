"""Independent 32px profile of video-cross.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '38797d19-9b71-4160-9877-96a19b19a579'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/video cross_38797d19-9b71-4160-9877-96a19b19a579.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('38797d19-9b71-4160-9877-96a19b19a579', 'pictographic-primitives/symbol/video cross_38797d19-9b71-4160-9877-96a19b19a579.svg'),)
PROFILE_SOURCE_KEYS = ('solo/video-cross',)
SOLO_SOURCE_ICON_IDS = ('video-cross',)
REFERENCE_EXPORT_SHA256 = 'd2ca9280949924a9afa3a43e09fb3c198f1d0913054a20d8c3627b5c2002dd6e'

class DrawingVariant2(Sub32):
    icon_id = 'video-cross-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Video camera with rounded body, attached flared right lens and centered plus. Construction reference: video."""
        box(self, 'body', 2, 4, 22, 28, 3)
        self.add_polyline('lens', (22, 12), (30, 8), (30, 24), (22, 20))
        self.relate('connect', 'lens', 'body')
        self.add_line('plus-h', (9, 16), (15, 16))
        self.add_line('plus-v', (12, 13), (12, 19))
        self.relate('connect', 'plus-h', 'plus-v')

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
