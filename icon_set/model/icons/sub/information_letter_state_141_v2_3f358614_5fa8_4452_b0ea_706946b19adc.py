from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Information Letter: A lowercase i has a tiny detached dot above a vertical stem with a leftward upper serif and a broad lower foot. Generate this component alone; exclude Circle Frame.\n\nConstruction: The dot, leftward upper serif, upright and bottom foot retain the source lowercase i.\nKeyshape: VRECT_S; final SUB32 envelope.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '3f358614-5fa8-4452-b0ea-706946b19adc'
SOURCE_PATH = 'pictographic-primitives/state/information_3f358614-5fa8-4452-b0ea-706946b19adc.svg'
AUTHOR = 'gpt-6'

class InformationLetterState141Variant2(SourceFaithfulSideSub):
    icon_id = 'information-letter-state-141-v2'
    variant_of = 'information-letter-state-141'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('information', 'letter', 'lowercase', 'i', 'tiny', 'detached', 'dot', 'vertical')
    keyshape = Keyshape.SQUARE
    canvas_width = 64
    canvas_height = 64

    def build(self):
        """Original circled information symbol: detached dot, upper left serif, stem and lower foot."""
        circle(self, 'frame', 32, 32, 30)
        from icon_set.typeface.framed_source_forms import draw_information_serif
        draw_information_serif(self)
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
TYPEFACE_GLYPH_IDS = ('letter-i',)

TYPEFACE_PROFILE_VARIANTS = ('letter-i-source-serif',)
