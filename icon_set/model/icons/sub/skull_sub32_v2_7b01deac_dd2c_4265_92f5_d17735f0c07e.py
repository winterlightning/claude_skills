"""Independent 32px profile of skull.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '7b01deac-dd2c-4265-92f5-d17735f0c07e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/skull_7b01deac-dd2c-4265-92f5-d17735f0c07e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7b01deac-dd2c-4265-92f5-d17735f0c07e', 'pictographic-primitives/interface-essential/skull_7b01deac-dd2c-4265-92f5-d17735f0c07e.svg'), ('85266d86-6f31-4d3b-91ca-d5a232d0c46c', 'pictographic-primitives/interface-essential/skull_85266d86-6f31-4d3b-91ca-d5a232d0c46c.svg'), ('bf02abda-c65a-4ff2-af41-3fdc5c490cc7', 'pictographic-primitives/interface-essential/skull_bf02abda-c65a-4ff2-af41-3fdc5c490cc7.svg'))
PROFILE_SOURCE_KEYS = ('solo/skull', 'solo/skull-85266d86', 'solo/skull-bf02abda')
SOLO_SOURCE_ICON_IDS = ('skull', 'skull-85266d86', 'skull-bf02abda')
REFERENCE_EXPORT_SHA256 = '25b205a3c21b4763f24a7fe4a450a28bf3c3d6bb04cd6302737e3eff5567e46c'

class DrawingVariant2(Sub32):
    icon_id = 'skull-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Open skull with domed cranium, two dot eyes, cheek transitions and three lower tooth strokes. Construction reference: skull."""
        self.add_line('jaw-l', (8, 30), (8, 27))
        self.add_bezier('cheek-l', (8, 27), ((8, 23), (2, 25), (2, 18)))
        self.add_line('side-l', (2, 18), (2, 16))
        self.add_arc('crown', (2, 16), (30, 16), radius_x=14)
        self.add_line('side-r', (30, 16), (30, 18))
        self.add_bezier('cheek-r', (30, 18), ((30, 25), (24, 23), (24, 27)))
        self.add_line('jaw-r', (24, 27), (24, 30))
        self.add_contour('skull', 'jaw-l', 'cheek-l', 'side-l', 'crown', 'side-r', 'cheek-r', 'jaw-r')
        self.add_line('tooth', (16, 28), (16, 30))
        self.add_dot('eye-l', (11, 15))
        self.add_dot('eye-r', (21, 15))

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
