"""Independent 32px profile of credit-card.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '66b95d3f-a723-4cfd-830c-ed99236a5244'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/payments/credit card_66b95d3f-a723-4cfd-830c-ed99236a5244.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('66b95d3f-a723-4cfd-830c-ed99236a5244', 'pictographic-primitives/payments/credit card_66b95d3f-a723-4cfd-830c-ed99236a5244.svg'),)
PROFILE_SOURCE_KEYS = ('solo/credit-card',)
SOLO_SOURCE_ICON_IDS = ('credit-card',)
REFERENCE_EXPORT_SHA256 = '1fd402939e860a5b0b45fbcafa0d8a50ee5cff773c7938114a2df17bdcfcb04e'

class DrawingVariant2(Sub32):
    icon_id = 'credit-card-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'payments'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Rounded payment card, horizontal strip division and single dot. Construction reference: credit-card."""
        box(self, 'card', 2, 4, 30, 28, 3)
        self.add_line('stripe', (2, 12), (30, 12))
        self.relate('connect', 'stripe', 'card')
        self.add_dot('mark', (23, 20))

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
