"""Independent 32px profile of retro-game-controller.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'dd63e94e-812e-44c7-92f2-bbfc699f5e98'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/technology/game_dd63e94e-812e-44c7-92f2-bbfc699f5e98.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('dd63e94e-812e-44c7-92f2-bbfc699f5e98', 'pictographic-primitives/technology/game_dd63e94e-812e-44c7-92f2-bbfc699f5e98.svg'),)
PROFILE_SOURCE_KEYS = ('solo/retro-game-controller',)
SOLO_SOURCE_ICON_IDS = ('retro-game-controller',)
REFERENCE_EXPORT_SHA256 = '1ca60569a79b97e54d4f99c3c09e34c4f41c334c81f75ed74689eb1e8e52c596'

class DrawingVariant2(Sub32):
    icon_id = 'retro-game-controller-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'technology'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Tilted retro controller with diagonal curved body, plus pad and two separate round buttons. Construction reference: gamepad-2."""
        self.add_bezier('a', (22, 4), ((26, 4), (30, 7), (30, 12)))
        self.add_bezier('b', (30, 12), ((30, 19), (27, 24), (22, 25)))
        self.add_bezier('c', (22, 25), ((17, 26), (15, 28), (10, 28)))
        self.add_bezier('d', (10, 28), ((5, 28), (2, 25), (2, 20)))
        self.add_bezier('e', (2, 20), ((2, 15), (5, 12), (10, 10)))
        self.add_bezier('f', (10, 10), ((15, 8), (17, 4), (22, 4)))
        self.add_contour('body', 'a', 'b', 'c', 'd', 'e', 'f', closed=True)
        self.add_line('pad-h', (9, 19), (13, 19))
        self.add_line('pad-v', (11, 17), (11, 21))
        self.relate('connect', 'pad-h', 'pad-v')
        self.add_dot('button-a', (22, 11))
        self.add_dot('button-b', (22, 18))

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
