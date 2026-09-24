"""Independent 32px profile of luggage.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '0b930759-f290-469b-a412-4c466c1f838c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/luggage_0b930759-f290-469b-a412-4c466c1f838c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0b930759-f290-469b-a412-4c466c1f838c', 'pictographic-primitives/state/luggage_0b930759-f290-469b-a412-4c466c1f838c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/luggage',)
SOLO_SOURCE_ICON_IDS = ('luggage',)
REFERENCE_EXPORT_SHA256 = 'ebd363b1469735de22c8454660bdd205e274b4fdba037a0c5b2b828cebd6e842'

class DrawingVariant2(Sub32):
    icon_id = 'luggage-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Rounded suitcase, raised rectangular handle and two short straight wheel stems. Construction reference: luggage."""
        box(self, 'case', 4, 10, 28, 26, 3)
        self.add_polyline('handle', (11, 10), (11, 2), (21, 2), (21, 10))
        self.relate('connect', 'handle', 'case')
        for i, x in enumerate((9, 23)):
            self.add_line(f'wheel-{i}', (x, 26), (x, 30))
            self.relate('connect', f'wheel-{i}', 'case')

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
