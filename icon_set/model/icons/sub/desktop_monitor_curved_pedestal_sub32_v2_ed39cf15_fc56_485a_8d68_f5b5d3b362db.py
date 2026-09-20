"""Independent 32px profile of desktop-monitor-curved-pedestal.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'ed39cf15-fc56-485a-8d68-f5b5d3b362db'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/computers/batch-04/monitor_ed39cf15-fc56-485a-8d68-f5b5d3b362db.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ed39cf15-fc56-485a-8d68-f5b5d3b362db', 'pictographic-primitives/computers/batch-04/monitor_ed39cf15-fc56-485a-8d68-f5b5d3b362db.svg'),)
PROFILE_SOURCE_KEYS = ('solo/desktop-monitor-curved-pedestal',)
SOLO_SOURCE_ICON_IDS = ('desktop-monitor-curved-pedestal',)
REFERENCE_EXPORT_SHA256 = 'dec03f28ba3b705c3829c1eda97b7ba8035caa956709e70b9a141ecc0a8451ea'

class DrawingVariant2(Sub32):
    icon_id = 'desktop-monitor-curved-pedestal-sub32-v2'
    variant_of = 'desktop-monitor-curved-pedestal-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/device'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Rounded monitor and curved flared pedestal with closed base. Construction reference: monitor."""
        box(self, 'screen', 2, 2, 30, 20, 3)
        self.add_bezier('stand-r', (20, 20), ((20, 27), (23, 30), (26, 30)))
        self.add_line('base', (26, 30), (6, 30))
        self.add_bezier('stand-l', (6, 30), ((9, 30), (12, 27), (12, 20)))
        self.add_contour('stand', 'stand-r', 'base', 'stand-l')
        self.relate('connect', 'screen', 'stand')

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
