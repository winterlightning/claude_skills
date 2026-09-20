"""Independent 32px profile of archive-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '50e8e4be-2921-498a-b6bc-31b5b6442b6e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/content/archive_50e8e4be-2921-498a-b6bc-31b5b6442b6e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('50e8e4be-2921-498a-b6bc-31b5b6442b6e', 'pictographic-primitives/content/archive_50e8e4be-2921-498a-b6bc-31b5b6442b6e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/archive-content',)
SOLO_SOURCE_ICON_IDS = ('archive-content',)
REFERENCE_EXPORT_SHA256 = '926bff737c8bf8a9d8370db741bde00711aa04ccf2eeeb7ce457b3310227cfc3'

class DrawingVariant2(Sub32):
    icon_id = 'archive-content-sub32-v2'
    variant_of = 'archive-content-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'content'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Closed document frame and all three horizontal content lines. Small-size treatment: Reduced three content lines to two. Construction reference: file-text: rounded enclosing page."""
        box(self, 'page', 2, 2, 30, 30, 3)
        self.add_line('line-1', (10, 11), (22, 11))
        self.add_line('line-2', (10, 21), (18, 21))

def box(s, n, l, t, r, b, k=3):
    if k == 0:
        s.add_polyline(n, (l, t), (r, t), (r, b), (l, b), (l, t))
        return
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
