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

class DrawingVariant2(Sub32):
    icon_id = 'money-chat-bubble-solo-profile32-v2'
    variant_of = 'money-chat-bubble-solo-profile32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/finance'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Money speech bubble with shared dollar sign. Construction reference: shared typeface and original frame."""
        self.add_polyline('bubble', (2, 2), (30, 2), (30, 24), (14, 24), (6, 30), (6, 24), (2, 24), (2, 2))
        self.add_bezier('char32-p1-r1-1', (20, 11), ((20, 10), (18, 10), (16, 10)))
        self.add_bezier('char32-p1-r1-2', (16, 10), ((14, 10), (12, 11), (12, 13)))
        self.add_bezier('char32-p1-r1-3', (12, 13), ((12, 13), (12, 13), (12, 13)))
        self.add_bezier('char32-p1-r1-4', (12, 13), ((12, 17), (20, 15), (20, 19)))
        self.add_bezier('char32-p1-r1-5', (20, 19), ((20, 19), (20, 19), (20, 19)))
        self.add_bezier('char32-p1-r1-6', (20, 19), ((20, 22), (18, 23), (16, 23)))
        self.add_bezier('char32-p1-r1-7', (16, 23), ((14, 23), (12, 22), (12, 21)))
        self.add_contour('char32-path-1-1', 'char32-p1-r1-1', 'char32-p1-r1-2', 'char32-p1-r1-3', 'char32-p1-r1-4', 'char32-p1-r1-5', 'char32-p1-r1-6', 'char32-p1-r1-7', closed=False)
        self.add_line('char32-p2-r1-1', (16, 8), (16, 24))
        self.add_contour('char32-path-2-1', 'char32-p2-r1-1', closed=False)
        self.relate('connect', 'char32-path-2-1', 'char32-path-1-1')

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
