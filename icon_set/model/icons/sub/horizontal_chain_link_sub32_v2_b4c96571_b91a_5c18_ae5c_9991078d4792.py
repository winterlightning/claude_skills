"""Independent 32px profile of horizontal-chain-link.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'b4c96571-b91a-5c18-ae5c-9991078d4792'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/hyperlink_b4c96571-b91a-5c18-ae5c-9991078d4792.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b4c96571-b91a-5c18-ae5c-9991078d4792', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/hyperlink_b4c96571-b91a-5c18-ae5c-9991078d4792.svg'),)
PROFILE_SOURCE_KEYS = ('solo/horizontal-chain-link',)
SOLO_SOURCE_ICON_IDS = ('horizontal-chain-link',)
REFERENCE_EXPORT_SHA256 = '96613f489f00818202b8110f36cef6070c09c6ab562561a713e0d742ae86ea76'

class DrawingVariant2(Sub32):
    icon_id = 'horizontal-chain-link-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Two horizontal rounded links with inward-curved returning tips and separate middle connecting bar. Construction reference: link."""
        for name, mirror in [('left', False), ('right', True)]:

            def p(x, y):
                return (32 - x if mirror else x, y)
            sweep = mirror
            self.add_arc(name + '-return-top', p(12, 9), p(8, 6), radius_x=4, radius_y=3, sweep=sweep)
            self.add_line(name + '-top', p(8, 6), p(6, 6))
            self.add_arc(name + '-tl', p(6, 6), p(2, 10), radius_x=4, sweep=sweep)
            self.add_line(name + '-side', p(2, 10), p(2, 22))
            self.add_arc(name + '-bl', p(2, 22), p(6, 26), radius_x=4, sweep=sweep)
            self.add_line(name + '-base', p(6, 26), p(8, 26))
            self.add_arc(name + '-return-base', p(8, 26), p(12, 23), radius_x=4, radius_y=3, sweep=sweep)
            self.add_contour(name, *[name + '-' + s for s in ('return-top', 'top', 'tl', 'side', 'bl', 'base', 'return-base')])
        self.add_line('middle', (10, 16), (22, 16))

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
