"""Connected Nodes. Retains the identifying silhouette and visible features.

VRECT_L visible extremes (6, 2, 42, 46); centerlines (8, 4, 40, 44).
Lucide share-2: three equal circular nodes joined by two clean diagonal links.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1cca002e-6e10-4b77-a9bd-bdca69594b0c'
SOURCE_PATH = 'pictographic-primitives/symbol/design vector_1cca002e-6e10-4b77-a9bd-bdca69594b0c.svg'
AUTHOR = 'gpt-6'


class NodesConnectedAngle(Solo48):
    icon_id = 'nodes-connected-angle'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ()
    keywords = ('nodes', 'vector', 'share', 'network', 'connection', 'graph', 'design', 'points')

    def build(self) -> None:
        self.add_arc('left-node-right', (14, 18), (14, 30), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('left-node-left', (14, 30), (14, 18), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('left-node', 'left-node-right', 'left-node-left', closed=True)
        self.add_arc('top-node-right', (34, 4), (34, 16), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('top-node-left', (34, 16), (34, 4), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('top-node', 'top-node-right', 'top-node-left', closed=True)
        self.add_arc('bottom-node-right', (34, 32), (34, 44), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('bottom-node-left', (34, 44), (34, 32), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('bottom-node', 'bottom-node-right', 'bottom-node-left', closed=True)
        self.add_line('top-link', (14, 18), (28, 10))
        self.add_line('bottom-link', (14, 30), (28, 38))
        self.relate("connect", 'left-node', 'top-link')
        self.relate("connect", 'top-node', 'top-link')
        self.relate("connect", 'left-node', 'bottom-link')
        self.relate("connect", 'bottom-node', 'bottom-link')
