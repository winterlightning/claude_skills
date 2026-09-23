"""Independent 32px profile of rounded-square-microchip-with-eight-pins.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '91baab07-2434-44bf-b597-92da30445815'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/electronics/safety helmet mine_91baab07-2434-44bf-b597-92da30445815.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('91baab07-2434-44bf-b597-92da30445815', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/electronics/safety helmet mine_91baab07-2434-44bf-b597-92da30445815.svg'),)
PROFILE_SOURCE_KEYS = ('solo/rounded-square-microchip-with-eight-pins',)
SOLO_SOURCE_ICON_IDS = ('rounded-square-microchip-with-eight-pins',)
REFERENCE_EXPORT_SHA256 = '915ab20b05f26b0889089a862d5a9bbbdf3f451a453d3c44ecafce85a0ef26ff'

class DrawingVariant2(Sub32):
    icon_id = 'rounded-square-microchip-with-eight-pins-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/electronics'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Rounded microchip body with exactly two pins on each of four sides. Construction reference: cpu."""
        box(self, 'body', 6, 6, 26, 26, 3)
        for i, v in enumerate((11, 21)):
            for side, a, b in [('top', (v, 2), (v, 6)), ('bottom', (v, 26), (v, 30)), ('left', (2, v), (6, v)), ('right', (26, v), (30, v))]:
                name = f'{side}-{i}'
                self.add_line(name, a, b)
                self.relate('connect', name, 'body')

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
