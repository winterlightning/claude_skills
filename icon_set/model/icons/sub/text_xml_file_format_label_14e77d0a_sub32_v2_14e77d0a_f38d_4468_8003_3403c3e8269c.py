"""Independent 32px profile of text-xml-file-format-label-14e77d0a.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = '14e77d0a-f38d-4468-8003-3403c3e8269c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/dist/text32/text-xml-file-format-label-14e77d0a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('14e77d0a-f38d-4468-8003-3403c3e8269c', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/xml (text)_14e77d0a-f38d-4468-8003-3403c3e8269c.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-xml-file-format-label-14e77d0a',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '9069c9a0be00054f0eae3c807f669f6e29eedd81e819a84d97e9dfaed5418e5e'

class DrawingVariant2(TextSub32):
    icon_id = 'text-xml-file-format-label-14e77d0a-sub32-v2'
    variant_of = 'text-xml-file-format-label-14e77d0a-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 87
    text_ink_bounds = (0, 0, 86, 32)

    def build(self):
        """Shared typeface letter-x-uppercase, letter-m-uppercase, letter-l-uppercase; natural proportions, 32-unit ink height and integer fitted layout. Construction reference: icon_set/typeface/glyphs.json."""
        self.add_line('p1-r1-1', (2, 2), (22, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (22, 2), (2, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (32, 30), (32, 2))
        self.add_line('p3-r1-2', (32, 2), (45, 20))
        self.add_line('p3-r1-3', (45, 20), (58, 2))
        self.add_line('p3-r1-4', (58, 2), (58, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (68, 2), (68, 30))
        self.add_line('p4-r1-2', (68, 30), (84, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)

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
TYPEFACE_GLYPH_IDS = ('letter-x-uppercase', 'letter-m-uppercase', 'letter-l-uppercase')
