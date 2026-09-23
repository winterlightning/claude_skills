"""Independent 32px profile of file-emails.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '5bd8438c-94c0-4326-8e22-5188c667350d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/emails/file_5bd8438c-94c0-4326-8e22-5188c667350d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5bd8438c-94c0-4326-8e22-5188c667350d', 'pictographic-primitives/emails/file_5bd8438c-94c0-4326-8e22-5188c667350d.svg'), ('ee647811-20d2-4d87-9000-0d11db8aa255', 'pictographic-primitives/files/document_ee647811-20d2-4d87-9000-0d11db8aa255.svg'))
PROFILE_SOURCE_KEYS = ('solo/file-emails', 'solo/document-files')
SOLO_SOURCE_ICON_IDS = ('file-emails', 'document-files')
REFERENCE_EXPORT_SHA256 = '69667b7d09f1c2eb89fdde47e5fed35df35e783a156002aaee93d6d92a54cf6e'

class DrawingVariant2(Sub32):
    icon_id = 'file-emails-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'emails'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Square-corner page with clipped top-right and exactly two lines. Construction reference: file-text."""
        self.add_polyline('page', (4, 2), (20, 2), (28, 10), (28, 30), (4, 30), closed=True)
        for y in (14, 22):
            self.add_line(f'text-{y}', (12, y), (20, y))

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
