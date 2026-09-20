"""Independent 32px profile of exclamation-point-warning-triangle-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '42f29bd3-1507-484e-98bb-b90c40309892'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/dist/gallery/combination-originals/42f29bd3-1507-484e-98bb-b90c40309892.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('42f29bd3-1507-484e-98bb-b90c40309892', 'icon_set/dist/gallery/combination-originals/42f29bd3-1507-484e-98bb-b90c40309892.svg'),)
PROFILE_SOURCE_KEYS = ('solo/exclamation-point-warning-triangle-solo',)
SOLO_SOURCE_ICON_IDS = ('exclamation-point-warning-triangle-solo',)
REFERENCE_EXPORT_SHA256 = '4527c73c3453bc70aa7b4e7dbbe251d34863d0f19f843b79cde5579688fe0c47'

class DrawingVariant2(Sub32):
    icon_id = 'exclamation-point-warning-triangle-sub32-v2'
    variant_of = 'exclamation-point-warning-triangle-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Warning triangle with a vertical exclamation stem and separate dot. Construction reference: triangle-alert."""
        self.add_polyline('triangle', (16, 2), (30, 30), (2, 30), closed=True)
        self.add_line('stem', (16, 16), (16, 17))
        self.add_dot('dot', (16, 23))

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
