"""Speech bubble and tail enclosing the shared two-bar bitcoin glyph. Complete-source repair; previous variant preserved."""
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Speech bubble and tail enclosing the shared two-bar bitcoin glyph. Complete-source repair; previous variant preserved.'
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Bitcoin Sign: An uppercase B has two rounded bowls and two short parallel stems projecting above and below its horizontal ends. Generate this component alone; exclude Round Speech Bubble.\n\nConstruction: The B-shaped currency glyph retains both pairs of short projecting stems.\nKeyshape: VRECT_XL; final SUB32 envelope.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'eba39542-9146-4913-b251-ee6a2d0da885'
SOURCE_PATH = 'pictographic-primitives/state/messages bubble circle bitcoin_eba39542-9146-4913-b251-ee6a2d0da885.svg'
AUTHOR = 'gpt-6'

class BitcoinSignState169Variant2(SourceFaithfulSideSub):
    icon_id = 'bitcoin-sign-state-169-v2'
    variant_of = 'bitcoin-sign-state-169'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('bitcoin', 'sign', 'uppercase', 'b', 'rounded', 'bowls', 'short', 'parallel')
    keyshape = Keyshape.SQUARE
    canvas_width = 64
    canvas_height = 64

    def build(self):
        """Speech bubble and tail enclosing the shared two-bar bitcoin glyph."""
        self.add_bezier('ul', (32, 2), ((14, 2), (2, 13), (2, 29)))
        self.add_bezier('ll', (2, 29), ((2, 37), (7, 47), (16, 51)))
        self.add_line('tail-1', (16, 51), (4, 62))
        self.add_line('tail-2', (4, 62), (21, 54))
        self.add_bezier('base', (21, 54), ((27, 56), (30, 56), (32, 56)))
        self.add_bezier('lr', (32, 56), ((50, 56), (62, 41), (62, 29)))
        self.add_bezier('ur', (62, 29), ((62, 13), (50, 2), (32, 2)))
        self.add_contour('frame', 'ul', 'll', 'tail-1', 'tail-2', 'base', 'lr', 'ur', closed=True)
        self.add_line('glyph-p1-r1-1', (22, 38), (22, 20))
        self.add_line('glyph-p1-r1-2', (22, 20), (33, 20))
        self.add_bezier('glyph-p1-r1-3', (33, 20), ((44.647727272727266, 20.09090909090909), (44.647727272727266, 29), (33, 29)))
        self.add_line('glyph-p1-r1-4', (33, 29), (22, 29))
        self.add_contour('glyph-path-1-1', 'glyph-p1-r1-1', 'glyph-p1-r1-2', 'glyph-p1-r1-3', 'glyph-p1-r1-4', closed=False)
        self.add_bezier('glyph-p2-r1-1', (33, 29), ((45.28409090909091, 29), (45.28409090909091, 37.90909090909091), (33, 38)))
        self.add_line('glyph-p2-r1-2', (33, 38), (22, 38))
        self.add_contour('glyph-path-2-1', 'glyph-p2-r1-1', 'glyph-p2-r1-2', closed=False)
        self.add_line('glyph-p3-r1-1', (25, 15), (25, 20))
        self.add_contour('glyph-path-3-1', 'glyph-p3-r1-1', closed=False)
        self.add_line('glyph-p4-r1-1', (33, 15), (33, 20))
        self.add_contour('glyph-path-4-1', 'glyph-p4-r1-1', closed=False)
        self.add_line('glyph-p5-r1-1', (25, 38), (25, 43))
        self.add_contour('glyph-path-5-1', 'glyph-p5-r1-1', closed=False)
        self.add_line('glyph-p6-r1-1', (33, 38), (33, 43))
        self.add_contour('glyph-path-6-1', 'glyph-p6-r1-1', closed=False)
        self.relate('connect', 'glyph-p1-r1-1', 'glyph-p2-r1-2')
        self.relate('connect', 'glyph-p1-r1-2', 'glyph-p4-r1-1')
        self.relate('connect', 'glyph-p1-r1-3', 'glyph-p2-r1-1')
        self.relate('connect', 'glyph-p1-r1-3', 'glyph-p4-r1-1')
        self.relate('connect', 'glyph-p1-r1-4', 'glyph-p2-r1-1')
        self.relate('connect', 'glyph-p2-r1-1', 'glyph-p6-r1-1')
        self.relate('connect', 'glyph-p2-r1-2', 'glyph-p6-r1-1')
        self.relate('connect', 'glyph-path-2-1', 'glyph-path-1-1')
        self.relate('connect', 'glyph-path-3-1', 'glyph-path-1-1')
        self.relate('connect', 'glyph-path-4-1', 'glyph-path-1-1')
        self.relate('connect', 'glyph-path-5-1', 'glyph-path-2-1')
        self.relate('connect', 'glyph-path-6-1', 'glyph-path-2-1')
        from icon_set.typeface.source_composition_forms import draw_bitcoin_serifs
        draw_bitcoin_serifs(self)

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
TYPEFACE_PROFILE_VARIANTS = ('symbol-bitcoin-source-serifs',)
TYPEFACE_GLYPH_IDS = ('symbol-bitcoin',)
