"""Broken heart outline behind the original descending diagonal slash. Complete-source repair; previous variant preserved."""
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Broken heart outline behind the original descending diagonal slash. Complete-source repair; previous variant preserved.'
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Diagonal Slash: A long diagonal line descends from upper left to lower right. Generate this component alone; exclude Heart.\n\nConstruction: The source falling diagonal slash is isolated from the heart; direction is preserved.\nKeyshape: SQUARE; the four extrema follow the SUB32 contract.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '00d83c6d-7ad8-492b-9d49-4bc79c61758b'
SOURCE_PATH = 'pictographic-primitives/state/slash heart_00d83c6d-7ad8-492b-9d49-4bc79c61758b.svg'
AUTHOR = 'gpt-6'

class DiagonalSlashState255Variant2(SourceFaithfulSideSub):
    icon_id = 'diagonal-slash-state-255-v2'
    variant_of = 'diagonal-slash-state-255'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('diagonal', 'slash', 'long', 'line', 'descends', 'upper', 'left', 'lower')
    keyshape = Keyshape.SQUARE
    canvas_width = 32
    canvas_height = 32

    def build(self):
        """Broken heart outline behind the original descending diagonal slash."""
        self.add_polyline('slash', (2, 2), (5, 5), (23, 23), (30, 30))
        self.add_bezier('heart-top', (5, 5), ((9, -1), (13, 5), (16, 9)))
        self.add_bezier('heart-right', (16, 9), ((26, -3), (37, 12), (23, 23)))
        self.add_contour('heart-upper', 'heart-top', 'heart-right')
        self.add_bezier('heart-left', (3, 13), ((3, 17), (9, 24), (16, 29)))
        self.add_line('end', (16, 29), (17, 28))
        self.add_contour('heart-lower', 'heart-left', 'end')
        self.relate('connect', 'heart-upper', 'slash')

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
