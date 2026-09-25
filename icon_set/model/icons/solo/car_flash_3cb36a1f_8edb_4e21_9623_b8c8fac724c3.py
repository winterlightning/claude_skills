"""car flash: fresh SOLO48 repair.
Plan: Mirrored car outline and wheel arcs; wide lightning zigzag.
Keyshape: SQUARE. The taller front gives the lightning bolt clear space above the wheels.
Omissions: Minor roof and nose proportions rebalanced; no defining feature removed.
Construction reference: zap: a three-segment angular lightning gesture.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3cb36a1f-8edb-4e21-9623-b8c8fac724c3'
SOURCE_PATH = 'pictographic-primitives/other/car flash_3cb36a1f-8edb-4e21-9623-b8c8fac724c3.svg'
AUTHOR = 'gpt-6'
PARENT_SOURCE = 'icon_set/model/icons/solo/car_flash_3cb36a1f_8edb_4e21_9623_b8c8fac724c3.py'

class Drawing(Solo48):
    icon_id = 'car-flash'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('car', 'flash')

    def build(self):

        def circle(n, x, y, r):
            self.add_arc(n + '-a', (x - r, y), (x + r, y), radius_x=r)
            self.add_arc(n + '-b', (x + r, y), (x - r, y), radius_x=r)
            self.add_contour(n, n + '-a', n + '-b', closed=True)

        def rounded(n, l, t, r, b, k):
            self.add_line(n + '-t', (l + k, t), (r - k, t))
            self.add_arc(n + '-tr', (r - k, t), (r, t + k), radius_x=k)
            self.add_line(n + '-r', (r, t + k), (r, b - k))
            self.add_arc(n + '-br', (r, b - k), (r - k, b), radius_x=k)
            self.add_line(n + '-b', (r - k, b), (l + k, b))
            self.add_arc(n + '-bl', (l + k, b), (l, b - k), radius_x=k)
            self.add_line(n + '-l', (l, b - k), (l, t + k))
            self.add_arc(n + '-tl', (l, t + k), (l + k, t), radius_x=k)
            self.add_contour(n, *[n + '-' + s for s in ['t', 'tr', 'r', 'br', 'b', 'bl', 'l', 'tl']], closed=True)
        self.add_polyline('roof', (10, 14), (12, 14), (14, 6), (34, 6), (36, 14), (38, 14))
        self.add_arc('nose-right', (38, 14), (42, 18), radius_x=4)
        self.add_line('side-right', (42, 18), (42, 36))
        self.add_line('bumper-right', (42, 36), (40, 36))
        self.add_arc('wheel-right', (40, 36), (28, 36), radius_x=6)
        self.add_line('base', (28, 36), (20, 36))
        self.add_arc('wheel-left', (20, 36), (8, 36), radius_x=6)
        self.add_line('bumper-left', (8, 36), (6, 36))
        self.add_line('side-left', (6, 36), (6, 18))
        self.add_arc('nose-left', (6, 18), (10, 14), radius_x=4)
        self.add_contour('body', 'nose-right', 'side-right', 'bumper-right', 'wheel-right', 'base', 'wheel-left', 'bumper-left', 'side-left', 'nose-left')
        self.relate('connect', 'roof', 'body')
        self.add_polyline('flash', (23, 15), (17, 22), (31, 22), (25, 27))

# Explicit user approval for this exact SVG; changes invalidate the exception.
Drawing.exception = {'reason': 'User explicitly approved the repaired main icons as exceptions, retaining their current artwork and original validation findings.', 'approved_by': 'user', 'approved_on': '2026-09-25', 'svg_sha256': '635dde496beb876e802002e8f1bdfa9a4e50cfd239b971be8ca3445732e0b3f1', 'approval_scope': '47 repaired side-main sources identified in this task', 'source_uuid': '3cb36a1f-8edb-4e21-9623-b8c8fac724c3'}
