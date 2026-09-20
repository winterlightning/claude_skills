"""Independent 32px profile of bitcoin-speech-bubble-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._tall_base import SideSub32Exception
SOURCE_ICON_ID = '1b6ce2a0-ce30-49ce-99cf-a772bb04245d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/messages bubble round bitcoin_1b6ce2a0-ce30-49ce-99cf-a772bb04245d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1b6ce2a0-ce30-49ce-99cf-a772bb04245d', 'pictographic-primitives/symbol/messages bubble round bitcoin_1b6ce2a0-ce30-49ce-99cf-a772bb04245d.svg'), ('692b5811-84ae-4db0-8d66-219feaafec3e', 'pictographic-primitives/symbol/messages bubble square bitcoin_692b5811-84ae-4db0-8d66-219feaafec3e.svg'))
PROFILE_SOURCE_KEYS = ('solo/bitcoin-speech-bubble-solo', 'solo/bitcoin-message-speech-bubble-solo')
SOLO_SOURCE_ICON_IDS = ('bitcoin-speech-bubble-solo', 'bitcoin-message-speech-bubble-solo')
REFERENCE_EXPORT_SHA256 = 'b73c31329ae01f27540a1ce72ce15f754c4ac94d8a3a365ecbe392c12cd61ff2'

class DrawingVariant4(SideSub32Exception):
    icon_id = 'bitcoin-speech-bubble-solo-profile32-v4'
    variant_of = 'bitcoin-speech-bubble-solo-profile32-v3'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/finance'
    profile_source_keys = PROFILE_SOURCE_KEYS
    canvas_width = 32
    canvas_height = 44
    canvas_width = 32
    canvas_height = 44
    canvas_width = 32
    canvas_height = 44
    canvas_width = 32
    canvas_height = 44
    canvas_width = 32
    canvas_height = 48
    canvas_width = 32
    canvas_height = 48
    canvas_width = 32
    canvas_height = 48
    canvas_width = 32
    canvas_height = 48

    def build(self):
        """Restored oval Bitcoin speech bubble, lower-left tail, B bowls and both pairs of currency ticks. Construction reference: Original source composition; clean contour construction."""
        self.add_bezier('oval-tl', (16, 2), ((8, 2), (2, 10), (2, 20)))
        self.add_bezier('oval-bl', (2, 20), ((2, 28), (4, 34), (6, 38)))
        self.add_line('tail-a', (6, 38), (4, 46))
        self.add_line('tail-b', (4, 46), (12, 43))
        self.add_bezier('oval-br', (12, 43), ((24, 46), (30, 34), (30, 20)))
        self.add_bezier('oval-tr', (30, 20), ((30, 10), (24, 2), (16, 2)))
        self.add_contour('bubble', 'oval-tl', 'oval-bl', 'tail-a', 'tail-b', 'oval-br', 'oval-tr')
        from icon_set.typeface.sub32 import draw_bitcoin
        draw_bitcoin(self)

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
TYPEFACE_GLYPH_IDS = ('symbol-bitcoin',)

TYPEFACE_PROFILE_VARIANTS = ('symbol-bitcoin-compact32',)
