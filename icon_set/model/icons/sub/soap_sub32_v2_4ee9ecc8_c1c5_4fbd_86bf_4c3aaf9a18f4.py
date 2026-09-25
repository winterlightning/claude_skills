"""Independent 32px profile of soap.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '4ee9ecc8-c1c5-4fbd-86bf-4c3aaf9a18f4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/soap_4ee9ecc8-c1c5-4fbd-86bf-4c3aaf9a18f4.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4ee9ecc8-c1c5-4fbd-86bf-4c3aaf9a18f4', 'pictographic-primitives/symbol/soap_4ee9ecc8-c1c5-4fbd-86bf-4c3aaf9a18f4.svg'),)
PROFILE_SOURCE_KEYS = ('solo/soap',)
SOLO_SOURCE_ICON_IDS = ('soap',)
REFERENCE_EXPORT_SHA256 = '359ecc91d653bc7a4f8ae3bf5f6bffd1fe0b31fe274abbe6daeb34ca448f9742'

class DrawingVariant2(Sub32):
    icon_id = 'soap-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Cylindrical soap bar with complete open elliptical top, vertical sides and curved lower edge. Construction reference: cylinder."""
        self.add_arc('top-a', (2, 10), (30, 10), radius_x=14, radius_y=6)
        self.add_arc('top-b', (30, 10), (2, 10), radius_x=14, radius_y=6)
        self.add_contour('top', 'top-a', 'top-b', closed=True)
        self.add_line('left', (2, 10), (2, 22))
        self.add_arc('base', (2, 22), (30, 22), radius_x=14, radius_y=6, sweep=False)
        self.add_line('right', (30, 22), (30, 10))
        self.add_contour('body', 'left', 'base', 'right')
        self.relate('connect', 'body', 'top')

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
