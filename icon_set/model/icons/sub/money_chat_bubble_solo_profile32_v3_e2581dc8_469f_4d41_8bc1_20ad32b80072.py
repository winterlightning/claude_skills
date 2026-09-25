"""Independent 32px profile of money-chat-bubble-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'e2581dc8-469f-4d41-8bc1-20ad32b80072'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/messages bubble square dollar sign_e2581dc8-469f-4d41-8bc1-20ad32b80072.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e2581dc8-469f-4d41-8bc1-20ad32b80072', 'pictographic-primitives/symbol/messages bubble square dollar sign_e2581dc8-469f-4d41-8bc1-20ad32b80072.svg'), ('a0e713ab-5594-48b4-9fb9-5bd0a13657f4', 'pictographic-primitives/other/messages bubble round dollar sign_a0e713ab-5594-48b4-9fb9-5bd0a13657f4.svg'), ('93c99818-8211-47c5-bf92-9fa83e3cab72', 'pictographic-primitives/other/message dollar sign lines_93c99818-8211-47c5-bf92-9fa83e3cab72.svg'))
PROFILE_SOURCE_KEYS = ('solo/money-chat-bubble-solo', 'solo/dollar-sign-chat-bubble-solo', 'solo/money-message-bubble-solo')
SOLO_SOURCE_ICON_IDS = ('money-chat-bubble-solo', 'dollar-sign-chat-bubble-solo', 'money-message-bubble-solo')
REFERENCE_EXPORT_SHA256 = 'a0eb804bb7dcb76a17857cbff085f2d0c34ad5451f33cc871fe310fcb1e19a5e'

class DrawingVariant3(Sub32):
    icon_id = 'money-chat-bubble-solo-profile32-v3'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Money chat bubble retaining its tail and the approved light dollar mark. Construction reference: source composition; shared small-size character construction."""
        self.add_polyline('bubble', (2, 2), (30, 2), (30, 26), (16, 26), (8, 30), (8, 26), (2, 26), (2, 2))
        from icon_set.typeface.sub32 import draw_dollar
        draw_dollar(self, 10, 2)

def box(s, n, l, t, r, b, k=3):
    if k == 0:
        s.add_polyline(n, (l, t), (r, t), (r, b), (l, b), (l, t))
        return
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
TYPEFACE_GLYPH_IDS = ('symbol-dollar',)

TYPEFACE_PROFILE_VARIANTS = ('symbol-dollar-compact32',)
