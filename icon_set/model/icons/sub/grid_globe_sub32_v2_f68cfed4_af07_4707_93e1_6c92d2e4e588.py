"""Independent 32px profile of grid-globe.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'f68cfed4-af07-4707-93e1-6c92d2e4e588'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/maps/earth_f68cfed4-af07-4707-93e1-6c92d2e4e588.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f68cfed4-af07-4707-93e1-6c92d2e4e588', 'pictographic-primitives/maps/earth_f68cfed4-af07-4707-93e1-6c92d2e4e588.svg'),)
PROFILE_SOURCE_KEYS = ('solo/grid-globe',)
SOLO_SOURCE_ICON_IDS = ('grid-globe',)
REFERENCE_EXPORT_SHA256 = 'a453e1b32864b0cbb9a7d310bda7543aa788eb898dee362ded5855db863c554c'

class DrawingVariant2(Sub32):
    icon_id = 'grid-globe-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'maps'
    categories = ('maps', 'state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Circular globe with two straight meridians and one equator. Construction reference: globe."""
        circle(self, 'globe', 16, 16, 14)
        self.add_line('equator', (2, 16), (30, 16))
        self.relate('connect', 'equator', 'globe')
        for x in (10, 22):
            self.add_line(f'meridian-{x}', (x, 4), (x, 28))
            self.relate('connect', f'meridian-{x}', 'globe')
            self.relate('connect', f'meridian-{x}', 'equator')

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
