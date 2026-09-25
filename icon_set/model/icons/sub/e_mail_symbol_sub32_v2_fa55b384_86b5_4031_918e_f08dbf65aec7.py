"""Independent 32px profile of e-mail-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'fa55b384-86b5-4031-918e-f08dbf65aec7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/e mail_fa55b384-86b5-4031-918e-f08dbf65aec7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('fa55b384-86b5-4031-918e-f08dbf65aec7', 'pictographic-primitives/symbol/e mail_fa55b384-86b5-4031-918e-f08dbf65aec7.svg'),)
PROFILE_SOURCE_KEYS = ('solo/e-mail-symbol',)
SOLO_SOURCE_ICON_IDS = ('e-mail-symbol',)
REFERENCE_EXPORT_SHA256 = 'f69ae2d00a398809a257e89a569439f828a3647e23318e490856f84cc2a87106'

class DrawingVariant2(Sub32):
    icon_id = 'e-mail-symbol-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Envelope with square top corners, rounded lower corners and V flap with rounded point. Construction reference: mail."""
        self.add_polyline('upper', (2, 4), (30, 4), (30, 25))
        self.add_arc('br', (30, 25), (27, 28), radius_x=3)
        self.add_line('base', (27, 28), (5, 28))
        self.add_arc('bl', (5, 28), (2, 25), radius_x=3)
        self.add_line('left', (2, 25), (2, 4))
        self.add_contour('lower', 'br', 'base', 'bl', 'left')
        self.relate('connect', 'upper', 'lower')
        self.add_line('flap-l', (2, 4), (14, 16))
        self.add_bezier('flap-point', (14, 16), ((15, 17), (17, 17), (18, 16)))
        self.add_line('flap-r', (18, 16), (30, 4))
        self.add_contour('flap', 'flap-l', 'flap-point', 'flap-r')
        self.relate('connect', 'flap', 'upper')
        self.relate('connect', 'flap', 'lower')

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
