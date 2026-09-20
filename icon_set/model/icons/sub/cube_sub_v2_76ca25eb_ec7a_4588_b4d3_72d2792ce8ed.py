"""Magnifying glass enclosing the complete three-face cube. Complete-source repair; previous variant preserved."""
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Magnifying glass enclosing the complete three-face cube. Complete-source repair; previous variant preserved.'
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Cube: A cube is shown from above with a diamond-shaped top and two upright side faces meeting at a central vertical edge. Generate this component alone; exclude Magnifying Glass Frame.\n\nConstruction: An isometric cube preserves its diamond top and two side faces around one centre edge.\nKeyshape: VRECT_XL; authored to the SUB32 envelope.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '76ca25eb-ec7a-4588-b4d3-72d2792ce8ed'
SOURCE_PATH = 'pictographic-primitives/state/magnifying glass cube_76ca25eb-ec7a-4588-b4d3-72d2792ce8ed.svg'
AUTHOR = 'gpt-6'

class CubeSubVariant2(SourceFaithfulSideSub):
    icon_id = 'cube-sub-v2'
    variant_of = 'cube-sub'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('cube', 'shown', 'diamond', 'shaped', 'top', 'upright', 'side', 'faces')
    keyshape = Keyshape.SQUARE
    canvas_width = 48
    canvas_height = 48

    def build(self):
        """Magnifying glass enclosing the complete three-face cube."""
        circle(self, 'glass', 21, 21, 19)
        self.add_line('handle', (35, 35), (46, 46))
        self.relate('connect', 'glass', 'handle')
        self.add_polyline('cube', (11, 15), (21, 10), (31, 15), (31, 27), (21, 33), (11, 27), (11, 15), closed=True)
        self.add_polyline('faces', (11, 15), (21, 21), (31, 15))
        self.add_line('vertical', (21, 21), (21, 33))
        self.relate('connect', 'cube', 'faces')
        self.relate('connect', 'cube', 'vertical')
        self.relate('connect', 'faces', 'vertical')

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
