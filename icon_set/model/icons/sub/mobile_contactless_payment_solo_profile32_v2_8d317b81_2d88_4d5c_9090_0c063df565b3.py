"""Independent 32px profile of mobile-contactless-payment-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '8d317b81-2d88-4d5c-9090-0c063df565b3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/mobile phone dollar sign wireless_8d317b81-2d88-4d5c-9090-0c063df565b3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8d317b81-2d88-4d5c-9090-0c063df565b3', 'pictographic-primitives/other/mobile phone dollar sign wireless_8d317b81-2d88-4d5c-9090-0c063df565b3.svg'),)
PROFILE_SOURCE_KEYS = ('solo/mobile-contactless-payment-solo',)
SOLO_SOURCE_ICON_IDS = ('mobile-contactless-payment-solo',)
REFERENCE_EXPORT_SHA256 = 'a876b26c0cc05c054034c777d3eb9a0358c522a6a9e464fc0280f5350bd3f04f'

class DrawingVariant2(Sub32):
    icon_id = 'mobile-contactless-payment-solo-profile32-v2'
    variant_of = 'mobile-contactless-payment-solo-profile32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/finance'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Wireless-payment phone and shared dollar sign. Construction reference: shared typeface and original frame."""
        box(self, 'phone', 4, 10, 28, 30, 3)
        self.add_arc('wireless', (8, 6), (24, 6), radius_x=8, radius_y=4)
        self.add_bezier('char29-p1-r1-1', (20, 11), ((20, 10), (18, 10), (16, 10)))
        self.add_bezier('char29-p1-r1-2', (16, 10), ((14, 10), (12, 11), (12, 13)))
        self.add_bezier('char29-p1-r1-3', (12, 13), ((12, 13), (12, 13), (12, 13)))
        self.add_bezier('char29-p1-r1-4', (12, 13), ((12, 17), (20, 15), (20, 19)))
        self.add_bezier('char29-p1-r1-5', (20, 19), ((20, 19), (20, 19), (20, 19)))
        self.add_bezier('char29-p1-r1-6', (20, 19), ((20, 22), (18, 23), (16, 23)))
        self.add_bezier('char29-p1-r1-7', (16, 23), ((14, 23), (12, 22), (12, 21)))
        self.add_contour('char29-path-1-1', 'char29-p1-r1-1', 'char29-p1-r1-2', 'char29-p1-r1-3', 'char29-p1-r1-4', 'char29-p1-r1-5', 'char29-p1-r1-6', 'char29-p1-r1-7', closed=False)
        self.add_line('char29-p2-r1-1', (16, 8), (16, 24))
        self.add_contour('char29-path-2-1', 'char29-p2-r1-1', closed=False)
        self.relate('connect', 'char29-path-2-1', 'char29-path-1-1')

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
