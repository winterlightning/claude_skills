"""Independent 32px profile of database-servers.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '7226fb36-c110-4033-9d0b-3e66cfa5b027'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/servers/database_7226fb36-c110-4033-9d0b-3e66cfa5b027.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7226fb36-c110-4033-9d0b-3e66cfa5b027', 'pictographic-primitives/servers/database_7226fb36-c110-4033-9d0b-3e66cfa5b027.svg'), ('b3ea511d-2f05-474a-944e-587c5423980b', 'pictographic-primitives/diagrams/database_b3ea511d-2f05-474a-944e-587c5423980b.svg'))
PROFILE_SOURCE_KEYS = ('solo/database-servers', 'solo/database-diagrams')
SOLO_SOURCE_ICON_IDS = ('database-servers', 'database-diagrams')
REFERENCE_EXPORT_SHA256 = 'ad9ac229eddcd969e40d210b27eeed7f66ff8c9a2e5a743bbaf9796892935d26'

class DrawingVariant2(Sub32):
    icon_id = 'database-servers-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'servers'
    categories = ('servers', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Database outline with curved crown and exactly two internal tier arcs; no invented closed ellipse. Construction reference: database."""
        self.add_arc('crown', (4, 6), (28, 6), radius_x=12, radius_y=4)
        self.add_line('right', (28, 6), (28, 26))
        self.add_arc('base', (28, 26), (4, 26), radius_x=12, radius_y=4)
        self.add_line('left', (4, 26), (4, 6))
        self.add_contour('body', 'crown', 'right', 'base', 'left', closed=True)
        for y in (11, 19):
            self.add_arc(f'tier-{y}', (28, y), (4, y), radius_x=12, radius_y=4)
            self.relate('connect', f'tier-{y}', 'body')

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
