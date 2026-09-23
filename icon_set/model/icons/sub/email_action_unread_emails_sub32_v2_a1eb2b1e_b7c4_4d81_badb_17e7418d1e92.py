"""Independent 32px profile of email-action-unread-emails.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'a1eb2b1e-b7c4-4d81-badb-17e7418d1e92'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/emails/email action unread_a1eb2b1e-b7c4-4d81-badb-17e7418d1e92.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a1eb2b1e-b7c4-4d81-badb-17e7418d1e92', 'pictographic-primitives/emails/email action unread_a1eb2b1e-b7c4-4d81-badb-17e7418d1e92.svg'),)
PROFILE_SOURCE_KEYS = ('solo/email-action-unread-emails',)
SOLO_SOURCE_ICON_IDS = ('email-action-unread-emails',)
REFERENCE_EXPORT_SHA256 = '5cd1e40be8bc1724f6a68a79e27429301168c7fac24d21e03a8299609b3114a0'

class DrawingVariant2(Sub32):
    icon_id = 'email-action-unread-emails-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'emails'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Original single envelope; remove invented rear stacked rectangle. Construction reference: mail."""
        self.add_polyline('upper', (2, 4), (30, 4), (30, 24))
        self.add_arc('br', (30, 24), (26, 28), radius_x=4)
        self.add_line('bottom', (26, 28), (6, 28))
        self.add_arc('bl', (6, 28), (2, 24), radius_x=4)
        self.add_line('left', (2, 24), (2, 4))
        self.add_contour('envelope', 'br', 'bottom', 'bl', 'left')
        self.relate('connect', 'upper', 'envelope')
        self.add_polyline('flap', (2, 4), (16, 18), (30, 4))
        self.relate('connect', 'flap', 'envelope')
        self.relate('connect', 'flap', 'upper')

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
