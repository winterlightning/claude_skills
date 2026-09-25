"""Independent 32px profile of balaclava-mask-batch-025-12.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '484cb3fb-0065-4ca7-ac5f-156d807d114c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/criminal_484cb3fb-0065-4ca7-ac5f-156d807d114c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('484cb3fb-0065-4ca7-ac5f-156d807d114c', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/criminal_484cb3fb-0065-4ca7-ac5f-156d807d114c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/balaclava-mask-batch-025-12',)
SOLO_SOURCE_ICON_IDS = ('balaclava-mask-batch-025-12',)
REFERENCE_EXPORT_SHA256 = 'c4e86c80d7111839b06cbdba703750f8525d496d58afabdac997f2e29302f882'

class DrawingVariant2(Sub32):
    icon_id = 'balaclava-mask-batch-025-12-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Balaclava mask with complete crossing eye loops, rounded skull, two neck notches and flared lower hem. Construction reference: venetian-mask: coherent enclosing contour and paired curved eye construction."""
        self.add_arc('skull', (2, 16), (30, 16), radius_x=14)
        self.add_line('right', (30, 16), (30, 20))
        self.add_bezier('right-neck', (30, 20), ((30, 22), (28, 24), (26, 25)))
        self.add_line('right-flare', (26, 25), (30, 28))
        self.add_bezier('hem-right', (30, 28), ((30, 30), (24, 30), (16, 30)))
        self.add_bezier('hem-left', (16, 30), ((8, 30), (2, 30), (2, 28)))
        self.add_line('left-flare', (2, 28), (6, 25))
        self.add_bezier('left-neck', (6, 25), ((4, 24), (2, 22), (2, 20)))
        self.add_line('left', (2, 20), (2, 16))
        self.add_contour('mask', 'skull', 'right', 'right-neck', 'right-flare', 'hem-right', 'hem-left', 'left-flare', 'left-neck', 'left', closed=True)
        self.add_bezier('eye-l-top', (16, 16), ((12, 10), (9, 10), (9, 16)))
        self.add_bezier('eye-l-bottom', (9, 16), ((9, 22), (12, 22), (16, 16)))
        self.add_bezier('eye-r-top', (16, 16), ((20, 10), (23, 10), (23, 16)))
        self.add_bezier('eye-r-bottom', (23, 16), ((23, 22), (20, 22), (16, 16)))
        self.add_contour('eyes', 'eye-l-top', 'eye-l-bottom', 'eye-r-top', 'eye-r-bottom', closed=True)

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
