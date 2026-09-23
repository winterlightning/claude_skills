"""Independent 32px profile of link-interlocking.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'a1310a44-a79e-47db-836c-4e40111ae679'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/link_a1310a44-a79e-47db-836c-4e40111ae679.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a1310a44-a79e-47db-836c-4e40111ae679', 'pictographic-primitives/symbol/link_a1310a44-a79e-47db-836c-4e40111ae679.svg'),)
PROFILE_SOURCE_KEYS = ('solo/link-interlocking',)
SOLO_SOURCE_ICON_IDS = ('link-interlocking',)
REFERENCE_EXPORT_SHA256 = 'b153cd513d76822057a281f590fe026c25080249bcd1fc3605a230c69b119a1a'

class DrawingVariant2(Sub32):
    icon_id = 'link-interlocking-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Two diagonal open chain links and a short connecting stroke. Construction reference: link: opposing rounded C links."""
        self.add_arc('lower', (6, 12), (20, 26), radius_x=10, large_arc=True, sweep=False)
        self.add_arc('upper', (12, 6), (26, 20), radius_x=10, large_arc=True, sweep=True)
        self.add_line('join', (12, 20), (20, 12))

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
