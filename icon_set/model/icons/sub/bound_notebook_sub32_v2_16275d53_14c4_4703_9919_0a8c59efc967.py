"""Independent 32px profile of bound-notebook.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '16275d53-14c4-4703-9919-0a8c59efc967'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/content/archive_16275d53-14c4-4703-9919-0a8c59efc967.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('16275d53-14c4-4703-9919-0a8c59efc967', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/content/archive_16275d53-14c4-4703-9919-0a8c59efc967.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bound-notebook',)
SOLO_SOURCE_ICON_IDS = ('bound-notebook',)
REFERENCE_EXPORT_SHA256 = '852464449953dbbeaf09e56dd7ab7126f3a1b74ff57760b92c53481c496b579b'

class DrawingVariant2(Sub32):
    icon_id = 'bound-notebook-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'content'
    categories = ('primitives', 'content')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Rounded bound notebook, vertical binding and all three binding marks. Small-size treatment: Reduced three binding marks to two. Construction reference: notebook: binding and closed page."""
        box(self, 'book', 6, 2, 30, 30, 3)
        for i, y in enumerate((11, 21)):
            self.add_line(f'binding-{i}', (2, y), (12, y))
            self.relate('connect', f'binding-{i}', 'book')

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
