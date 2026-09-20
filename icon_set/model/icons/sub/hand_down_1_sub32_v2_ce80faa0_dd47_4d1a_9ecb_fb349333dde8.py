"""Independent 32px profile of hand-down-1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'ce80faa0-dd47-4d1a-9ecb-fb349333dde8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/hand down 1_ce80faa0-dd47-4d1a-9ecb-fb349333dde8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ce80faa0-dd47-4d1a-9ecb-fb349333dde8', 'pictographic-primitives/state/hand down 1_ce80faa0-dd47-4d1a-9ecb-fb349333dde8.svg'),)
PROFILE_SOURCE_KEYS = ('solo/hand-down-1',)
SOLO_SOURCE_ICON_IDS = ('hand-down-1',)
REFERENCE_EXPORT_SHA256 = 'fb4623487415fddfd564be9944deab4c5d09d02d5f1924be5c7ac64fa58eb37d'

class DrawingVariant2(Sub32):
    icon_id = 'hand-down-1-sub32-v2'
    variant_of = 'hand-down-1-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Downward diagonal pointing hand with extended finger, curved back, folded thumb and open wrist. Construction reference: hand."""
        self.add_bezier('back', (30, 4), ((26, 7), (22, 7), (20, 7)))
        self.add_bezier('upper', (20, 7), ((13, 7), (2, 12), (2, 15)))
        self.add_bezier('thumb-round', (2, 15), ((2, 18), (3, 19), (5, 19)))
        self.add_line('thumb-inner', (5, 19), (13, 16))
        self.add_line('finger-left', (13, 16), (7, 25))
        self.add_bezier('tip', (7, 25), ((6, 27), (7, 28), (9, 28)))
        self.add_line('finger-base', (9, 28), (15, 28))
        self.add_line('finger-right', (15, 28), (30, 10))
        self.add_contour('hand', 'back', 'upper', 'thumb-round', 'thumb-inner', 'finger-left', 'tip', 'finger-base', 'finger-right')

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
