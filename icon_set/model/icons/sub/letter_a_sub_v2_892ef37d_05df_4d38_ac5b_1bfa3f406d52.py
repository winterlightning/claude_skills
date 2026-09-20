from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Letter A: An uppercase A has two sloping sides meeting at a softly rounded apex and a horizontal crossbar. Generate this component alone; exclude Circle Frame.\n\nConstruction: Two mirrored sloping stems and a crossbar sharing exact points on the stems.\nKeyshape: SQUARE; the four extrema follow the SUB32 contract.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '892ef37d-05df-4d38-ac5b-1bfa3f406d52'
SOURCE_PATH = 'pictographic-primitives/state/a text in circle_892ef37d-05df-4d38-ac5b-1bfa3f406d52.svg'
AUTHOR = 'gpt-6'

class LetterASubVariant2(SourceFaithfulSideSub):
    icon_id = 'letter-a-sub-v2'
    variant_of = 'letter-a-sub'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('letter', 'uppercase', 'sloping', 'sides', 'meeting', 'softly', 'rounded', 'apex')
    keyshape = Keyshape.SQUARE
    canvas_width = 64
    canvas_height = 64

    def build(self):
        """Complete source circle and uppercase A, retaining the shared typeface."""
        circle(self, 'frame', 32, 32, 30)
        self.add_line('glyph-p1-r1-1', (22, 46), (31, 19))
        self.add_bezier('glyph-p1-r1-2', (31, 19), ((31.666666666666668, 17.58666666666667), (32.333333333333336, 17.58666666666667), (33, 19)))
        self.add_line('glyph-p1-r1-3', (33, 19), (42, 46))
        self.add_contour('glyph-path-1-1', 'glyph-p1-r1-1', 'glyph-p1-r1-2', 'glyph-p1-r1-3', closed=False)
        self.add_line('glyph-p2-r1-1', (26, 34), (38, 34))
        self.add_contour('glyph-path-2-1', 'glyph-p2-r1-1', closed=False)
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
TYPEFACE_GLYPH_IDS = ('letter-a-uppercase',)
