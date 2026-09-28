"""Independent 32px profile of pen-50e47373.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '50e47373-cb10-491f-a428-767a767f9cef'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/design/pen_50e47373-cb10-491f-a428-767a767f9cef.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('50e47373-cb10-491f-a428-767a767f9cef', 'pictographic-primitives/design/pen_50e47373-cb10-491f-a428-767a767f9cef.svg'), ('7ee2f930-e642-4295-aaa3-5150e3fc91e5', 'pictographic-primitives/design/pen_7ee2f930-e642-4295-aaa3-5150e3fc91e5.svg'))
PROFILE_SOURCE_KEYS = ('solo/pen-50e47373', 'solo/pen-7ee2f930')
SOLO_SOURCE_ICON_IDS = ('pen-50e47373', 'pen-7ee2f930')
REFERENCE_EXPORT_SHA256 = '4ed27c71c7372ed32ce2a47ac5f724620e282c674712c89a5fa989db8f2253d6'

class DrawingVariant2(Sub32):
    icon_id = 'pen-50e47373-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'design'
    categories = ('design', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Diagonal pencil with rounded cap, cap seam, pointed tip and tip seam. Construction reference: pencil."""
        self.add_line('upper', (6, 20), (21, 5))
        self.add_bezier('cap-upper', (21, 5), ((23, 3), (23, 2), (25, 2)))
        self.add_arc('cap-crown', (25, 2), (30, 7), radius_x=5)
        self.add_bezier('cap-lower', (30, 7), ((30, 9), (29, 11), (27, 13)))
        self.add_polyline('lower', (27, 13), (13, 27), (2, 30), (6, 20))
        self.add_contour('cap', 'upper', 'cap-upper', 'cap-crown', 'cap-lower')
        self.relate('connect', 'cap', 'lower')
        self.add_line('cap-seam', (18, 8), (25, 15))
        self.relate('connect', 'cap-seam', 'cap')
        self.relate('connect', 'cap-seam', 'lower')
        self.add_line('tip-seam', (6, 20), (13, 27))
        self.relate('connect', 'tip-seam', 'cap')
        self.relate('connect', 'tip-seam', 'lower')

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
