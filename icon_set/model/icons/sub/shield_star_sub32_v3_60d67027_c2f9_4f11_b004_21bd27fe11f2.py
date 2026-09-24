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

class DrawingVariant3(Sub32):
    icon_id = 'shield-star-sub32-v3'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'protection'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Shield with a genuine five-point outlined star; upper frame opens around the star. Construction reference: source composition; shared small-size character construction."""
        self.add_polyline('star', (16, 2), (20, 8), (26, 8), (21, 13), (23, 20), (16, 16), (9, 20), (11, 13), (6, 8), (12, 8), (16, 2))
        self.add_line('left', (2, 14), (2, 19))
        self.add_bezier('shield-left', (2, 19), ((2, 26), (10, 28), (16, 30)))
        self.add_bezier('shield-right', (16, 30), ((22, 28), (30, 26), (30, 19)))
        self.add_line('right', (30, 19), (30, 14))
        self.add_contour('shield', 'left', 'shield-left', 'shield-right', 'right')

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
