"""Independent 32px profile of money-bag.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '6e31cce6-f749-4014-8bc4-bf1b7d5d439c'
SOURCE_PATH = 'pictographic-primitives/symbol/money bag_6e31cce6-f749-4014-8bc4-bf1b7d5d439c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6e31cce6-f749-4014-8bc4-bf1b7d5d439c', 'pictographic-primitives/symbol/money bag_6e31cce6-f749-4014-8bc4-bf1b7d5d439c.svg'), ('e362c0ea-dba3-4194-90fc-c3ab21b70d2b', 'pictographic-primitives/other/pouch dollar_e362c0ea-dba3-4194-90fc-c3ab21b70d2b.svg'))
PROFILE_SOURCE_KEYS = ('solo/money-bag', 'solo/money-bag-with-dollar-sign-solo')
SOLO_SOURCE_ICON_IDS = ('money-bag', 'money-bag-with-dollar-sign-solo')
REFERENCE_EXPORT_SHA256 = '0e2c5e13d6bbd9c804573a7efed2f30626824cad34a4b2376b257e0c7b72e3b7'

class DrawingVariant3(Sub32):
    icon_id = 'money-bag-sub32-v3'
    variant_label = 'User review correction; preserve earlier variants'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_polyline('neck-left', (8, 2), (12, 6))
        self.add_polyline('neck-right', (24, 2), (20, 6))
        self.add_bezier('left-top', (12, 6), ((8, 10), (2, 14), (2, 20)))
        self.add_line('left', (2, 20), (2, 24))
        self.add_arc('bl', (2, 24), (8, 30), radius_x=6, sweep=False)
        self.add_line('bottom', (8, 30), (24, 30))
        self.add_arc('br', (24, 30), (30, 24), radius_x=6, sweep=False)
        self.add_line('right', (30, 24), (30, 20))
        self.add_bezier('right-top', (30, 20), ((30, 14), (24, 10), (20, 6)))
        self.add_contour('bag', 'left-top', 'left', 'bl', 'bottom', 'br', 'right', 'right-top')
        self.relate('connect', 'neck-left', 'bag')
        self.relate('connect', 'neck-right', 'bag')
        self.add_line('dollar-top', (17, 14), (16, 14))
        self.add_arc('dollar-upper', (16, 14), (16, 18), radius_x=4, radius_y=2, sweep=False)
        self.add_arc('dollar-lower', (16, 18), (16, 22), radius_x=4, radius_y=2, sweep=True)
        self.add_line('dollar-bottom', (16, 22), (15, 22))
        self.add_contour('dollar', 'dollar-top', 'dollar-upper', 'dollar-lower', 'dollar-bottom')
        self.add_line('tick-top', (16, 12), (16, 14))
        self.add_line('tick-bottom', (16, 22), (16, 23))
        self.relate('connect', 'tick-top', 'dollar')
        self.relate('connect', 'tick-bottom', 'dollar')

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
