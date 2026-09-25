"""Independent 32px profile of upward-hand-pointer-batch-024-07.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'eab3080c-0a62-4d7b-b2b0-750ba686504c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/hand point 1_eab3080c-0a62-4d7b-b2b0-750ba686504c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('eab3080c-0a62-4d7b-b2b0-750ba686504c', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/hand point 1_eab3080c-0a62-4d7b-b2b0-750ba686504c.svg'), ('82734f7a-f16b-4ab7-8833-a4322d4cbd4b', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/hand point_82734f7a-f16b-4ab7-8833-a4322d4cbd4b.svg'))
PROFILE_SOURCE_KEYS = ('solo/upward-hand-pointer-batch-024-07', 'solo/upward-hand-pointer-batch-024-08')
SOLO_SOURCE_ICON_IDS = ('upward-hand-pointer-batch-024-07', 'upward-hand-pointer-batch-024-08')
REFERENCE_EXPORT_SHA256 = 'aa934776c74bb68e01a16f3a104dde6a87e4430f41e0f1465eea3d92e1c7d917'

class DrawingVariant2(Sub32):
    icon_id = 'upward-hand-pointer-batch-024-07-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Upward index-finger pointer with rounded finger, folded palm, thumb and open wrist. Construction reference: hand."""
        self.add_line('index-l', (13, 17), (13, 6))
        self.add_arc('index-top', (13, 6), (21, 6), radius_x=4)
        self.add_line('index-r', (21, 6), (21, 14))
        self.add_bezier('palm', (21, 14), ((26, 14), (28, 18), (28, 22)))
        self.add_line('wrist-r', (28, 22), (28, 30))
        self.add_contour('right', 'index-l', 'index-top', 'index-r', 'palm', 'wrist-r')
        self.add_line('thumb-inner', (13, 17), (9, 13))
        self.add_bezier('thumb-top', (9, 13), ((6, 10), (4, 12), (4, 15)))
        self.add_bezier('thumb-lower', (4, 15), ((4, 17), (5, 18), (7, 20)))
        self.add_line('wrist-l', (7, 20), (15, 30))
        self.add_contour('left', 'thumb-inner', 'thumb-top', 'thumb-lower', 'wrist-l')
        self.relate('connect', 'left', 'right')

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
