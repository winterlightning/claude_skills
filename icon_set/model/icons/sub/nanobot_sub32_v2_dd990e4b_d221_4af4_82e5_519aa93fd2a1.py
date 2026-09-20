"""Independent 32px profile of nanobot.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'dd990e4b-d221-4af4-82e5-519aa93fd2a1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/nanobot_dd990e4b-d221-4af4-82e5-519aa93fd2a1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('dd990e4b-d221-4af4-82e5-519aa93fd2a1', 'pictographic-primitives/state/nanobot_dd990e4b-d221-4af4-82e5-519aa93fd2a1.svg'),)
PROFILE_SOURCE_KEYS = ('solo/nanobot',)
SOLO_SOURCE_ICON_IDS = ('nanobot',)
REFERENCE_EXPORT_SHA256 = '7ad2a4aedf8e623d264f045f700872f67db3207d773da5b87af2b7f8083f3b0a'

class DrawingVariant2(Sub32):
    icon_id = 'nanobot-sub32-v2'
    variant_of = 'nanobot-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Hexagonal nanobot body, open circular center and two attached lower claws. Construction reference: bot."""
        self.add_polyline('body', (16, 2), (28, 9), (28, 21), (16, 28), (4, 21), (4, 9), closed=True)
        circle(self, 'opening', 16, 14, 4)
        self.add_bezier('claw-l-a', (4, 21), ((3, 23), (2, 24), (2, 26)))
        self.add_bezier('claw-l-b', (2, 26), ((2, 28), (3, 29), (4, 30)))
        self.add_bezier('claw-r-a', (28, 21), ((29, 23), (30, 24), (30, 26)))
        self.add_bezier('claw-r-b', (30, 26), ((30, 28), (29, 29), (28, 30)))
        for side in ('l', 'r'):
            self.add_contour('claw-' + side, 'claw-' + side + '-a', 'claw-' + side + '-b')
            self.relate('connect', 'claw-' + side, 'body')

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
