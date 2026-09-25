"""Independent 32px profile of pin.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '76f7fdb5-5122-45e4-a53b-be1029308735'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/pin_76f7fdb5-5122-45e4-a53b-be1029308735.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('76f7fdb5-5122-45e4-a53b-be1029308735', 'pictographic-primitives/interface-essential/pin_76f7fdb5-5122-45e4-a53b-be1029308735.svg'), ('9b4b8603-58f9-4f81-8664-658ab7045658', 'pictographic-primitives/interface-essential/pin_9b4b8603-58f9-4f81-8664-658ab7045658.svg'), ('79f28f0f-6da1-42b3-a142-474d81fe6b26', 'pictographic-primitives/state/pin wave_79f28f0f-6da1-42b3-a142-474d81fe6b26.svg'))
PROFILE_SOURCE_KEYS = ('solo/pin', 'solo/pin-9b4b8603', 'solo/pin-wave')
SOLO_SOURCE_ICON_IDS = ('pin', 'pin-9b4b8603', 'pin-wave')
REFERENCE_EXPORT_SHA256 = '267d1985c489b24572604f32fc408010b1c0590304c66b4756ffb33ebc8ca294'

class DrawingVariant2(Sub32):
    icon_id = 'pin-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    categories = ('interface-essential', 'state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Symmetric pin with true circular hole and tangent shoulders. Construction reference: map-pin."""
        self.add_arc('crown', (4, 14), (28, 14), radius_x=12)
        self.add_bezier('right', (28, 14), ((28, 20), (21, 26), (16, 30)))
        self.add_bezier('left', (16, 30), ((11, 26), (4, 20), (4, 14)))
        self.add_contour('pin', 'crown', 'right', 'left', closed=True)
        circle(self, 'hole', 16, 14, 4)

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
