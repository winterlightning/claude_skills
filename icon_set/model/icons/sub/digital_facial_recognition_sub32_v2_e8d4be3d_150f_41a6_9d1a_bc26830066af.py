"""Independent 32px profile of digital-facial-recognition.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'e8d4be3d-150f-41a6-9d1a-bc26830066af'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/deepfake_e8d4be3d-150f-41a6-9d1a-bc26830066af.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e8d4be3d-150f-41a6-9d1a-bc26830066af', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/deepfake_e8d4be3d-150f-41a6-9d1a-bc26830066af.svg'),)
PROFILE_SOURCE_KEYS = ('solo/digital-facial-recognition',)
SOLO_SOURCE_ICON_IDS = ('digital-facial-recognition',)
REFERENCE_EXPORT_SHA256 = 'e827b403f0f2d98ad6e17a3c029a6b96aa2d7c5f71feae73879022078538d516'

class DrawingVariant2(Sub32):
    icon_id = 'digital-facial-recognition-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
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
