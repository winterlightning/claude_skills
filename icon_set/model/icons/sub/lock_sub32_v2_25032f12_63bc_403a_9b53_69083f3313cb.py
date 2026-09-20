"""Independent 32px profile of lock.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '25032f12-63bc-403a-9b53-69083f3313cb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/lock_25032f12-63bc-403a-9b53-69083f3313cb.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('25032f12-63bc-403a-9b53-69083f3313cb', 'pictographic-primitives/interface-essential/lock_25032f12-63bc-403a-9b53-69083f3313cb.svg'), ('e43b261d-5d07-450c-ab97-9058803311d6', 'pictographic-primitives/interface-essential/lock_e43b261d-5d07-450c-ab97-9058803311d6.svg'), ('ee9cb073-d745-4a2a-a54b-ab36b6f8efb7', 'pictographic-primitives/interface-essential/lock_ee9cb073-d745-4a2a-a54b-ab36b6f8efb7.svg'), ('386cb547-821f-4d23-a0b8-bb7f43205473', 'pictographic-primitives/interface-essential/lock_386cb547-821f-4d23-a0b8-bb7f43205473.svg'))
PROFILE_SOURCE_KEYS = ('solo/lock', 'solo/lock-e43b261d', 'solo/lock-ee9cb073', 'solo/lock-interface-essential')
SOLO_SOURCE_ICON_IDS = ('lock', 'lock-e43b261d', 'lock-ee9cb073', 'lock-interface-essential')
REFERENCE_EXPORT_SHA256 = 'c3f139e1f35a4f1b1fb13df6b653dd944c83035799d224f6acd7916e6c9b27e7'

class DrawingVariant2(Sub32):
    icon_id = 'lock-sub32-v2'
    variant_of = 'lock-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Rounded body and circular shackle; no added keyhole. Construction reference: lock."""
        box(self, 'body', 4, 14, 28, 30, 3)
        self.add_line('shackle-left', (8, 14), (8, 10))
        self.add_arc('shackle-top', (8, 10), (24, 10), radius_x=8)
        self.add_line('shackle-right', (24, 10), (24, 14))
        self.add_contour('shackle', 'shackle-left', 'shackle-top', 'shackle-right')
        self.relate('connect', 'body', 'shackle')

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
