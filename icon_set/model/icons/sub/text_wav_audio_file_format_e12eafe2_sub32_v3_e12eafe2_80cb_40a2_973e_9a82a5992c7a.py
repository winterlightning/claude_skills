"""Independent 32px profile of text-wav-audio-file-format-e12eafe2.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = 'e12eafe2-80cb-40a2-973e-9a82a5992c7a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/wav (text)_e12eafe2-80cb-40a2-973e-9a82a5992c7a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e12eafe2-80cb-40a2-973e-9a82a5992c7a', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/wav (text)_e12eafe2-80cb-40a2-973e-9a82a5992c7a.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-wav-audio-file-format-e12eafe2',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '7be1a01e833f348505ed56546b20882a0a63278c6a96d2a1b44fe8d28039a297'

class DrawingVariant3(TextSub32):
    icon_id = 'text-wav-audio-file-format-e12eafe2-sub32-v3'
    variant_of = 'text-wav-audio-file-format-e12eafe2-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 95
    text_ink_bounds = (0, 0, 94, 32)

    def build(self):
        """Shared glyphs letter-w-uppercase, letter-a-uppercase, letter-v-uppercase at 32px ink height and natural width. Construction reference: shared typeface / geometric source construction."""
        self.add_line('g0-p1-r1-1', (2, 2), (9, 30))
        self.add_line('g0-p1-r1-2', (9, 30), (17, 3))
        self.add_line('g0-p1-r1-3', (17, 3), (25, 30))
        self.add_line('g0-p1-r1-4', (25, 30), (32, 2))
        self.add_contour('g0-path-1-1', 'g0-p1-r1-1', 'g0-p1-r1-2', 'g0-p1-r1-3', 'g0-p1-r1-4', closed=False)
        self.add_line('g1-p1-r1-1', (41, 30), (50, 3))
        self.add_bezier('g1-p1-r1-2', (50, 3), ((50.666666666666664, 2.3333333333333335), (51, 2), (51, 2)))
        self.add_bezier('g1-p1-r1-3', (51, 2), ((51.666666666666664, 2), (52.333333333333336, 2.3333333333333335), (53, 3)))
        self.add_line('g1-p1-r1-4', (53, 3), (62, 30))
        self.add_contour('g1-path-1-1', 'g1-p1-r1-1', 'g1-p1-r1-2', 'g1-p1-r1-3', 'g1-p1-r1-4', closed=False)
        self.add_line('g1-p2-r1-1', (45, 18), (58, 18))
        self.add_contour('g1-path-2-1', 'g1-p2-r1-1', closed=False)
        self.relate('connect', 'g1-path-2-1', 'g1-path-1-1')
        self.add_line('g2-p1-r1-1', (71, 2), (80, 28))
        self.add_bezier('g2-p1-r1-2', (80, 28), ((80.66666666666667, 29.333333333333332), (81.33333333333333, 30), (82, 30)))
        self.add_bezier('g2-p1-r1-3', (82, 30), ((82, 30), (82.33333333333333, 29.333333333333332), (83, 28)))
        self.add_line('g2-p1-r1-4', (83, 28), (92, 2))
        self.add_contour('g2-path-1-1', 'g2-p1-r1-1', 'g2-p1-r1-2', 'g2-p1-r1-3', 'g2-p1-r1-4', closed=False)

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
TYPEFACE_GLYPH_IDS = ('letter-w-uppercase', 'letter-a-uppercase', 'letter-v-uppercase')
