"""Independent 32px profile of money-bag.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '6e31cce6-f749-4014-8bc4-bf1b7d5d439c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/money bag_6e31cce6-f749-4014-8bc4-bf1b7d5d439c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6e31cce6-f749-4014-8bc4-bf1b7d5d439c', 'pictographic-primitives/symbol/money bag_6e31cce6-f749-4014-8bc4-bf1b7d5d439c.svg'), ('e362c0ea-dba3-4194-90fc-c3ab21b70d2b', 'pictographic-primitives/other/pouch dollar_e362c0ea-dba3-4194-90fc-c3ab21b70d2b.svg'))
PROFILE_SOURCE_KEYS = ('solo/money-bag', 'solo/money-bag-with-dollar-sign-solo')
SOLO_SOURCE_ICON_IDS = ('money-bag', 'money-bag-with-dollar-sign-solo')
REFERENCE_EXPORT_SHA256 = '0e2c5e13d6bbd9c804573a7efed2f30626824cad34a4b2376b257e0c7b72e3b7'

class DrawingVariant2(Sub32):
    icon_id = 'money-bag-sub32-v2'
    variant_of = 'money-bag-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Money bag with gathered neck and shared dollar sign. Construction reference: shared typeface and original frame."""
        self.add_polyline('bag-top', (10, 8), (6, 2), (26, 2), (22, 8))
        self.add_bezier('bag-right', (22, 8), ((30, 16), (30, 22), (30, 25)))
        self.add_bezier('bag-bottom', (30, 25), ((30, 30), (2, 30), (2, 25)))
        self.add_bezier('bag-left', (2, 25), ((2, 22), (2, 16), (10, 8)))
        self.add_line('tie', (10, 8), (22, 8))
        self.add_contour('bag', 'bag-right', 'bag-bottom', 'bag-left')
        self.relate('connect', 'bag-top', 'bag')
        self.relate('connect', 'tie', 'bag')
        self.relate('connect', 'tie', 'bag-top')
        self.add_bezier('char31-p1-r1-1', (20, 11), ((20, 10), (18, 10), (16, 10)))
        self.add_bezier('char31-p1-r1-2', (16, 10), ((14, 10), (12, 11), (12, 13)))
        self.add_bezier('char31-p1-r1-3', (12, 13), ((12, 13), (12, 13), (12, 13)))
        self.add_bezier('char31-p1-r1-4', (12, 13), ((12, 17), (20, 15), (20, 19)))
        self.add_bezier('char31-p1-r1-5', (20, 19), ((20, 19), (20, 19), (20, 19)))
        self.add_bezier('char31-p1-r1-6', (20, 19), ((20, 22), (18, 23), (16, 23)))
        self.add_bezier('char31-p1-r1-7', (16, 23), ((14, 23), (12, 22), (12, 21)))
        self.add_contour('char31-path-1-1', 'char31-p1-r1-1', 'char31-p1-r1-2', 'char31-p1-r1-3', 'char31-p1-r1-4', 'char31-p1-r1-5', 'char31-p1-r1-6', 'char31-p1-r1-7', closed=False)
        self.add_line('char31-p2-r1-1', (16, 8), (16, 24))
        self.add_contour('char31-path-2-1', 'char31-p2-r1-1', closed=False)
        self.relate('connect', 'char31-path-2-1', 'char31-path-1-1')

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
