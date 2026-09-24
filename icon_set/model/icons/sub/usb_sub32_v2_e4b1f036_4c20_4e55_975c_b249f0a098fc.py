"""Independent 32px profile of usb.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'e4b1f036-4c20-4e55-975c-b249f0a098fc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/usb_e4b1f036-4c20-4e55-975c-b249f0a098fc.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e4b1f036-4c20-4e55-975c-b249f0a098fc', 'pictographic-primitives/state/usb_e4b1f036-4c20-4e55-975c-b249f0a098fc.svg'),)
PROFILE_SOURCE_KEYS = ('solo/usb',)
SOLO_SOURCE_ICON_IDS = ('usb',)
REFERENCE_EXPORT_SHA256 = '8569afa12f1a5809791eafab748edcae54ae265cef077bc2423d71be566d38fa'

class DrawingVariant2(Sub32):
    icon_id = 'usb-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """USB plug with rectangular connector above a rounded lower housing. Construction reference: usb (construction differs from local trident reference)."""
        box(self, 'housing', 4, 12, 28, 30, 5)
        self.add_polyline('connector', (10, 12), (10, 2), (22, 2), (22, 12))
        self.relate('connect', 'connector', 'housing')

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
