"""Independent 32px profile of religious-cross.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '9c558392-d894-4aba-8bb9-2185dd4ed2fe'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/religion/religious cross_9c558392-d894-4aba-8bb9-2185dd4ed2fe.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9c558392-d894-4aba-8bb9-2185dd4ed2fe', 'pictographic-primitives/religion/religious cross_9c558392-d894-4aba-8bb9-2185dd4ed2fe.svg'),)
PROFILE_SOURCE_KEYS = ('solo/religious-cross',)
SOLO_SOURCE_ICON_IDS = ('religious-cross',)
REFERENCE_EXPORT_SHA256 = '56d57a5c91cd60286131789072b054c481906a9fbff462c771d6b708bd17f021'

class DrawingVariant2(Sub32):
    icon_id = 'religious-cross-sub32-v2'
    variant_of = 'religious-cross-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'religion'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Upright religious cross with short horizontal arms and longer lower stem. Construction reference: cross."""
        self.add_polyline('cross', (12, 2), (20, 2), (20, 10), (28, 10), (28, 18), (20, 18), (20, 30), (12, 30), (12, 18), (4, 18), (4, 10), (12, 10), closed=True)

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
