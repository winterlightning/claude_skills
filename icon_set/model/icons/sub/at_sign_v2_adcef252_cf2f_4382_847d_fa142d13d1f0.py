"""Inner asymmetric bowl connected to the right return; complete open outer sweep. Complete-source repair; previous variant preserved."""
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Inner asymmetric bowl connected to the right return; complete open outer sweep. Complete-source repair; previous variant preserved.'
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'At Sign: A circular inner bowl joins a returning curve on the right, surrounded by a broad outer loop. The outer loop remains open near the lower-right edge.\n\nConstruction: An inner circular bowl joins an angled return and broad outer circular loop; retain the open lower-right ending.\nKeyshape: SQUARE; authored to the SUB32 envelope.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'adcef252-cf2f-4382-847d-fa142d13d1f0'
SOURCE_PATH = 'pictographic-primitives/state/@ (text)_adcef252-cf2f-4382-847d-fa142d13d1f0.svg'
AUTHOR = 'gpt-6'

class AtSignVariant2(SourceFaithfulSideSub):
    icon_id = 'at-sign-v2'
    variant_of = 'at-sign'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('sign', 'circular', 'inner', 'bowl', 'joins', 'returning', 'curve', 'right')
    keyshape = Keyshape.SQUARE
    canvas_width = 32
    canvas_height = 32

    def build(self):
        """Inner asymmetric bowl connected to the right return; complete open outer sweep."""
        self.add_bezier('bowl-top', (22, 17), ((25, 5), (9, 7), (10, 17)))
        self.add_bezier('bowl-bottom', (10, 17), ((10, 25), (18, 24), (22, 20)))
        self.add_line('bowl-join', (22, 20), (22, 17))
        self.add_contour('bowl', 'bowl-top', 'bowl-bottom', 'bowl-join', closed=True)
        self.add_bezier('return', (22, 20), ((25, 26), (30, 23), (30, 16)))
        self.add_bezier('outer-tr', (30, 16), ((30, 8), (24, 2), (16, 2)))
        self.add_bezier('outer-tl', (16, 2), ((8, 2), (2, 8), (2, 16)))
        self.add_bezier('outer-bl', (2, 16), ((2, 24), (8, 30), (16, 30)))
        self.add_bezier('outer-end', (16, 30), ((18, 30), (20, 30), (22, 29)))
        self.add_contour('outer', 'return', 'outer-tr', 'outer-tl', 'outer-bl', 'outer-end')
        self.relate('connect', 'bowl', 'outer')

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
