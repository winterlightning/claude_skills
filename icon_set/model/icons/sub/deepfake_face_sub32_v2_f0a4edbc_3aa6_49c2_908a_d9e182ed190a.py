"""Independent 32px profile of deepfake-face.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'f0a4edbc-3aa6-49c2-908a-d9e182ed190a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/deep fake_f0a4edbc-3aa6-49c2-908a-d9e182ed190a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f0a4edbc-3aa6-49c2-908a-d9e182ed190a', 'pictographic-primitives/symbol/deep fake_f0a4edbc-3aa6-49c2-908a-d9e182ed190a.svg'),)
PROFILE_SOURCE_KEYS = ('solo/deepfake-face',)
SOLO_SOURCE_ICON_IDS = ('deepfake-face',)
REFERENCE_EXPORT_SHA256 = '96aca030dc9e0bba6e269d766dba0eabf78e5840774642a171fea63aac10b37e'

class DrawingVariant2(Sub32):
    icon_id = 'deepfake-face-sub32-v2'
    variant_of = 'deepfake-face-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbols/standalone'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Rounded facial-scan mask, crossing vertical/horizontal guides and curved smile. Construction reference: scan-face."""
        self.add_arc('top', (4, 14), (28, 14), radius_x=12)
        self.add_line('right', (28, 14), (28, 18))
        self.add_arc('jaw', (28, 18), (4, 18), radius_x=12)
        self.add_line('left', (4, 18), (4, 14))
        self.add_contour('face', 'top', 'right', 'jaw', 'left', closed=True)
        self.add_line('horizontal', (5, 12), (27, 12))
        self.relate('connect', 'horizontal', 'face')
        self.add_line('vertical', (16, 2), (16, 17))
        self.relate('connect', 'vertical', 'face')
        self.relate('connect', 'horizontal', 'vertical')
        self.add_arc('smile', (12, 22), (20, 22), radius_x=6, sweep=False)

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
