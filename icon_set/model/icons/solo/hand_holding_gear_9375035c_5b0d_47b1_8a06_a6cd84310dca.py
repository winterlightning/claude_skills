"""A hand pinches a small toothed gear between a curved thumb and finger. The gear has a central circular hole, and the wrist rises along the right side before curving around it.
Lucide settings teeth and hand curved grasp. Four broad teeth and a center dot replace crowded teeth and a tiny ring. Upper finger and lower thumb hold the gear; right forearm is deliberately asymmetric.
SQUARE: centerline extremes (6,6)-(42,42); freshly authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9375035c-5b0d-47b1-8a06-a6cd84310dca'
SOURCE_PATH = 'pictographic-primitives/work/workflow teamwork cog hand_9375035c-5b0d-47b1-8a06-a6cd84310dca.svg'
AUTHOR = 'gpt-6'


class HandHoldingGear(Solo48):
    icon_id = 'hand-holding-gear'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "work"
    categories = ("work", "primitives")
    aliases = ()
    keywords = ('hand', 'gear', 'cog', 'holding', 'mechanism', 'teamwork')

    def build(self) -> None:
        self.add_polyline('gear', (14, 6), (22, 6), (22, 10), (26, 10), (26, 14), (30, 14), (30, 22), (26, 22), (26, 26), (22, 26), (22, 30), (14, 30), (14, 26), (10, 26), (10, 22), (6, 22), (6, 14), (10, 14), (10, 10), (14, 10), closed=True)
        self.add_dot('gear-hub', (18, 18))
        self.add_line('finger-top', (30, 14), (34, 14))
        self.add_arc('hand-round', (34, 14), (42, 22), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_line('arm', (42, 22), (42, 42))
        self.add_contour('upper-hand', 'finger-top', 'hand-round', 'arm', closed=False)
        self.relate("connect", 'upper-hand', 'gear')
        self.add_polyline('thumb-wrist', (22, 30), (30, 40), (30, 42), closed=False)
        self.relate("connect", 'thumb-wrist', 'gear')
