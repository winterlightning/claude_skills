"""Independent 32px profile of diagonal-paintbrush-with-curved-bristles.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'dc5549d8-9b05-4532-8ed4-ef18efdf1b0f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/design/brush_dc5549d8-9b05-4532-8ed4-ef18efdf1b0f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('dc5549d8-9b05-4532-8ed4-ef18efdf1b0f', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/brush_dc5549d8-9b05-4532-8ed4-ef18efdf1b0f.svg'), ('a0a41169-49c3-4086-a686-b84d4a7eeb92', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/brush_a0a41169-49c3-4086-a686-b84d4a7eeb92.svg'))
PROFILE_SOURCE_KEYS = ('solo/diagonal-paintbrush-with-curved-bristles',)
SOLO_SOURCE_ICON_IDS = ('diagonal-paintbrush-with-curved-bristles',)
REFERENCE_EXPORT_SHA256 = 'eb6248c50044d536c9f23dee3c893cfc9dd5394b08b169fc95148cff18defc3a'

class DrawingVariant2(Sub32):
    icon_id = 'diagonal-paintbrush-with-curved-bristles-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'design'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Diagonal paintbrush with rounded handle, diagonal ferrule seam and pointed curved bristles. Construction reference: paintbrush."""
        self.add_line('handle-l', (12, 13), (22, 3))
        self.add_bezier('tip-l', (22, 3), ((23, 2), (24, 2), (25, 2)))
        self.add_arc('tip-r', (25, 2), (30, 7), radius_x=5)
        self.add_bezier('tip-end', (30, 7), ((30, 9), (29, 10), (28, 11)))
        self.add_line('handle-r', (28, 11), (19, 20))
        self.add_line('seam', (19, 20), (12, 13))
        self.add_contour('handle', 'handle-l', 'tip-l', 'tip-r', 'tip-end', 'handle-r', 'seam', closed=True)
        self.add_bezier('bristles-l', (12, 13), ((4, 12), (7, 25), (2, 30)))
        self.add_bezier('bristles-base', (2, 30), ((13, 30), (23, 28), (19, 20)))
        self.add_contour('bristles', 'bristles-l', 'bristles-base')
        self.relate('connect', 'bristles', 'handle')

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
