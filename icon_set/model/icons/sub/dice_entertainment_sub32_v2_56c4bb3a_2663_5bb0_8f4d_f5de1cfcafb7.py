"""Independent 32px profile of dice-entertainment.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '56c4bb3a-2663-5bb0-8f4d-f5de1cfcafb7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/entertainment/dice_56c4bb3a-2663-5bb0-8f4d-f5de1cfcafb7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('56c4bb3a-2663-5bb0-8f4d-f5de1cfcafb7', 'pictographic-primitives/entertainment/dice_56c4bb3a-2663-5bb0-8f4d-f5de1cfcafb7.svg'),)
PROFILE_SOURCE_KEYS = ('solo/dice-entertainment',)
SOLO_SOURCE_ICON_IDS = ('dice-entertainment',)
REFERENCE_EXPORT_SHA256 = '65cd5fc7a2d62dbf513efd8d82ba848c9fd30f4cb3da305163c379d5ae67f3b7'

class DrawingVariant2(Sub32):
    icon_id = 'dice-entertainment-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'entertainment'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Rounded die with exactly five dot pips. Construction reference: dice-5."""
        box(self, 'die', 2, 2, 30, 30, 5)
        for x, y in [(9, 9), (23, 9), (16, 16), (9, 23), (23, 23)]:
            self.add_dot(f'pip-{x}-{y}', (x, y))

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
