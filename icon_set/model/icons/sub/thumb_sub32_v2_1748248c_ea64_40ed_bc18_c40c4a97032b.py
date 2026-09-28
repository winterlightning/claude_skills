"""Independent 32px profile of thumb.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '1748248c-ea64-40ed-bc18-c40c4a97032b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/thumb_1748248c-ea64-40ed-bc18-c40c4a97032b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1748248c-ea64-40ed-bc18-c40c4a97032b', 'pictographic-primitives/state/thumb_1748248c-ea64-40ed-bc18-c40c4a97032b.svg'), ('c5652a88-5c11-499a-8e2e-486a9b3a75d1', 'pictographic-primitives/symbol/thumb_c5652a88-5c11-499a-8e2e-486a9b3a75d1.svg'))
PROFILE_SOURCE_KEYS = ('solo/thumb', 'solo/thumb-symbol')
SOLO_SOURCE_ICON_IDS = ('thumb', 'thumb-symbol')
REFERENCE_EXPORT_SHA256 = 'd0ba68115546736ca9894c4ac6f3e5459fbf3145a63a8a908393719577d98d78'

class DrawingVariant2(Sub32):
    icon_id = 'thumb-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Thumb-up silhouette with raised rounded thumb, concave web, slanted finger edge and short wrist. Construction reference: thumbs-up."""
        self.add_bezier('wrist-top', (4, 16), ((10, 16), (11, 12), (12, 6)))
        self.add_bezier('thumb-top', (12, 6), ((12, 2), (14, 2), (16, 2)))
        self.add_bezier('thumb-round', (16, 2), ((20, 2), (22, 4), (21, 8)))
        self.add_line('thumb-side', (21, 8), (20, 14))
        self.add_line('finger-top', (20, 14), (25, 14))
        self.add_bezier('finger-tip', (25, 14), ((28, 14), (28, 16), (28, 17)))
        self.add_line('finger-side', (28, 17), (25, 27))
        self.add_bezier('palm', (25, 27), ((24, 30), (22, 30), (19, 30)))
        self.add_line('base', (19, 30), (14, 30))
        self.add_bezier('wrist-bottom', (14, 30), ((10, 30), (10, 28), (7, 28)))
        self.add_line('wrist-a', (7, 28), (4, 28))
        self.add_line('wrist-b', (4, 28), (4, 16))
        self.add_contour('hand', 'wrist-top', 'thumb-top', 'thumb-round', 'thumb-side', 'finger-top', 'finger-tip', 'finger-side', 'palm', 'base', 'wrist-bottom', 'wrist-a', 'wrist-b', closed=True)

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
