"""Crenellated castle tower: reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b638c75c-e761-5d73-8e35-dbb30e06a28e'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-03/historical building tower_b638c75c-e761-5d73-8e35-dbb30e06a28e.svg'
AUTHOR = 'gpt-6'


class Landmark(Solo48):
    icon_id = 'crenellated-castle-tower'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('castle', 'tower', 'keep', 'fortress', 'battlement', 'crenellation', 'medieval', 'defence')

    def build(self):
        # HRECT_L centerline extremes (6,8)-(42,40).
        # Building owns silhouette and attached architecture; repeat pairs share axes.
        # Three equal merlons and two equal notches share an 8-unit repeat.
        self.add_polyline("outline", (4,40), (8,24), (4,24), (4,8), (12,8), (12,16), (20,16), (20,8), (28,8), (28,16), (36,16), (36,8), (44,8), (44,24), (40,24), (44,40), (30,40), (18,40), closed=True)
        self.add_line("door-left", (18,40), (18,34))
        self.add_arc("door-top", (18,34), (30,34), radius_x=6)
        self.add_line("door-right", (30,34), (30,40))
        self.add_contour("door", "door-left", "door-top", "door-right")
        self.relate("connect", "door", "outline")
