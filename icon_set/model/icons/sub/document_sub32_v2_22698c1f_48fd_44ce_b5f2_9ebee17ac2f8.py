"""Independent 32px profile of document.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '22698c1f-48fd-44ce-b5f2-9ebee17ac2f8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/content/document_22698c1f-48fd-44ce-b5f2-9ebee17ac2f8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('22698c1f-48fd-44ce-b5f2-9ebee17ac2f8', 'pictographic-primitives/content/document_22698c1f-48fd-44ce-b5f2-9ebee17ac2f8.svg'),)
PROFILE_SOURCE_KEYS = ('solo/document',)
SOLO_SOURCE_ICON_IDS = ('document',)
REFERENCE_EXPORT_SHA256 = '691d59ac9b29c0d50e3b52c9d0b9a380d5678681575e327798cd84427e393a31'

class DrawingVariant2(Sub32):
    icon_id = 'document-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'content'
    categories = ('content', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Rounded document with two left-aligned lines, the lower line shorter. Construction reference: file."""
        box(self, 'page', 4, 2, 28, 30, 3)
        self.add_line('line-1', (12, 12), (20, 12))
        self.add_line('line-2', (12, 21), (15, 21))

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
