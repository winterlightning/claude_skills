"""Independent 32px profile of robot-3b4771f4.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '3b4771f4-de72-4538-b549-43276caa2ff1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/artificial-intelligence/robot_3b4771f4-de72-4538-b549-43276caa2ff1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3b4771f4-de72-4538-b549-43276caa2ff1', 'pictographic-primitives/artificial-intelligence/robot_3b4771f4-de72-4538-b549-43276caa2ff1.svg'), ('233b4b91-c66d-47bb-8540-9a5b8f63230e', 'pictographic-primitives/artificial-intelligence/robot_233b4b91-c66d-47bb-8540-9a5b8f63230e.svg'))
PROFILE_SOURCE_KEYS = ('solo/robot-3b4771f4', 'solo/robot-artificial-intelligence')
SOLO_SOURCE_ICON_IDS = ('robot-3b4771f4', 'robot-artificial-intelligence')
REFERENCE_EXPORT_SHA256 = 'e8045c3d77e1b5a76dd3c471742c92d3976285f48fc3a2b95d7f608881c1f4fa'

class DrawingVariant2(Sub32):
    icon_id = 'robot-3b4771f4-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'artificial-intelligence'
    categories = ('artificial-intelligence', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Rounded robot head, two antenna stems and two short vertical eyes. Construction reference: bot."""
        box(self, 'head', 2, 10, 30, 30, 6)
        for x in (10, 22):
            self.add_line(f'antenna-{x}', (x, 2), (x, 10))
            self.relate('connect', f'antenna-{x}', 'head')
        for x in (11, 21):
            self.add_line(f'eye-{x}', (x, 18), (x, 22))

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
