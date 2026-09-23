"""Independent 32px profile of mobile-phone-phones.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '0ccd2887-dbd0-4ab5-a736-e2ba5438da4d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/phones/mobile phone_0ccd2887-dbd0-4ab5-a736-e2ba5438da4d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0ccd2887-dbd0-4ab5-a736-e2ba5438da4d', 'pictographic-primitives/phones/mobile phone_0ccd2887-dbd0-4ab5-a736-e2ba5438da4d.svg'), ('70454eff-c88b-47e2-b376-ad91c78c22f0', 'pictographic-primitives/phones/mobile phone_70454eff-c88b-47e2-b376-ad91c78c22f0.svg'), ('c4f9e2f1-641c-4dbb-ae42-c4ce12aafedf', 'pictographic-primitives/phones/mobile phone_c4f9e2f1-641c-4dbb-ae42-c4ce12aafedf.svg'))
PROFILE_SOURCE_KEYS = ('solo/mobile-phone-phones', 'solo/mobile-phone-70454eff', 'solo/mobile-phone-c4f9e2f1')
SOLO_SOURCE_ICON_IDS = ('mobile-phone-phones', 'mobile-phone-70454eff', 'mobile-phone-c4f9e2f1')
REFERENCE_EXPORT_SHA256 = '04503e0736e507598f14c69f2520921f4375190d995f1c7e395b765219108e21'

class DrawingVariant2(Sub32):
    icon_id = 'mobile-phone-phones-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'phones'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Tall rounded phone, single lower horizontal division. Construction reference: smartphone."""
        box(self, 'phone', 6, 2, 26, 30, 4)
        self.add_line('division', (6, 22), (26, 22))
        self.relate('connect', 'phone', 'division')

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
