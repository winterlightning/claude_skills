"""Independent 32px profile of wind-state.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'bfffa211-4688-49bd-87eb-16a4c14d3a9b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/wind_bfffa211-4688-49bd-87eb-16a4c14d3a9b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bfffa211-4688-49bd-87eb-16a4c14d3a9b', 'pictographic-primitives/state/wind_bfffa211-4688-49bd-87eb-16a4c14d3a9b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/wind-state',)
SOLO_SOURCE_ICON_IDS = ('wind-state',)
REFERENCE_EXPORT_SHA256 = 'b0c06fb6be77ede6d48dd5ed914886bba90470855351411b5d9c65dfa0691d5a'

class DrawingVariant2(Sub32):
    icon_id = 'wind-state-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Three separate horizontal wind waves with rising curled right ends. Construction reference: wind."""
        for i, y in enumerate((4, 14, 24)):
            self.add_bezier(f'a-{i}', (2, y + 2), ((5, y), (7, y), (9, y)))
            self.add_bezier(f'b-{i}', (9, y), ((14, y), (15, y + 4), (22, y + 4)))
            self.add_bezier(f'c-{i}', (22, y + 4), ((27, y + 4), (30, y + 4), (30, y)))
            self.add_contour(f'wave-{i}', f'a-{i}', f'b-{i}', f'c-{i}')

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
