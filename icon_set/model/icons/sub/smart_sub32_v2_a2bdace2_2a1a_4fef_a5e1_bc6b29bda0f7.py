"""Independent 32px profile of smart.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'a2bdace2-2a1a-4fef-a5e1-bc6b29bda0f7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/smart_a2bdace2-2a1a-4fef-a5e1-bc6b29bda0f7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a2bdace2-2a1a-4fef-a5e1-bc6b29bda0f7', 'pictographic-primitives/state/smart_a2bdace2-2a1a-4fef-a5e1-bc6b29bda0f7.svg'),)
PROFILE_SOURCE_KEYS = ('solo/smart',)
SOLO_SOURCE_ICON_IDS = ('smart',)
REFERENCE_EXPORT_SHA256 = '09cd865c43d3540992d1184e677cbc210e361c060348f4c51a48a9340af15d7b'

class DrawingVariant2(Sub32):
    icon_id = 'smart-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Three nested open Wi-Fi arches without a dot. Construction reference: wifi."""
        for n, left, right, y, rx, ry in [('outer', 2, 30, 12, 14, 8), ('middle', 8, 24, 20, 8, 6), ('inner', 12, 20, 28, 4, 4)]:
            self.add_arc(n, (left, y), (right, y), radius_x=rx, radius_y=ry)

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
