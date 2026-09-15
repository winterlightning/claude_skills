"""Opposed quarter-round vise jaws on a base with a right crank; channel reduced to the support."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b18a28ee-ccb5-411b-9471-e98234065972'
SOURCE_PATH = 'pictographic-primitives/tools/clamp press_b18a28ee-ccb5-411b-9471-e98234065972.svg'
AUTHOR = 'gpt-6'

class BenchVise(Solo48):
    icon_id = 'bench-vise'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/tools'
    aliases = ()
    keywords = ('vise', 'bench vise', 'clamp', 'press', 'jaws', 'workshop', 'hold', 'tool')

    def build(self) -> None:
        """Centerline review: preserve the silhouette; remove duplicated ink and split real attachments into shared nodes."""
        for n, left in [('left', True), ('right', False)]:
            x = 16 if left else 26
            outer = 4 if left else 38
            self.add_line(n + '-edges-1', (x, 8), (x, 22))
            self.add_line(n + '-edges-2', (x, 22), (outer, 22))
            self.add_arc(n + '-curve', (outer, 22), (x, 8), radius_x=12, radius_y=14, sweep=left)
            self.add_contour(n + '-jaw', n + '-edges-1', n + '-edges-2', n + '-curve', closed=True)
        self.add_line('support-left', (10, 22), (10, 40))
        self.add_polyline('support', (32, 40), (32, 31), (32, 22))
        self.relate('connect', 'support-left', 'left-jaw')
        self.relate('connect', 'support-left', 'base')
        self.relate('connect', 'support', 'right-jaw')
        self.add_polyline('base', (6, 40), (10, 40), (32, 40), (38, 40))
        self.relate('connect', 'support', 'base')
        self.add_line('crank-link', (32, 31), (44, 31))
        self.add_line('crank', (44, 22), (44, 40))
        self.relate('connect', 'crank-link', 'support')
        self.relate('connect', 'crank-link', 'crank')
