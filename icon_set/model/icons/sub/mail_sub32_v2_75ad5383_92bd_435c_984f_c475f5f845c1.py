"""Independent 32px profile of mail.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '75ad5383-92bd-435c-984f-c475f5f845c1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/mail_75ad5383-92bd-435c-984f-c475f5f845c1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('75ad5383-92bd-435c-984f-c475f5f845c1', 'pictographic-primitives/symbol/mail_75ad5383-92bd-435c-984f-c475f5f845c1.svg'), ('19aca772-9076-4cc0-8470-0cdffef95def', 'pictographic-primitives/symbol/e mail_19aca772-9076-4cc0-8470-0cdffef95def.svg'), ('a6d5c36b-5f72-4bbf-a205-b2d56aaf29a5', 'pictographic-primitives/symbol/mail_a6d5c36b-5f72-4bbf-a205-b2d56aaf29a5.svg'), ('2a98051e-e248-4ae8-8a84-a56070dcb2ad', 'pictographic-primitives/symbol/page mail_2a98051e-e248-4ae8-8a84-a56070dcb2ad.svg'))
PROFILE_SOURCE_KEYS = ('solo/mail', 'solo/e-mail', 'solo/mail-symbol', 'solo/page-mail')
SOLO_SOURCE_ICON_IDS = ('mail', 'e-mail', 'mail-symbol', 'page-mail')
REFERENCE_EXPORT_SHA256 = '9e2c67811a8f83e9c1036555c0f9612b42e7aa6d06c6eab13201a553c08ff94d'

class DrawingVariant2(Sub32):
    icon_id = 'mail-sub32-v2'
    variant_of = 'mail-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Rounded envelope with one V flap; remove lower diagonals absent from original. Construction reference: mail."""
        box(self, 'envelope', 2, 4, 30, 28, 3)
        self.add_polyline('flap', (2, 8), (16, 17), (30, 8))
        self.relate('connect', 'envelope', 'flap')

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
