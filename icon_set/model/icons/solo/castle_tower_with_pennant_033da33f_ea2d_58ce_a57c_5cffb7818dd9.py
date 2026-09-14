"""Castle tower with pennant: reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '033da33f-ea2d-58ce-a57c-5cffb7818dd9'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-03/historical building castle_033da33f-ea2d-58ce-a57c-5cffb7818dd9.svg'
AUTHOR = 'gpt-6'


class Landmark(Solo48):
    icon_id = 'castle-tower-with-pennant'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('castle', 'tower', 'turret', 'fortress', 'battlement', 'flag', 'pennant', 'medieval')

    def build(self):
        # SQUARE centerline extremes (6,6)-(42,42).
        # Building owns silhouette and attached architecture; repeat pairs share axes.
        # Pennant is physically attached; two merlons leave space above the arch.
        self.add_polyline("outline", (6,42), (10,28), (6,24), (6,18), (14,18), (14,24), (24,24), (34,24), (34,18), (42,18), (42,24), (38,28), (42,42), (30,42), (18,42), closed=True)
        self.add_polyline("flag", (24,24), (24,14), (24,6), (36,6), (36,14), (24,14))
        self.relate("connect", "flag", "outline")
        self.add_line("door-left", (18,42), (18,38))
        self.add_arc("door-top", (18,38), (30,38), radius_x=6)
        self.add_line("door-right", (30,38), (30,42))
        self.add_contour("door", "door-left", "door-top", "door-right")
        self.relate("connect", "door", "outline")
