"""An open palm-up hand presenting a three-node share network.

SOLO48 HRECT_L: visible (2, 6)-(46, 42), centerline (4, 8)-(44, 40).

Symbol plan: the hand is the library's palm-up hand (Lucide `hand-heart`
construction). Mirrored about x=24, a large hub ring (r4) rests on the thumb (its bottom
node splits the thumb's top edge) and branches by straight spokes up to two
smaller node rings (r3, the exempt 6-circle); each ring is a closed run of
cardinal quarter arcs so the spokes end on arc nodes.
Revision: the rejected drawing gave two upright hands as Y-shapes that did
not read (feedback: "hand"); one unmistakable open hand replaces them.
Construction reference: Lucide `hand-heart` (via `hand-holding-heart`) and
`share-2` (rings joined by spokes).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'faabe7b6-2ce7-47c5-a31b-881b93ad2845'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cupped-hands-share-component/20260926T152509Z-thuan-mac-1/reference/e learning share_faabe7b6-2ce7-47c5-a31b-881b93ad2845.svg'
AUTHOR = 'claude-opus-5-5'

AXIS = 24
HUB, HUB_R = (24, 20), 4
NODE_L, NODE_R = (11, 11), 3


def mx(p):
    return (2 * AXIS - p[0], p[1])


class Drawing(Solo48):
    icon_id = 'cupped-hands-share-component'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('e learning share', 'hand sharing network')
    keywords = ('share', 'network', 'e-learning', 'hand', 'connect', 'nodes', 'knowledge', 'offer')

    def ring(self, name, c, r):
        x, y = c
        pts = [(x + r, y), (x, y + r), (x - r, y), (x, y - r)]
        ids = []
        for i in range(4):
            self.add_arc(f'{name}-{i}', pts[i], pts[(i + 1) % 4], radius_x=r, sweep=True)
            ids.append(f'{name}-{i}')
        self.add_contour(name, *ids, closed=True)

    def build(self):
        self.ring('hub', HUB, HUB_R)
        for s, f in (('left', lambda p: p), ('right', mx)):
            node = f(NODE_L)
            self.ring(f'{s}-node', node, NODE_R)
            near = f((NODE_L[0] + NODE_R, NODE_L[1]))
            hub_side = f((HUB[0] - HUB_R, HUB[1]))
            self.add_line(f'{s}-spoke', hub_side, near)
            self.relate('connect', f'{s}-spoke', 'hub')
            self.relate('connect', f'{s}-spoke', f'{s}-node')
        # palm-up hand
        self.add_arc('palm-upper', (4, 28), (14, 24), radius_x=10, radius_y=4)
        self.add_line('thumb-top-l', (14, 24), (24, 24))
        self.add_line('thumb-top-r', (24, 24), (28, 24))
        self.add_arc('thumb-tip-upper', (28, 24), (32, 28), radius_x=4)
        self.add_arc('thumb-tip-lower', (32, 28), (28, 32), radius_x=4)
        self.add_line('thumb-bottom', (28, 32), (18, 32))
        self.add_contour('thumb', 'palm-upper', 'thumb-top-l', 'thumb-top-r', 'thumb-tip-upper', 'thumb-tip-lower', 'thumb-bottom')
        self.relate('connect', 'hub', 'thumb')
        self.add_line('fingers-upper', (32, 28), (38, 28))
        self.add_arc('fingertips', (38, 28), (44, 32), radius_x=6)
        self.add_line('fingers-lower', (44, 32), (34, 40))
        self.add_line('palm-base', (34, 40), (12, 40))
        self.add_line('wrist-lower', (12, 40), (4, 38))
        self.add_contour('hand', 'fingers-upper', 'fingertips', 'fingers-lower', 'palm-base', 'wrist-lower')
        self.relate('connect', 'thumb', 'hand')
