"""Independent 32px profile of bitcoin-cryptocurrency-symbol-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = '056563c8-a6c4-4201-b355-6ff5f08795ea'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/circle bitcoin_056563c8-a6c4-4201-b355-6ff5f08795ea.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('056563c8-a6c4-4201-b355-6ff5f08795ea', 'pictographic-primitives/other/circle bitcoin_056563c8-a6c4-4201-b355-6ff5f08795ea.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bitcoin-cryptocurrency-symbol-solo',)
SOLO_SOURCE_ICON_IDS = ('bitcoin-cryptocurrency-symbol-solo',)
REFERENCE_EXPORT_SHA256 = '6db0f41abd34096506cbe717f84b6feed6b423dc6a6f03c030b5246b03c11ac7'

class DrawingVariant2(TextSub32):
    icon_id = 'bitcoin-cryptocurrency-symbol-solo-profile32-v2'
    variant_of = 'bitcoin-cryptocurrency-symbol-solo-profile32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/finance'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 25
    text_ink_bounds = (0, 0, 25, 32)

    def build(self):
        """Shared symbol-bitcoin at natural width and full 32px ink height. Construction reference: shared typeface / geometric source construction."""
        self.add_line('g0-p1-r1-1', (2, 25), (2, 7))
        self.add_line('g0-p1-r1-2', (2, 7), (13, 7))
        self.add_bezier('g0-p1-r1-3', (13, 7), ((19, 7), (22, 9), (22, 12)))
        self.add_bezier('g0-p1-r1-4', (22, 12), ((22, 14), (19, 16), (13, 16)))
        self.add_line('g0-p1-r1-5', (13, 16), (2, 16))
        self.add_contour('g0-path-1-1', 'g0-p1-r1-1', 'g0-p1-r1-2', 'g0-p1-r1-3', 'g0-p1-r1-4', 'g0-p1-r1-5', closed=False)
        self.add_bezier('g0-p2-r1-1', (13, 16), ((20, 16), (23, 18), (23, 20)))
        self.add_bezier('g0-p2-r1-2', (23, 20), ((23, 23), (20, 25), (13, 25)))
        self.add_line('g0-p2-r1-3', (13, 25), (2, 25))
        self.add_contour('g0-path-2-1', 'g0-p2-r1-1', 'g0-p2-r1-2', 'g0-p2-r1-3', closed=False)
        self.add_line('g0-p3-r1-1', (5, 2), (5, 7))
        self.add_contour('g0-path-3-1', 'g0-p3-r1-1', closed=False)
        self.add_line('g0-p4-r1-1', (13, 2), (13, 7))
        self.add_contour('g0-path-4-1', 'g0-p4-r1-1', closed=False)
        self.add_line('g0-p5-r1-1', (5, 25), (5, 30))
        self.add_contour('g0-path-5-1', 'g0-p5-r1-1', closed=False)
        self.add_line('g0-p6-r1-1', (13, 25), (13, 30))
        self.add_contour('g0-path-6-1', 'g0-p6-r1-1', closed=False)
        self.relate('connect', 'g0-p1-r1-1', 'g0-p2-r1-3')
        self.relate('connect', 'g0-p1-r1-2', 'g0-p4-r1-1')
        self.relate('connect', 'g0-p1-r1-3', 'g0-p4-r1-1')
        self.relate('connect', 'g0-p1-r1-4', 'g0-p2-r1-1')
        self.relate('connect', 'g0-p1-r1-5', 'g0-p2-r1-1')
        self.relate('connect', 'g0-p2-r1-2', 'g0-p6-r1-1')
        self.relate('connect', 'g0-p2-r1-3', 'g0-p6-r1-1')
        self.relate('connect', 'g0-path-2-1', 'g0-path-1-1')
        self.relate('connect', 'g0-path-3-1', 'g0-path-1-1')
        self.relate('connect', 'g0-path-4-1', 'g0-path-1-1')
        self.relate('connect', 'g0-path-5-1', 'g0-path-2-1')
        self.relate('connect', 'g0-path-6-1', 'g0-path-2-1')

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
TYPEFACE_GLYPH_IDS = ('symbol-bitcoin',)
