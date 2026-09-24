from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "19dc1699-da2b-4e42-b072-21890cdb8a28"
SOURCE_PATH = "icon_set/work/todo-references/heart rate 1_19dc1699-da2b-4e42-b072-21890cdb8a28.svg"
AUTHOR = "gpt-6"
class HeartRate(Solo48):
    """A heart outline crossed by an attached heartbeat trace."""
    icon_id = "heart-rate-1"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/medical"
    aliases = ("heart pulse",)
    keywords = ("heartbeat", "health", "rate")
    def build(self):
        # Mirrored radius10 lobes; intentional asymmetric ECG crosses shared nodes.
        # Envelope centerline x4..44, y8..40, with axis24.
        axis, r = 24, 10
        self.add_arc("left-outer",(4,18),(14,8),radius_x=r)
        self.add_arc("left-inner",(14,8),(axis,12),radius_x=r,radius_y=4)
        self.add_arc("right-inner",(axis,12),(34,8),radius_x=r,radius_y=4)
        self.add_arc("right-outer",(34,8),(44,18),radius_x=r)
        self.add_arc("right-upper",(44,18),(42,24),radius_x=r)
        self.add_arc("right-lower",(42,24),(40,26),radius_x=r)
        self.add_line("right-side",(40,26),(axis,40))
        self.add_line("left-side",(axis,40),(8,26))
        self.add_arc("left-shoulder",(8,26),(4,18),radius_x=r)
        self.add_contour("heart","left-outer","left-inner","right-inner","right-outer","right-upper","right-lower","right-side","left-side","left-shoulder",closed=True)
        self.add_polyline("pulse",(8,26),(14,26),(19,20),(24,27),(30,24),(42,24))
        self.relate("connect","pulse","heart")
