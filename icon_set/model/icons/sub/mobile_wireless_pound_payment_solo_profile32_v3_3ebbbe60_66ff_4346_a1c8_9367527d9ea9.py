"""Independent 32px profile of mobile-wireless-pound-payment-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._tall_base import TallSideSub32
SOURCE_ICON_ID = '3ebbbe60-66ff-4346-a1c8-9367527d9ea9'
SOURCE_PATH = 'pictographic-primitives/other/mobile phone pound sign wireless_3ebbbe60-66ff-4346-a1c8-9367527d9ea9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3ebbbe60-66ff-4346-a1c8-9367527d9ea9', 'pictographic-primitives/other/mobile phone pound sign wireless_3ebbbe60-66ff-4346-a1c8-9367527d9ea9.svg'),)
PROFILE_SOURCE_KEYS = ('solo/mobile-wireless-pound-payment-solo',)
SOLO_SOURCE_ICON_IDS = ('mobile-wireless-pound-payment-solo',)
REFERENCE_EXPORT_SHA256 = '29749699c767f28e1029d9ab391a263486c9f4c9a99ec4b6267829fa49b27803'

class DrawingVariant3(TallSideSub32):
    icon_id = 'mobile-wireless-pound-payment-solo-profile32-v3'
    variant_label = 'User review correction; preserve earlier variants'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('wireless', (4, 6), (28, 6), radius_x=12, radius_y=4)
        box(self, 'phone', 2, 12, 30, 46, 4)

        class Offset:

            def add_line(_, n, a, b):
                return self.add_line(n, (a[0], a[1] + 13), (b[0], b[1] + 13))

            def add_bezier(_, n, a, ps):
                return self.add_bezier(n, (a[0], a[1] + 13), tuple(((x, y + 13) for x, y in ps)))

            def add_arc(_, n, a, b, **kw):
                return self.add_arc(n, (a[0], a[1] + 13), (b[0], b[1] + 13), **kw)

            def __getattr__(_, n):
                return getattr(self, n)
        g = Offset()
        g.add_bezier('currency-p1-r1-1', (22, 10), ((22, 8), (20, 7), (17, 7)))
        g.add_bezier('currency-p1-r1-2', (17, 7), ((14, 7), (12, 8), (12, 11)))
        g.add_line('currency-p1-r1-3', (12, 11), (12, 19))
        g.add_bezier('currency-p1-r1-4', (12, 19), ((12, 22), (11, 24), (9, 24)))
        g.add_line('currency-p1-r1-5', (9, 24), (23, 24))
        g.add_contour('currency-path-1-1', 'currency-p1-r1-1', 'currency-p1-r1-2', 'currency-p1-r1-3', 'currency-p1-r1-4', 'currency-p1-r1-5', closed=False)
        g.add_line('currency-p2-r1-1', (9, 16), (18, 16))
        g.add_contour('currency-path-2-1', 'currency-p2-r1-1', closed=False)
        g.relate('connect', 'currency-path-2-1', 'currency-path-1-1')

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
