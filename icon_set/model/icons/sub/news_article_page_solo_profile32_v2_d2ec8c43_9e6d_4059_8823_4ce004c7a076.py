"""Independent 32px profile of news-article-page-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'd2ec8c43-9e6d-4059-8823-4ce004c7a076'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/content/newspaper_d2ec8c43-9e6d-4059-8823-4ce004c7a076.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d2ec8c43-9e6d-4059-8823-4ce004c7a076', 'pictographic-primitives/content/newspaper_d2ec8c43-9e6d-4059-8823-4ce004c7a076.svg'), ('d2ec8c43-9e6d-4059-8823-4ce004c7a076', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/content/newspaper_d2ec8c43-9e6d-4059-8823-4ce004c7a076.svg'))
PROFILE_SOURCE_KEYS = ('solo/news-article-page-solo', 'solo/news-article-page-solo-b005-04')
SOLO_SOURCE_ICON_IDS = ('news-article-page-solo', 'news-article-page-solo-b005-04')
REFERENCE_EXPORT_SHA256 = 'd6621b1619d0c960358bcd327148514b5572e5e34dcf89f6af9d83fd5b5f21e3'

class DrawingVariant2(Sub32):
    icon_id = 'news-article-page-solo-profile32-v2'
    variant_of = 'news-article-page-solo-profile32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Clipped-corner page with closed picture panel and both horizontal text lines. Small-size treatment: Combined the picture area into a page header and reduced the body text to one line. Construction reference: file-image: closed picture panel."""
        box(self, 'page', 4, 2, 28, 30, 3)
        self.add_line('header', (4, 12), (28, 12))
        self.relate('connect', 'header', 'page')
        self.add_line('body-text', (12, 22), (20, 22))

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
