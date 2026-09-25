from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'House: A house has a pointed gable roof, short projecting eaves, and a rectangular body interrupted below by a rounded doorway. Generate this component alone; exclude Circle Frame.\n\nConstruction: A peaked roof projects over walls; an arched doorway interrupts the lower outline.\nKeyshape: SQUARE; authored to the SUB32 envelope.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '37b7d84a-3d3a-4e68-9fa0-db3c6d240895'
SOURCE_PATH = 'pictographic-primitives/state/house circle_37b7d84a-3d3a-4e68-9fa0-db3c6d240895.svg'
AUTHOR = 'gpt-6'

class HouseSubVariant2(SourceFaithfulSideSub):
    icon_id = 'house-sub-v2'
    variant_of = 'house-sub'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('house', 'pointed', 'gable', 'roof', 'short', 'projecting', 'eaves', 'rectangular')
    keyshape = Keyshape.SQUARE
    canvas_width = 64
    canvas_height = 64

    def build(self):
        """Complete circular outline and house with projecting roof, side walls and rounded doorway."""
        circle(self, 'frame', 32, 32, 30)
        self.add_polyline('roof', (12, 30), (32, 10), (52, 30))
        self.add_polyline('left', (18, 24), (18, 46), (26, 46), (26, 38))
        self.add_arc('door', (26, 38), (38, 38), radius_x=6, sweep=True)
        self.add_polyline('right', (38, 38), (38, 46), (46, 46), (46, 24))
        self.relate('connect', 'roof', 'left')
        self.relate('connect', 'roof', 'right')
        self.relate('connect', 'left', 'door')
        self.relate('connect', 'right', 'door')
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
