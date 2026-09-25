"""Complete circle enclosing the shared pound glyph. Complete-source repair; previous variant preserved."""
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Complete circle enclosing the shared pound glyph. Complete-source repair; previous variant preserved.'
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Pound Sign: A pound sign has a curved upper hook, upright stem, middle crossbar, and a flat lower foot extending right. Generate this component alone; exclude Circle Frame.\n\nConstruction: A rounded upper hook flows tangentially into a vertical stem above a broad foot and crossing bar.\nKeyshape: VRECT_L; the four extrema follow the SUB32 contract.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'd00222dd-fe8c-4806-ad6b-9c8ece57b642'
SOURCE_PATH = 'pictographic-primitives/state/circle pound_d00222dd-fe8c-4806-ad6b-9c8ece57b642.svg'
AUTHOR = 'gpt-6'

class PoundSignSubVariant2(SourceFaithfulSideSub):
    icon_id = 'pound-sign-sub-v2'
    variant_of = 'pound-sign-sub'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('pound', 'sign', 'curved', 'upper', 'hook', 'upright', 'stem', 'middle')
    keyshape = Keyshape.SQUARE
    canvas_width = 48
    canvas_height = 48

    def build(self):
        """Complete circle enclosing the shared pound glyph."""
        circle(self, 'frame', 24, 24, 22)
        self.add_bezier('glyph-p1-r1-1', (32, 16), ((32.45999079351963, 10.62002761944111), (18.143083296794103, 9.969259096862677), (18, 18)))
        self.add_line('glyph-p1-r1-2', (18, 18), (18, 28))
        self.add_bezier('glyph-p1-r1-3', (18, 28), ((18.143083296794103, 32.746157387107836), (16.841546251637237, 36), (14, 36)))
        self.add_line('glyph-p1-r1-4', (14, 36), (34, 36))
        self.add_contour('glyph-path-1-1', 'glyph-p1-r1-1', 'glyph-p1-r1-2', 'glyph-p1-r1-3', 'glyph-p1-r1-4', closed=False)
        self.add_line('glyph-p2-r1-1', (14, 25), (27, 25))
        self.add_contour('glyph-path-2-1', 'glyph-p2-r1-1', closed=False)
        self.relate('connect', 'glyph-path-2-1', 'glyph-path-1-1')

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
TYPEFACE_GLYPH_IDS = ('symbol-pound',)
