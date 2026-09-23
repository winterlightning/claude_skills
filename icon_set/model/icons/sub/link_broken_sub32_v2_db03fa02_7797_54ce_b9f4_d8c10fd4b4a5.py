"""Independent 32px profile of link-broken.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'db03fa02-7797-54ce-b9f4-d8c10fd4b4a5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/link broken_db03fa02-7797-54ce-b9f4-d8c10fd4b4a5.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('db03fa02-7797-54ce-b9f4-d8c10fd4b4a5', 'pictographic-primitives/interface-essential/link broken_db03fa02-7797-54ce-b9f4-d8c10fd4b4a5.svg'),)
PROFILE_SOURCE_KEYS = ('solo/link-broken',)
SOLO_SOURCE_ICON_IDS = ('link-broken',)
REFERENCE_EXPORT_SHA256 = '80e294c2ee1bcefe095796b4e3262b87a294657bd1638a3a2b04fcb29e95ef3b'

class DrawingVariant2(Sub32):
    icon_id = 'link-broken-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Two open diagonal chain ends and three separate upper-left break rays. Construction reference: link-2-off."""
        self.add_line('upper-a', (16, 9), (21, 4))
        self.add_bezier('upper-b', (21, 4), ((23, 2), (24, 2), (25, 2)))
        self.add_bezier('upper-c', (25, 2), ((28, 2), (30, 4), (30, 7)))
        self.add_bezier('upper-d', (30, 7), ((30, 9), (29, 10), (27, 12)))
        self.add_line('upper-e', (27, 12), (23, 16))
        self.add_contour('upper', 'upper-a', 'upper-b', 'upper-c', 'upper-d', 'upper-e')
        self.add_line('lower-a', (9, 16), (4, 21))
        self.add_bezier('lower-b', (4, 21), ((2, 23), (2, 24), (2, 25)))
        self.add_bezier('lower-c', (2, 25), ((2, 28), (4, 30), (7, 30)))
        self.add_bezier('lower-d', (7, 30), ((9, 30), (10, 29), (12, 27)))
        self.add_line('lower-e', (12, 27), (16, 23))
        self.add_contour('lower', 'lower-a', 'lower-b', 'lower-c', 'lower-d', 'lower-e')
        self.add_line('ray-top', (12, 2), (12, 4))
        self.add_line('ray-diagonal', (3, 3), (5, 5))
        self.add_line('ray-left', (2, 12), (4, 12))

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
