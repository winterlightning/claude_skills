"""Independent 32px profile of human-eye-160ed52a.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '160ed52a-22e5-47c1-8202-7d7e9f91f1ec'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/health/eye_160ed52a-22e5-47c1-8202-7d7e9f91f1ec.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('160ed52a-22e5-47c1-8202-7d7e9f91f1ec', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/eye_160ed52a-22e5-47c1-8202-7d7e9f91f1ec.svg'),)
PROFILE_SOURCE_KEYS = ('solo/human-eye-160ed52a',)
SOLO_SOURCE_ICON_IDS = ('human-eye-160ed52a',)
REFERENCE_EXPORT_SHA256 = '044e2ea9d57ea076a782adc06fc5517ca825163141babecee730f0f30d8070c2'

class DrawingVariant2(Sub32):
    icon_id = 'human-eye-160ed52a-sub32-v2'
    variant_of = 'human-eye-160ed52a-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'health'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Symmetric almond eye and round iris; preserve the open iris hole. Construction reference: eye."""
        self.add_bezier('upper-left', (2, 16), ((5, 10), (10, 4), (16, 4)))
        self.add_bezier('upper-right', (16, 4), ((22, 4), (27, 10), (30, 16)))
        self.add_bezier('lower-right', (30, 16), ((27, 22), (22, 28), (16, 28)))
        self.add_bezier('lower-left', (16, 28), ((10, 28), (5, 22), (2, 16)))
        self.add_contour('eye', 'upper-left', 'upper-right', 'lower-right', 'lower-left', closed=True)
        circle(self, 'iris', 16, 16, 5)

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
