"""Independent 32px profile of state32-204ecec0-870d-4feb-9da5-e8ed98b8f9c3.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '204ecec0-870d-4feb-9da5-e8ed98b8f9c3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/circle equal_204ecec0-870d-4feb-9da5-e8ed98b8f9c3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('204ecec0-870d-4feb-9da5-e8ed98b8f9c3', 'pictographic-primitives/state/circle equal_204ecec0-870d-4feb-9da5-e8ed98b8f9c3.svg'),)
PROFILE_SOURCE_KEYS = ('solo/circle-equal',)
SOLO_SOURCE_ICON_IDS = ('circle-equal',)
REFERENCE_EXPORT_SHA256 = '917d6a6978003524e3c088523c09b23119e1083b3f0b97fbefcfb21cc7fa840b'

class DrawingVariant2(Sub32):
    icon_id = 'state32-204ecec0-870d-4feb-9da5-e8ed98b8f9c3-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Circle with two centered equal-length horizontal equality bars. Construction reference: equal."""
        circle(self, 'circle', 16, 16, 14)
        self.add_line('upper', (10, 12), (22, 12))
        self.add_line('lower', (10, 20), (22, 20))

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
