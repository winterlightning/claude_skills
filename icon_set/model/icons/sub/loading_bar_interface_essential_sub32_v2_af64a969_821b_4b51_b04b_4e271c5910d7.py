"""Independent 32px profile of loading-bar-interface-essential.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'af64a969-821b-4b51-b04b-4e271c5910d7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/loading bar_af64a969-821b-4b51-b04b-4e271c5910d7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('af64a969-821b-4b51-b04b-4e271c5910d7', 'pictographic-primitives/interface-essential/loading bar_af64a969-821b-4b51-b04b-4e271c5910d7.svg'),)
PROFILE_SOURCE_KEYS = ('solo/loading-bar-interface-essential',)
SOLO_SOURCE_ICON_IDS = ('loading-bar-interface-essential',)
REFERENCE_EXPORT_SHA256 = '8dc2090d8469d05f859adf93717c02503a8192b99946f46c21adbf358d600f1d'

class DrawingVariant2(Sub32):
    icon_id = 'loading-bar-interface-essential-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_S
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Horizontal loading capsule with one rising diagonal separator. Construction reference: none."""
        self.add_line('top', (8, 10), (24, 10))
        self.add_arc('right', (24, 10), (24, 22), radius_x=6)
        self.add_line('bottom', (24, 22), (8, 22))
        self.add_arc('left', (8, 22), (8, 10), radius_x=6)
        self.add_contour('capsule', 'top', 'right', 'bottom', 'left', closed=True)
        self.add_line('separator', (12, 22), (20, 10))
        self.relate('connect', 'separator', 'capsule')

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
