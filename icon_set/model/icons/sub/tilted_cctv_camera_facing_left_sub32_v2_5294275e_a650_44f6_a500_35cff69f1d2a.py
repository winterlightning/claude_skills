"""Independent 32px profile of tilted-cctv-camera-facing-left.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '5294275e-a650-44f6-a500-35cff69f1d2a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/protection/surveillance cctv 1_5294275e-a650-44f6-a500-35cff69f1d2a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5294275e-a650-44f6-a500-35cff69f1d2a', 'pictographic-primitives/protection/surveillance cctv 1_5294275e-a650-44f6-a500-35cff69f1d2a.svg'),)
PROFILE_SOURCE_KEYS = ('solo/tilted-cctv-camera-facing-left',)
SOLO_SOURCE_ICON_IDS = ('tilted-cctv-camera-facing-left',)
REFERENCE_EXPORT_SHA256 = 'c9f751e8d2093e41aeb84b03566b8b6f5c6e01a1ca620823906eebced1853faa'

class DrawingVariant2(Sub32):
    icon_id = 'tilted-cctv-camera-facing-left-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'protection'
    categories = ('protection', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Left-facing tilted CCTV housing, detached front marker and curved wall bracket. Construction reference: cctv."""
        self.add_polyline('housing', (8, 10), (26, 4), (30, 16), (12, 22), closed=True)
        self.add_line('front', (2, 14), (4, 21))
        self.add_line('bracket-stem', (21, 19), (21, 25))
        self.add_arc('bracket-turn', (21, 25), (24, 28), radius_x=3, sweep=False)
        self.add_line('bracket-end', (24, 28), (30, 28))
        self.add_contour('bracket', 'bracket-stem', 'bracket-turn', 'bracket-end')
        self.relate('connect', 'housing', 'bracket')

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
