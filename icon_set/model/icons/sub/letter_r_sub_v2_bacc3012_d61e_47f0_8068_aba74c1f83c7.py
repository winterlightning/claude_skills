from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Letter R: An uppercase R combines a straight upright stem, rounded upper bowl, and diagonal leg descending to the right. Generate this component alone; exclude Circle Frame.\n\nConstruction: An upright, upper elliptical bowl and diagonal leg share attachment nodes.\nKeyshape: VRECT_L; the four extrema follow the SUB32 contract.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'bacc3012-d61e-47f0-8068-aba74c1f83c7'
SOURCE_PATH = 'pictographic-primitives/state/circle R_bacc3012-d61e-47f0-8068-aba74c1f83c7.svg'
AUTHOR = 'gpt-6'

class LetterRSubVariant2(SourceFaithfulSideSub):
    icon_id = 'letter-r-sub-v2'
    variant_of = 'letter-r-sub'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('letter', 'r', 'uppercase', 'combines', 'straight', 'upright', 'stem', 'rounded')
    keyshape = Keyshape.SQUARE
    canvas_width = 64
    canvas_height = 64

    def build(self):
        """Complete source circle and uppercase R, retaining the shared typeface."""
        circle(self, 'frame', 32, 32, 30)
        self.add_line('glyph-p1-r1-1', (22, 46), (22, 18))
        self.add_line('glyph-p1-r1-2', (22, 18), (32, 18))
        self.add_bezier('glyph-p1-r1-3', (32, 18), ((44.44444444444444, 18), (44.44444444444444, 32.77777777777778), (32, 33)))
        self.add_line('glyph-p1-r1-4', (32, 33), (22, 33))
        self.add_contour('glyph-path-1-1', 'glyph-p1-r1-1', 'glyph-p1-r1-2', 'glyph-p1-r1-3', 'glyph-p1-r1-4', closed=False)
        self.add_line('glyph-p2-r1-1', (32, 33), (42, 46))
        self.add_contour('glyph-path-2-1', 'glyph-p2-r1-1', closed=False)
        self.relate('connect', 'glyph-p1-r1-3', 'glyph-p2-r1-1')
        self.relate('connect', 'glyph-p1-r1-4', 'glyph-p2-r1-1')
        self.relate('connect', 'glyph-path-2-1', 'glyph-path-1-1')
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
TYPEFACE_GLYPH_IDS = ('letter-r-uppercase',)
