"""Independent 32px profile of mobile-contactless-payment-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._tall_base import TallSideSub32
SOURCE_ICON_ID = '8d317b81-2d88-4d5c-9090-0c063df565b3'
SOURCE_PATH = 'pictographic-primitives/other/mobile phone dollar sign wireless_8d317b81-2d88-4d5c-9090-0c063df565b3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8d317b81-2d88-4d5c-9090-0c063df565b3', 'pictographic-primitives/other/mobile phone dollar sign wireless_8d317b81-2d88-4d5c-9090-0c063df565b3.svg'),)
PROFILE_SOURCE_KEYS = ('solo/mobile-contactless-payment-solo',)
SOLO_SOURCE_ICON_IDS = ('mobile-contactless-payment-solo',)
REFERENCE_EXPORT_SHA256 = 'a876b26c0cc05c054034c777d3eb9a0358c522a6a9e464fc0280f5350bd3f04f'

class DrawingVariant3(TallSideSub32):
    icon_id = 'mobile-contactless-payment-solo-profile32-v3'
    variant_label = 'User review correction; preserve earlier variants'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('wireless', (4, 6), (28, 6), radius_x=12, radius_y=4)
        self.add_line('lt', (10, 12), (6, 12))
        self.add_arc('tl', (6, 12), (2, 16), radius_x=4, sweep=False)
        self.add_line('l', (2, 16), (2, 42))
        self.add_arc('bl', (2, 42), (6, 46), radius_x=4, sweep=False)
        self.add_line('lb', (6, 46), (10, 46))
        self.add_contour('left', 'lt', 'tl', 'l', 'bl', 'lb')
        self.add_line('rt', (22, 12), (26, 12))
        self.add_arc('tr', (26, 12), (30, 16), radius_x=4)
        self.add_line('r', (30, 16), (30, 42))
        self.add_arc('br', (30, 42), (26, 46), radius_x=4)
        self.add_line('rb', (26, 46), (22, 46))
        self.add_contour('right', 'rt', 'tr', 'r', 'br', 'rb')

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
        g.add_bezier('currency-p1-r1-1', (22, 9), ((22, 7), (19, 6), (16, 6)))
        g.add_bezier('currency-p1-r1-2', (16, 6), ((13, 6), (10, 7), (9, 11)))
        g.add_bezier('currency-p1-r1-3', (9, 11), ((9, 11), (9, 11), (9, 12)))
        g.add_bezier('currency-p1-r1-4', (9, 12), ((9, 17), (23, 15), (23, 21)))
        g.add_bezier('currency-p1-r1-5', (23, 21), ((23, 21), (23, 21), (23, 22)))
        g.add_bezier('currency-p1-r1-6', (23, 22), ((23, 25), (20, 27), (16, 27)))
        g.add_bezier('currency-p1-r1-7', (16, 27), ((13, 27), (10, 26), (9, 24)))
        g.add_contour('currency-path-1-1', 'currency-p1-r1-1', 'currency-p1-r1-2', 'currency-p1-r1-3', 'currency-p1-r1-4', 'currency-p1-r1-5', 'currency-p1-r1-6', 'currency-p1-r1-7', closed=False)
        g.add_line('currency-p2-r1-1', (16, 3), (16, 29))
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
