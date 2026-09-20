"""Circle enclosing a single-bar yuan sign, preserving the original one-bar form. Complete-source repair; previous variant preserved."""
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Circle enclosing a single-bar yuan sign, preserving the original one-bar form. Complete-source repair; previous variant preserved.'
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Yuan Sign: A Y-shaped currency glyph has two diagonal upper arms and a single horizontal bar crossing its lower stem. Generate this component alone; exclude Circle Frame.\n\nConstruction: The Y-shaped currency glyph retains exactly one crossbar, as in this source.\nKeyshape: VRECT_XL; final SUB32 envelope.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '7b4acd01-51fe-4645-a2d7-08e28c65ee64'
SOURCE_PATH = 'pictographic-primitives/state/circle yuan_7b4acd01-51fe-4645-a2d7-08e28c65ee64.svg'
AUTHOR = 'gpt-6'

class YuanSignState92Variant2(SourceFaithfulSideSub):
    icon_id = 'yuan-sign-state-92-v2'
    variant_of = 'yuan-sign-state-92'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('yuan', 'sign', 'y', 'shaped', 'currency', 'glyph', 'diagonal', 'upper')
    keyshape = Keyshape.SQUARE
    canvas_width = 32
    canvas_height = 32

    def build(self):
        """Circle enclosing a single-bar yuan sign, preserving the original one-bar form."""
        circle(self, 'frame', 16, 16, 14)
        self.add_line('glyph-p1-r1-1', (11, 10), (16, 16))
        self.add_line('glyph-p1-r1-2', (16, 16), (21, 10))
        self.add_contour('glyph-path-1-1', 'glyph-p1-r1-1', 'glyph-p1-r1-2', closed=False)
        self.add_line('glyph-p2-r1-1', (16, 16), (16, 22))
        self.add_contour('glyph-path-2-1', 'glyph-p2-r1-1', closed=False)
        self.add_line('glyph-p3-r1-1', (12, 19), (20, 19))
        self.add_contour('glyph-path-3-1', 'glyph-p3-r1-1', closed=False)
        self.relate('connect', 'glyph-p1-r1-1', 'glyph-p2-r1-1')
        self.relate('connect', 'glyph-p1-r1-2', 'glyph-p2-r1-1')
        self.relate('connect', 'glyph-path-2-1', 'glyph-path-1-1')
        self.relate('connect', 'glyph-path-3-1', 'glyph-path-2-1')

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
TYPEFACE_GLYPH_IDS = ('symbol-yuan-one-bar',)
