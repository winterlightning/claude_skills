"""Independent 32px profile of trash.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '2501b9fd-9e68-4968-a930-e114d61b1fc2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/trash_2501b9fd-9e68-4968-a930-e114d61b1fc2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2501b9fd-9e68-4968-a930-e114d61b1fc2', 'pictographic-primitives/state/trash_2501b9fd-9e68-4968-a930-e114d61b1fc2.svg'), ('809378b8-e0d0-4cfb-9e28-6f64d31ac4f8', 'pictographic-primitives/symbol/trash_809378b8-e0d0-4cfb-9e28-6f64d31ac4f8.svg'), ('5e0c6d19-547e-46f0-8ec6-c837972fb3f0', 'pictographic-primitives/state/trash_5e0c6d19-547e-46f0-8ec6-c837972fb3f0.svg'))
PROFILE_SOURCE_KEYS = ('solo/trash', 'solo/trash-809378b8', 'solo/trash-state')
SOLO_SOURCE_ICON_IDS = ('trash', 'trash-809378b8', 'trash-state')
REFERENCE_EXPORT_SHA256 = 'ed23ae1a3b6974bca427a959faf7c6b37679d30c452424990e72e5b4fb6dd1f3'

class DrawingVariant2(Sub32):
    icon_id = 'trash-sub32-v2'
    variant_of = 'trash-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Trash can with separate-width lid, central lid stem, straight body sides and rounded lower corners. Construction reference: trash."""
        self.add_line('lid', (4, 10), (28, 10))
        self.add_line('handle', (16, 2), (16, 10))
        self.relate('connect', 'lid', 'handle')
        self.add_line('right', (26, 10), (26, 26))
        self.add_arc('br', (26, 26), (22, 30), radius_x=4)
        self.add_line('base', (22, 30), (10, 30))
        self.add_arc('bl', (10, 30), (6, 26), radius_x=4)
        self.add_line('left', (6, 26), (6, 10))
        self.add_contour('body', 'right', 'br', 'base', 'bl', 'left')
        self.relate('connect', 'lid', 'body')

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
