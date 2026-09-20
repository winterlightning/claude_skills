from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Letter B: An uppercase B has a straight upright stem and two rounded bowls, with the lower bowl slightly fuller. Generate this component alone; exclude Circle Frame.\n\nConstruction: Two equal elliptical bowls share the middle crossbar and left upright.\nKeyshape: VRECT_L; the four extrema follow the SUB32 contract.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'bc52ca8a-3c94-4ea2-a571-d56f66bbeff1'
SOURCE_PATH = 'pictographic-primitives/state/b text in circle_bc52ca8a-3c94-4ea2-a571-d56f66bbeff1.svg'
AUTHOR = 'gpt-6'

class LetterBSubVariant2(SourceFaithfulSideSub):
    icon_id = 'letter-b-sub-v2'
    variant_of = 'letter-b-sub'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('letter', 'b', 'uppercase', 'straight', 'upright', 'stem', 'rounded', 'bowls')
    keyshape = Keyshape.SQUARE
    canvas_width = 64
    canvas_height = 64

    def build(self):
        """Complete source circle and uppercase B, retaining the shared typeface."""
        circle(self, 'frame', 32, 32, 30)
        self.add_line('glyph-p1-r1-1', (23, 46), (23, 18))
        self.add_line('glyph-p1-r1-2', (23, 18), (32, 18))
        self.add_bezier('glyph-p1-r1-3', (32, 18), ((43.66666666666666, 18.000000000000004), (43.66666666666666, 31.999999999999996), (32, 32)))
        self.add_line('glyph-p1-r1-4', (32, 32), (23, 32))
        self.add_contour('glyph-path-1-1', 'glyph-p1-r1-1', 'glyph-p1-r1-2', 'glyph-p1-r1-3', 'glyph-p1-r1-4', closed=False)
        self.add_bezier('glyph-p2-r1-1', (32, 32), ((44.44444444444444, 31.999999999999996), (44.44444444444444, 45.999999999999986), (32, 46)))
        self.add_line('glyph-p2-r1-2', (32, 46), (23, 46))
        self.add_contour('glyph-path-2-1', 'glyph-p2-r1-1', 'glyph-p2-r1-2', closed=False)
        self.relate('connect', 'glyph-p1-r1-1', 'glyph-p2-r1-2')
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
TYPEFACE_GLYPH_IDS = ('letter-b-uppercase',)
