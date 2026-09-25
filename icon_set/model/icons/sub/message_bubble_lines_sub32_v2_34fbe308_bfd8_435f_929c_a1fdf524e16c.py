"""Independent 32px profile of message-bubble-lines.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '34fbe308-bfd8-435f-929c-a1fdf524e16c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/message lines_34fbe308-bfd8-435f-929c-a1fdf524e16c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('34fbe308-bfd8-435f-929c-a1fdf524e16c', 'pictographic-primitives/symbol/message lines_34fbe308-bfd8-435f-929c-a1fdf524e16c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/message-bubble-lines',)
SOLO_SOURCE_ICON_IDS = ('message-bubble-lines',)
REFERENCE_EXPORT_SHA256 = '4cba4c38ccf41d2b8d3d4a508e1d401bcd0443c6f091fe1d5d6440bb24eab9c5'

class DrawingVariant2(Sub32):
    icon_id = 'message-bubble-lines-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Rounded rectangular speech bubble, lower-left tail and two equal lines. Construction reference: message-square."""
        self.add_line('top', (5, 2), (27, 2))
        self.add_arc('tr', (27, 2), (30, 5), radius_x=3)
        self.add_line('right', (30, 5), (30, 23))
        self.add_arc('br', (30, 23), (27, 26), radius_x=3)
        self.add_polyline('tail', (27, 26), (13, 26), (7, 30), (7, 26), (5, 26))
        self.add_arc('bl', (5, 26), (2, 23), radius_x=3)
        self.add_line('left', (2, 23), (2, 5))
        self.add_arc('tl', (2, 5), (5, 2), radius_x=3)
        self.add_contour('shell', 'bl', 'left', 'tl', 'top', 'tr', 'right', 'br')
        self.relate('connect', 'shell', 'tail')
        for y in (10, 18):
            self.add_line(f'text-{y}', (10, y), (22, y))

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
