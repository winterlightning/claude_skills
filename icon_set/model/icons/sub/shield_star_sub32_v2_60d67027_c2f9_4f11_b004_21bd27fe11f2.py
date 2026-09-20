"""Independent 32px profile of shield-star.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '60d67027-c2f9-4f11-b004-21bd27fe11f2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/protection/shield star_60d67027-c2f9-4f11-b004-21bd27fe11f2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('60d67027-c2f9-4f11-b004-21bd27fe11f2', 'pictographic-primitives/protection/shield star_60d67027-c2f9-4f11-b004-21bd27fe11f2.svg'),)
PROFILE_SOURCE_KEYS = ('solo/shield-star',)
SOLO_SOURCE_ICON_IDS = ('shield-star',)
REFERENCE_EXPORT_SHA256 = '23557e4569ad216f72d950d2ecca0672700cf127096ad68e6803641b5696365d'

class DrawingVariant2(Sub32):
    icon_id = 'shield-star-sub32-v2'
    variant_of = 'shield-star-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'protection'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Rounded shield containing a five-ray star mark. Construction reference: shield-star: open shield silhouette and central five-point symbol."""
        self.add_bezier('roof-left', (2, 6), ((6, 3), (12, 2), (16, 2)))
        self.add_bezier('roof-right', (16, 2), ((20, 2), (26, 3), (30, 6)))
        self.add_line('right', (30, 6), (30, 15))
        self.add_bezier('base-right', (30, 15), ((30, 22), (23, 28), (16, 30)))
        self.add_bezier('base-left', (16, 30), ((9, 28), (2, 22), (2, 15)))
        self.add_line('left', (2, 15), (2, 6))
        self.add_contour('shield', 'roof-left', 'roof-right', 'right', 'base-right', 'base-left', 'left', closed=True)
        for i, p in enumerate(((16, 9), (22, 13), (20, 20), (12, 20), (10, 13))):
            self.add_line(f'ray-{i}', (16, 15), p)
            for j in range(i):
                self.relate('connect', f'ray-{i}', f'ray-{j}')

def box(s, n, l, t, r, b, k=3):
    if k == 0:
        s.add_polyline(n, (l, t), (r, t), (r, b), (l, b), (l, t))
        return
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
