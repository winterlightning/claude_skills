"""Independent 32px profile of unlock.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '4aa8fd4e-dd20-4ab4-9374-89370bfa9188'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/unlock_4aa8fd4e-dd20-4ab4-9374-89370bfa9188.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4aa8fd4e-dd20-4ab4-9374-89370bfa9188', 'pictographic-primitives/state/unlock_4aa8fd4e-dd20-4ab4-9374-89370bfa9188.svg'), ('90a6ff07-21bc-47ed-b588-aacc1c25c397', 'pictographic-primitives/symbol/unlock_90a6ff07-21bc-47ed-b588-aacc1c25c397.svg'))
PROFILE_SOURCE_KEYS = ('solo/unlock', 'solo/unlock-90a6ff07')
SOLO_SOURCE_ICON_IDS = ('unlock', 'unlock-90a6ff07')
REFERENCE_EXPORT_SHA256 = '1aed9ece8daf9f853443f7683f46868886f3a263c274d74dfd3325a6c18aa711'

class DrawingVariant2(Sub32):
    icon_id = 'unlock-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Open padlock with rounded body and circular shackle open at the right. Construction reference: lock-open."""
        box(self, 'body', 4, 16, 28, 30, 3)
        self.add_line('shackle-l', (9, 16), (9, 9))
        self.add_arc('shackle-top', (9, 9), (23, 9), radius_x=7)
        self.add_contour('shackle', 'shackle-l', 'shackle-top')
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
