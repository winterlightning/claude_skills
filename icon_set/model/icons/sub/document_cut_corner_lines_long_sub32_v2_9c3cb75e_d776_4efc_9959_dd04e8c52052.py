"""Independent 32px profile of document-cut-corner-lines-long.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '9c3cb75e-d776-4efc-9959-dd04e8c52052'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/text file_9c3cb75e-d776-4efc-9959-dd04e8c52052.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9c3cb75e-d776-4efc-9959-dd04e8c52052', 'pictographic-primitives/symbol/text file_9c3cb75e-d776-4efc-9959-dd04e8c52052.svg'),)
PROFILE_SOURCE_KEYS = ('solo/document-cut-corner-lines-long',)
SOLO_SOURCE_ICON_IDS = ('document-cut-corner-lines-long',)
REFERENCE_EXPORT_SHA256 = '03dfa3386ea87fbe394118cf50a1713093725dc553f5625f77d08f242ce53976'

class DrawingVariant2(Sub32):
    icon_id = 'document-cut-corner-lines-long-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Document, clipped top-right corner and exactly two text lines. Construction reference: file-text."""
        self.add_line('top', (8, 2), (20, 2))
        self.add_polyline('corner', (20, 2), (28, 10), (28, 26))
        self.add_arc('br', (28, 26), (24, 30), radius_x=4)
        self.add_line('base', (24, 30), (8, 30))
        self.add_arc('bl', (8, 30), (4, 26), radius_x=4)
        self.add_line('left', (4, 26), (4, 6))
        self.add_arc('tl', (4, 6), (8, 2), radius_x=4)
        self.add_contour('page-round', 'br', 'base', 'bl', 'left', 'tl', 'top')
        self.relate('connect', 'page-round', 'corner')
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
