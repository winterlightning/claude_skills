"""Independent 32px profile of mobile-wireless-pound-payment-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '3ebbbe60-66ff-4346-a1c8-9367527d9ea9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/mobile phone pound sign wireless_3ebbbe60-66ff-4346-a1c8-9367527d9ea9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3ebbbe60-66ff-4346-a1c8-9367527d9ea9', 'pictographic-primitives/other/mobile phone pound sign wireless_3ebbbe60-66ff-4346-a1c8-9367527d9ea9.svg'),)
PROFILE_SOURCE_KEYS = ('solo/mobile-wireless-pound-payment-solo',)
SOLO_SOURCE_ICON_IDS = ('mobile-wireless-pound-payment-solo',)
REFERENCE_EXPORT_SHA256 = '29749699c767f28e1029d9ab391a263486c9f4c9a99ec4b6267829fa49b27803'

class DrawingVariant2(Sub32):
    icon_id = 'mobile-wireless-pound-payment-solo-profile32-v2'
    variant_of = 'mobile-wireless-pound-payment-solo-profile32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/finance'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Wireless-payment phone retaining shared pound character. Construction reference: shared typeface / geometric source construction."""
        box(self, 'phone', 4, 10, 28, 30, 3)
        self.add_arc('wireless', (8, 5), (24, 5), radius_x=10, radius_y=3)
        self.add_bezier('char13-p1-r1-1', (21, 11), ((21, 10), (19, 8), (17, 8)))
        self.add_bezier('char13-p1-r1-2', (17, 8), ((15, 8), (12, 10), (12, 12)))
        self.add_line('char13-p1-r1-3', (12, 12), (12, 19))
        self.add_bezier('char13-p1-r1-4', (12, 19), ((12, 21), (12, 23), (10, 24)))
        self.add_line('char13-p1-r1-5', (10, 24), (22, 24))
        self.add_contour('char13-path-1-1', 'char13-p1-r1-1', 'char13-p1-r1-2', 'char13-p1-r1-3', 'char13-p1-r1-4', 'char13-p1-r1-5', closed=False)
        self.add_line('char13-p2-r1-1', (10, 17), (18, 17))
        self.add_contour('char13-path-2-1', 'char13-p2-r1-1', closed=False)
        self.relate('connect', 'char13-path-2-1', 'char13-path-1-1')

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
TYPEFACE_GLYPH_IDS = ('symbol-pound',)
