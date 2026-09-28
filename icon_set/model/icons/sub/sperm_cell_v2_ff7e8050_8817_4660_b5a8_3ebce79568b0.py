"""Circle, diagonal prohibition segments, organic tilted sperm head and flowing tail. Complete-source repair; previous variant preserved."""
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Circle, diagonal prohibition segments, organic tilted sperm head and flowing tail. Complete-source repair; previous variant preserved.'
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Sperm Cell: An irregular oval head joins a long undulating tail that bends first right and then left before curling outward. Generate this component alone; exclude Prohibition Frame.\n\nConstruction: A rounded head joins two alternating curved tail segments and an outward terminal; the irregular source head is regularized to a circle for the integer-grid construction.\nKeyshape: VRECT_XL; authored to the SUB32 envelope.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'ff7e8050-8817-4660-b5a8-3ebce79568b0'
SOURCE_PATH = 'pictographic-primitives/state/slash sperm_ff7e8050-8817-4660-b5a8-3ebce79568b0.svg'
AUTHOR = 'gpt-6'

class SpermCellVariant2(SourceFaithfulSideSub):
    icon_id = 'sperm-cell-v2'
    variant_of = 'sperm-cell'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('sperm', 'cell', 'irregular', 'oval', 'head', 'joins', 'long', 'undulating')
    keyshape = Keyshape.SQUARE
    canvas_width = 48
    canvas_height = 48

    def build(self):
        """Circle, diagonal prohibition segments, organic tilted sperm head and flowing tail."""
        circle(self, 'frame', 24, 24, 22)
        self.add_line('slash-top', (34, 14), (40, 8))
        self.add_line('slash-bottom', (8, 40), (19, 29))
        self.relate('connect', 'frame', 'slash-top')
        self.relate('connect', 'frame', 'slash-bottom')
        self.add_bezier('head-a', (17, 11), ((12, 10), (15, 24), (20, 21)))
        self.add_bezier('head-b', (20, 21), ((28, 16), (24, 12), (17, 11)))
        self.add_contour('head', 'head-a', 'head-b', closed=True)
        self.add_bezier('tail-a', (22, 20), ((31, 25), (30, 29), (26, 32)))
        self.add_bezier('tail-b', (26, 32), ((22, 35), (25, 39), (30, 38)))
        self.add_contour('tail', 'tail-a', 'tail-b')
        self.relate('connect', 'head', 'tail')

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
