"""Independent 32px profile of key-round-bow.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '7f99ed9d-aefc-4d4a-9237-167f01c21fea'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/state key_7f99ed9d-aefc-4d4a-9237-167f01c21fea.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7f99ed9d-aefc-4d4a-9237-167f01c21fea', 'pictographic-primitives/symbol/state key_7f99ed9d-aefc-4d4a-9237-167f01c21fea.svg'), ('8d4e51db-4d2a-4285-a400-fd2f7b20a987', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-05/key_8d4e51db-4d2a-4285-a400-fd2f7b20a987.svg'))
PROFILE_SOURCE_KEYS = ('solo/key-round-bow',)
SOLO_SOURCE_ICON_IDS = ('key-round-bow',)
REFERENCE_EXPORT_SHA256 = '03bdc2b2de3f7f32bee53969b6cae062f640ce2cb12b8bc6469c35fbf2622cdb'

class DrawingVariant2(Sub32):
    icon_id = 'key-round-bow-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Diagonal key with a genuinely circular bow and visible circular hole. Construction reference: key-round."""
        self.add_arc('bow', (12, 10), (22, 20), radius_x=10, large_arc=True, sweep=False)
        self.add_polyline('shaft', (22, 20), (30, 11), (30, 2), (21, 2), (12, 10))
        self.relate('connect', 'bow', 'shaft')
        circle(self, 'hole', 12, 20, 3)

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
