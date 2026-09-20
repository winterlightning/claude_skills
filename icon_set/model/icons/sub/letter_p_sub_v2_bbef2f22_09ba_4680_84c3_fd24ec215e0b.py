from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Letter P: An uppercase P has a straight upright stem with one rounded bowl attached to its upper half. Generate this component alone; exclude Circle Frame.\n\nConstruction: An upright joins a half-elliptical upper bowl at its top and midpoint.\nKeyshape: VRECT_L; the four extrema follow the SUB32 contract.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'bbef2f22-09ba-4680-84c3-fd24ec215e0b'
SOURCE_PATH = 'pictographic-primitives/state/circle p_bbef2f22-09ba-4680-84c3-fd24ec215e0b.svg'
AUTHOR = 'gpt-6'

class LetterPSubVariant2(SourceFaithfulSideSub):
    icon_id = 'letter-p-sub-v2'
    variant_of = 'letter-p-sub'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('letter', 'p', 'uppercase', 'straight', 'upright', 'stem', 'rounded', 'bowl')
    keyshape = Keyshape.SQUARE
    canvas_width = 64
    canvas_height = 64

    def build(self):
        """Complete source circle and uppercase P, retaining the shared typeface."""
        circle(self, 'frame', 32, 32, 30)
        self.add_line('glyph-p1-r1-1', (22, 46), (22, 18))
        self.add_line('glyph-p1-r1-2', (22, 18), (32, 18))
        self.add_bezier('glyph-p1-r1-3', (32, 18), ((44.83333333333333, 18), (44.83333333333333, 32.77777777777778), (32, 33)))
        self.add_line('glyph-p1-r1-4', (32, 33), (22, 33))
        self.add_contour('glyph-path-1-1', 'glyph-p1-r1-1', 'glyph-p1-r1-2', 'glyph-p1-r1-3', 'glyph-p1-r1-4', closed=False)
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub

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
TYPEFACE_GLYPH_IDS = ('letter-p-uppercase',)
