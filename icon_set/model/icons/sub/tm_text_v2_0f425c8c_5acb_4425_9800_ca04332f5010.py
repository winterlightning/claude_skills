"""Circle enclosing uppercase T and M using the shared typeface. Complete-source repair; previous variant preserved."""
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Circle enclosing uppercase T and M using the shared typeface. Complete-source repair; previous variant preserved.'
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'TM Text: The uppercase letters TM sit side by side, with a broad crossbar on the T and two softly rounded peaks on the M. Generate this component alone; exclude Circle Frame.\n\nConstruction: A short T is followed by the source sloping-stem M; the horizontal profile keeps both letters readable with open spacing.\nKeyshape: HRECT_S; authored to the SUB32 envelope.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '0f425c8c-5acb-4425-9800-ca04332f5010'
SOURCE_PATH = 'pictographic-primitives/state/circle tm_0f425c8c-5acb-4425-9800-ca04332f5010.svg'
AUTHOR = 'gpt-6'

class TmTextVariant2(SourceFaithfulSideSub):
    icon_id = 'tm-text-v2'
    variant_of = 'tm-text'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('tm', 'text', 'uppercase', 'letters', 'sit', 'side', 'broad', 'crossbar')
    keyshape = Keyshape.SQUARE
    canvas_width = 64
    canvas_height = 64

    def build(self):
        """Circle enclosing uppercase T and M using the shared typeface."""
        circle(self, 'frame', 32, 32, 30)
        self.add_line('t-p1-r1-1', (13, 23), (27, 23))
        self.add_contour('t-path-1-1', 't-p1-r1-1', closed=False)
        self.add_line('t-p2-r1-1', (20, 23), (20, 41))
        self.add_contour('t-path-2-1', 't-p2-r1-1', closed=False)
        self.relate('connect', 't-path-2-1', 't-path-1-1')
        from icon_set.typeface.source_composition_forms import draw_sloping_m
        draw_sloping_m(self)

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
TYPEFACE_PROFILE_VARIANTS = ('letter-m-source-sloping',)
TYPEFACE_GLYPH_IDS = ('letter-t-uppercase', 'letter-m-uppercase')
