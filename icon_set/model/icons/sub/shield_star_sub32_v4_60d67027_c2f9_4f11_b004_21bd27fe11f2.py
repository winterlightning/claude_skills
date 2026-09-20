"""Independent 32px profile of shield-star.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._tall_base import SideSub32Exception
SOURCE_ICON_ID = '60d67027-c2f9-4f11-b004-21bd27fe11f2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/protection/shield star_60d67027-c2f9-4f11-b004-21bd27fe11f2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('60d67027-c2f9-4f11-b004-21bd27fe11f2', 'pictographic-primitives/protection/shield star_60d67027-c2f9-4f11-b004-21bd27fe11f2.svg'),)
PROFILE_SOURCE_KEYS = ('solo/shield-star',)
SOLO_SOURCE_ICON_IDS = ('shield-star',)
REFERENCE_EXPORT_SHA256 = '23557e4569ad216f72d950d2ecca0672700cf127096ad68e6803641b5696365d'

class DrawingVariant4(SideSub32Exception):
    icon_id = 'shield-star-sub32-v4'
    variant_of = 'shield-star-sub32-v3'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'protection'
    profile_source_keys = PROFILE_SOURCE_KEYS
    canvas_width = 32
    canvas_height = 48
    canvas_width = 32
    canvas_height = 48
    canvas_width = 32
    canvas_height = 48
    canvas_width = 32
    canvas_height = 48
    canvas_width = 32
    canvas_height = 48
    canvas_width = 32
    canvas_height = 48
    canvas_width = 32
    canvas_height = 48
    canvas_width = 32
    canvas_height = 48

    def build(self):
        """Complete closed shield with curved crown, pointed base and one five-point star fully inside. Construction reference: Original source composition; clean contour construction."""
        self.add_bezier('crown-l', (2, 6), ((7, 4), (12, 2), (16, 2)))
        self.add_bezier('crown-r', (16, 2), ((20, 2), (25, 4), (30, 6)))
        self.add_line('right', (30, 6), (30, 26))
        self.add_bezier('lower-r', (30, 26), ((30, 36), (24, 42), (16, 46)))
        self.add_bezier('lower-l', (16, 46), ((8, 42), (2, 36), (2, 26)))
        self.add_line('left', (2, 26), (2, 6))
        self.add_contour('shield', 'crown-l', 'crown-r', 'right', 'lower-r', 'lower-l', 'left')
        self.add_polyline('star', (16, 12), (19, 20), (23, 20), (20, 25), (22, 32), (16, 28), (10, 32), (12, 25), (9, 20), (13, 20), (16, 12))

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
