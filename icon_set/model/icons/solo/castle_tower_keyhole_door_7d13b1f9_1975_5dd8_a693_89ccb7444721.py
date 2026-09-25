"""A crenellated tower has an arched security door. Lucide castle informs the arched doorway and repeated battlements. Reduce crenellations and keyhole to a short lock slot."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7d13b1f9-1975-5dd8-a693-89ccb7444721'
SOURCE_PATH = 'pictographic-primitives/protection/protection castle gate_7d13b1f9-1975-5dd8-a693-89ccb7444721.svg'
AUTHOR = 'gpt-6'


class ProtectionIcon(Solo48):
    icon_id = 'castle-tower-keyhole-door'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "protection"
    aliases = ()
    keywords = ('castle', 'tower', 'door', 'keyhole', 'lock', 'fortress', 'security', 'protection')

    def build(self):
        # SQUARE centerline extremes: (6,6)-(42,42).

        # Tower silhouette owns two broad merlons and a physical keyhole doorway.
        self.add_polyline('tower',(6,42),(6,6),(14,6),(14,14),(22,14),(26,14),(34,14),(34,6),(42,6),(42,42),(34,42),(14,42),closed=True)
        self.add_line('door-left',(14,42),(14,30))
        self.add_arc('door-arch',(14,30),(34,30),radius_x=10)
        self.add_line('door-right',(34,30),(34,42))
        self.add_contour('door','door-left','door-arch','door-right')
        self.relate('connect','door','tower')
        self.add_line('keyhole',(24,30),(24,34))
