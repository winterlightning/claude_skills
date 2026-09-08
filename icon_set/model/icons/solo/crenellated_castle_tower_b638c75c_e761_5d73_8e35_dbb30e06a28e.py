"""Crenellated castle tower: reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b638c75c-e761-5d73-8e35-dbb30e06a28e'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-03/historical building tower_b638c75c-e761-5d73-8e35-dbb30e06a28e.svg'
AUTHOR = 'gpt-6'


class Landmark(Solo48):
    icon_id = 'crenellated-castle-tower'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('castle', 'tower', 'keep', 'fortress', 'battlement', 'crenellation', 'medieval', 'defence')

    def build(self):
        # Centerline extremes: (5,2)-(43,46); three broad merlons.
        self.add_polyline("outline", (5,46), (9,18), (5,18), (5,2), (13,2), (13,10), (20,10), (20,2), (28,2), (28,10), (35,10), (35,2), (43,2), (43,18), (39,18), (43,46), (30,46), (18,46), closed=True)
        self.add_line("door-left", (18, 46), (18, 35))
        self.add_arc("door-top", (18, 35), (30, 35), radius_x=6)
        self.add_line("door-right", (30, 35), (30, 46))
        self.add_contour("door", "door-left", "door-top", "door-right")
        self.relate("connect", "door", "outline")
