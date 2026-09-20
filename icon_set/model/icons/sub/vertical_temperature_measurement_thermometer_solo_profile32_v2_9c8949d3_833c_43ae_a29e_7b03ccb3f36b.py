"""Independent 32px profile of vertical-temperature-measurement-thermometer-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '9c8949d3-833c-43ae-a29e-7b03ccb3f36b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/thermometer_9c8949d3-833c-43ae-a29e-7b03ccb3f36b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9c8949d3-833c-43ae-a29e-7b03ccb3f36b', 'pictographic-primitives/other/thermometer_9c8949d3-833c-43ae-a29e-7b03ccb3f36b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/vertical-temperature-measurement-thermometer-solo',)
SOLO_SOURCE_ICON_IDS = ('vertical-temperature-measurement-thermometer-solo',)
REFERENCE_EXPORT_SHA256 = '29553c9bd62a6bc2d6b5970ba59b83429952e35800bbea38de40229fab789c2f'

class DrawingVariant2(Sub32):
    icon_id = 'vertical-temperature-measurement-thermometer-solo-profile32-v2'
    variant_of = 'vertical-temperature-measurement-thermometer-solo-profile32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Thermometer with rounded stem, bulb, interior mercury line, bulb dot and two right-side scale ticks. Construction reference: thermometer."""
        self.add_arc('top', (4, 10), (20, 10), radius_x=8)
        self.add_line('right', (20, 10), (20, 19))
        self.add_bezier('bulb-r', (20, 19), ((22, 21), (22, 23), (22, 24)))
        self.add_arc('bulb-bottom', (22, 24), (2, 24), radius_x=10, radius_y=6)
        self.add_bezier('bulb-l', (2, 24), ((2, 23), (2, 21), (4, 19)))
        self.add_line('left', (4, 19), (4, 10))
        self.add_contour('thermometer', 'top', 'right', 'bulb-r', 'bulb-bottom', 'bulb-l', 'left', closed=True)
        self.add_line('mercury', (12, 13), (12, 16))
        self.add_dot('bulb-dot', (12, 23))
        self.add_line('tick-1', (28, 6), (30, 6))
        self.add_line('tick-2', (28, 14), (30, 14))

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
