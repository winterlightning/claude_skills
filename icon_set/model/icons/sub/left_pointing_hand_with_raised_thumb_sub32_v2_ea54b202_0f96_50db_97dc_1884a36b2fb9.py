"""Independent 32px profile of left-pointing-hand-with-raised-thumb.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'ea54b202-0f96-50db-97dc-1884a36b2fb9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/hand pointer left_ea54b202-0f96-50db-97dc-1884a36b2fb9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ea54b202-0f96-50db-97dc-1884a36b2fb9', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/hand pointer left_ea54b202-0f96-50db-97dc-1884a36b2fb9.svg'),)
PROFILE_SOURCE_KEYS = ('solo/left-pointing-hand-with-raised-thumb',)
SOLO_SOURCE_ICON_IDS = ('left-pointing-hand-with-raised-thumb',)
REFERENCE_EXPORT_SHA256 = '450f361bcf4114b68574b09bd2db4032edd9d4e337422557a2efbd3b03f631bc'

class DrawingVariant2(Sub32):
    icon_id = 'left-pointing-hand-with-raised-thumb-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    categories = ('interface-essential', 'state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Left-pointing index finger, raised thumb and THREE distinct folded-finger scallops. Construction reference: none."""
        self.add_line('index-top', (6, 10), (18, 10))
        self.add_bezier('thumb', (18, 10), ((11, 5), (16, 2), (18, 2)))
        self.add_bezier('back', (18, 2), ((24, 2), (30, 11), (30, 17)))
        self.add_bezier('palm', (30, 17), ((30, 27), (27, 30), (23, 30)))
        self.add_line('base', (23, 30), (16, 30))
        for i in range(3):
            self.add_arc(f'fold-{i}', (16, 30 - 4 * i), (16, 26 - 4 * i), radius_x=2)
        self.add_line('index-base', (16, 18), (6, 18))
        self.add_arc('tip', (6, 18), (6, 10), radius_x=4)
        self.add_contour('hand', 'index-top', 'thumb', 'back', 'palm', 'base', 'fold-0', 'fold-1', 'fold-2', 'index-base', 'tip', closed=True)

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
