"""Independent 32px profile of spiraling-tornado.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'dc2f84e2-1e3c-4253-9ea5-be6ccd2c901f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/weather/hurricane_dc2f84e2-1e3c-4253-9ea5-be6ccd2c901f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('dc2f84e2-1e3c-4253-9ea5-be6ccd2c901f', 'pictographic-primitives/weather/hurricane_dc2f84e2-1e3c-4253-9ea5-be6ccd2c901f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/spiraling-tornado',)
SOLO_SOURCE_ICON_IDS = ('spiraling-tornado',)
REFERENCE_EXPORT_SHA256 = 'ff0341573f02b158b31d0b8fe7b6f66b34d300184969dc5471bc6b0582391c10'

class DrawingVariant2(Sub32):
    icon_id = 'spiraling-tornado-sub32-v2'
    variant_of = 'spiraling-tornado-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/weather'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Spiraling tornado with a continuous upper coil and two separate narrowing lower curves. Construction reference: tornado."""
        self.add_bezier('a', (22, 2), ((11, 2), (2, 5), (2, 10)))
        self.add_bezier('b', (2, 10), ((2, 14), (8, 16), (16, 16)))
        self.add_bezier('c', (16, 16), ((24, 16), (30, 14), (30, 11)))
        self.add_bezier('d', (30, 11), ((30, 9), (22, 9), (19, 9)))
        self.add_bezier('e', (19, 9), ((16, 9), (14, 10), (14, 11)))
        self.add_contour('coil', 'a', 'b', 'c', 'd', 'e')
        self.add_bezier('middle', (8, 22), ((12, 23), (20, 23), (24, 22)))
        self.add_bezier('bottom-l', (12, 29), ((13, 30), (14, 30), (16, 30)))
        self.add_bezier('bottom-r', (16, 30), ((18, 30), (19, 30), (20, 29)))
        self.add_contour('bottom', 'bottom-l', 'bottom-r')

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
