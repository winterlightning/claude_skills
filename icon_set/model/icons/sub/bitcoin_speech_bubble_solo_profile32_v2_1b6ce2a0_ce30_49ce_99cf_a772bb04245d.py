"""Independent 32px profile of bitcoin-speech-bubble-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '1b6ce2a0-ce30-49ce-99cf-a772bb04245d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/messages bubble round bitcoin_1b6ce2a0-ce30-49ce-99cf-a772bb04245d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1b6ce2a0-ce30-49ce-99cf-a772bb04245d', 'pictographic-primitives/symbol/messages bubble round bitcoin_1b6ce2a0-ce30-49ce-99cf-a772bb04245d.svg'), ('692b5811-84ae-4db0-8d66-219feaafec3e', 'pictographic-primitives/symbol/messages bubble square bitcoin_692b5811-84ae-4db0-8d66-219feaafec3e.svg'))
PROFILE_SOURCE_KEYS = ('solo/bitcoin-speech-bubble-solo', 'solo/bitcoin-message-speech-bubble-solo')
SOLO_SOURCE_ICON_IDS = ('bitcoin-speech-bubble-solo', 'bitcoin-message-speech-bubble-solo')
REFERENCE_EXPORT_SHA256 = 'b73c31329ae01f27540a1ce72ce15f754c4ac94d8a3a365ecbe392c12cd61ff2'

class DrawingVariant2(Sub32):
    icon_id = 'bitcoin-speech-bubble-solo-profile32-v2'
    variant_of = 'bitcoin-speech-bubble-solo-profile32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/finance'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Currency speech bubble retaining the shared Bitcoin sign and tail. Construction reference: shared typeface / geometric source construction."""
        self.add_polyline('bubble', (2, 2), (30, 2), (30, 24), (14, 24), (6, 30), (6, 24), (2, 24), (2, 2))
        self.add_line('char7-p1-r1-1', (11, 21), (11, 11))
        self.add_line('char7-p1-r1-2', (11, 11), (17, 11))
        self.add_bezier('char7-p1-r1-3', (17, 11), ((20, 11), (21, 12), (21, 14)))
        self.add_bezier('char7-p1-r1-4', (21, 14), ((21, 15), (20, 16), (17, 16)))
        self.add_line('char7-p1-r1-5', (17, 16), (11, 16))
        self.add_contour('char7-path-1-1', 'char7-p1-r1-1', 'char7-p1-r1-2', 'char7-p1-r1-3', 'char7-p1-r1-4', 'char7-p1-r1-5', closed=False)
        self.add_bezier('char7-p2-r1-1', (17, 16), ((20, 16), (21, 17), (21, 18)))
        self.add_bezier('char7-p2-r1-2', (21, 18), ((21, 20), (20, 21), (17, 21)))
        self.add_line('char7-p2-r1-3', (17, 21), (11, 21))
        self.add_contour('char7-path-2-1', 'char7-p2-r1-1', 'char7-p2-r1-2', 'char7-p2-r1-3', closed=False)
        self.add_line('char7-p3-r1-1', (12, 8), (12, 11))
        self.add_contour('char7-path-3-1', 'char7-p3-r1-1', closed=False)
        self.add_line('char7-p4-r1-1', (17, 8), (17, 11))
        self.add_contour('char7-path-4-1', 'char7-p4-r1-1', closed=False)
        self.add_line('char7-p5-r1-1', (12, 21), (12, 24))
        self.add_contour('char7-path-5-1', 'char7-p5-r1-1', closed=False)
        self.add_line('char7-p6-r1-1', (17, 21), (17, 24))
        self.add_contour('char7-path-6-1', 'char7-p6-r1-1', closed=False)
        self.relate('connect', 'char7-p1-r1-1', 'char7-p2-r1-3')
        self.relate('connect', 'char7-p1-r1-2', 'char7-p4-r1-1')
        self.relate('connect', 'char7-p1-r1-3', 'char7-p4-r1-1')
        self.relate('connect', 'char7-p1-r1-4', 'char7-p2-r1-1')
        self.relate('connect', 'char7-p1-r1-5', 'char7-p2-r1-1')
        self.relate('connect', 'char7-p2-r1-2', 'char7-p6-r1-1')
        self.relate('connect', 'char7-p2-r1-3', 'char7-p6-r1-1')
        self.relate('connect', 'char7-path-2-1', 'char7-path-1-1')
        self.relate('connect', 'char7-path-3-1', 'char7-path-1-1')
        self.relate('connect', 'char7-path-4-1', 'char7-path-1-1')
        self.relate('connect', 'char7-path-5-1', 'char7-path-2-1')
        self.relate('connect', 'char7-path-6-1', 'char7-path-2-1')

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
