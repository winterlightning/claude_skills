"""Independent 32px profile of gamepad-dpad-and-button-b06110ec-f282-457a-aacf-23318a701c51.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'b06110ec-f282-457a-aacf-23318a701c51'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/medias/gaming_b06110ec-f282-457a-aacf-23318a701c51.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b06110ec-f282-457a-aacf-23318a701c51', 'pictographic-primitives/medias/gaming_b06110ec-f282-457a-aacf-23318a701c51.svg'),)
PROFILE_SOURCE_KEYS = ('solo/gamepad-dpad-and-button-b06110ec-f282-457a-aacf-23318a701c51',)
SOLO_SOURCE_ICON_IDS = ('gamepad-dpad-and-button-b06110ec-f282-457a-aacf-23318a701c51',)
REFERENCE_EXPORT_SHA256 = '9934ba54fd0ca9c5f69b82ef829f07382dcb65e789b1e35490934e236c5c4d93'

class DrawingVariant2(Sub32):
    icon_id = 'gamepad-dpad-and-button-b06110ec-f282-457a-aacf-23318a701c51-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'medias'
    categories = ('medias', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Game controller with one plus and one dot; symmetric grip silhouette. Construction reference: gamepad."""
        self.add_line('top', (10, 4), (22, 4))
        self.add_bezier('right-upper', (22, 4), ((27, 4), (30, 20), (30, 24)))
        self.add_bezier('right-grip', (30, 24), ((30, 28), (26, 28), (24, 28)))
        self.add_bezier('right-inner', (24, 28), ((21, 28), (21, 23), (18, 23)))
        self.add_line('notch', (18, 23), (14, 23))
        self.add_bezier('left-inner', (14, 23), ((11, 23), (11, 28), (8, 28)))
        self.add_bezier('left-grip', (8, 28), ((6, 28), (2, 28), (2, 24)))
        self.add_bezier('left-upper', (2, 24), ((2, 20), (5, 4), (10, 4)))
        self.add_contour('body', 'top', 'right-upper', 'right-grip', 'right-inner', 'notch', 'left-inner', 'left-grip', 'left-upper', closed=True)
        self.add_line('dpad-h', (11, 13), (15, 13))
        self.add_line('dpad-v', (13, 11), (13, 15))
        self.relate('connect', 'dpad-h', 'dpad-v')
        self.add_dot('button', (21, 13))

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
