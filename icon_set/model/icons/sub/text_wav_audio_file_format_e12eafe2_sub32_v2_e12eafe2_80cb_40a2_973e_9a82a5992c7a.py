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

class DrawingVariant2(TextSub32):
    icon_id = 'text-wav-audio-file-format-e12eafe2-sub32-v2'
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
        """Shared typeface letter-w-uppercase, letter-a-uppercase, letter-v-uppercase at 32px ink height and natural width. Construction reference: shared typeface."""
        self.add_line('p1-r1-1', (2, 2), (8, 28))
        self.add_bezier('p1-r1-2', (8, 28), ((8.666666666666666, 30.666666666666668), (9.333333333333334, 30.666666666666668), (10, 28)))
        self.add_line('p1-r1-3', (10, 28), (16, 4))
        self.add_bezier('p1-r1-4', (16, 4), ((16.666666666666668, 2), (17.333333333333332, 2), (18, 4)))
        self.add_line('p1-r1-5', (18, 4), (24, 28))
        self.add_bezier('p1-r1-6', (24, 28), ((24.666666666666668, 30.666666666666668), (25.333333333333332, 30.666666666666668), (26, 28)))
        self.add_line('p1-r1-7', (26, 28), (32, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (41, 30), (50, 3))
        self.add_bezier('p2-r1-2', (50, 3), ((50.666666666666664, 1.6666666666666667), (51.333333333333336, 1.6666666666666667), (52, 3)))
        self.add_line('p2-r1-3', (52, 3), (61, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (45, 18), (57, 18))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (71, 2), (80, 28))
        self.add_bezier('p4-r1-2', (80, 28), ((80.66666666666667, 29.333333333333332), (81.33333333333333, 30), (82, 30)))
        self.add_bezier('p4-r1-3', (82, 30), ((82, 30), (82.33333333333333, 29.333333333333332), (83, 28)))
        self.add_line('p4-r1-4', (83, 28), (92, 2))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)

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
TYPEFACE_GLYPH_IDS = ('letter-w-uppercase', 'letter-a-uppercase', 'letter-v-uppercase')
