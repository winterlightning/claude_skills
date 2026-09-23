"""Independent 32px profile of workflow-data-table-1-business.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'c8dfe4cb-2c1f-4086-8985-b294567074d5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/business/workflow data table 1_c8dfe4cb-2c1f-4086-8985-b294567074d5.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c8dfe4cb-2c1f-4086-8985-b294567074d5', 'pictographic-primitives/business/workflow data table 1_c8dfe4cb-2c1f-4086-8985-b294567074d5.svg'),)
PROFILE_SOURCE_KEYS = ('solo/workflow-data-table-1-business',)
SOLO_SOURCE_ICON_IDS = ('workflow-data-table-1-business',)
REFERENCE_EXPORT_SHA256 = '2ac32d16ecefe3bfc57dd0fea54831bcf97c249c35c6bbfb5c6ef98866b7848b'

class DrawingVariant2(Sub32):
    icon_id = 'workflow-data-table-1-business-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'business'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Rounded data table, full-width header and a three-column/two-row body. Construction reference: none."""
        box(self, 'table', 2, 2, 30, 30, 3)
        for y in (10, 20):
            self.add_line(f'row-{y}', (2, y), (30, y))
            self.relate('connect', f'row-{y}', 'table')
        for x in (11, 21):
            self.add_line(f'column-{x}', (x, 10), (x, 30))
            self.relate('connect', f'column-{x}', 'table')
            for y in (10, 20):
                self.relate('connect', f'column-{x}', f'row-{y}')

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
