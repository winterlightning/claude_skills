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
        # Centerline extremes: (2,2)-(46,46); flag above a flared keep.
        self.add_polyline("outline", (2,46), (6,29), (6,20), (14,20), (14,27), (22,27), (22,20), (30,20), (30,27), (38,27), (38,20), (46,20), (46,29), (42,46), (30,46), (18,46), closed=True)
        self.add_polyline("flag", (22,20), (22,10), (22,2), (38,2), (34,6), (38,10), (22,10))
        self.relate("connect", "flag", "outline")
        self.add_line("door-left", (18, 46), (18, 39))
        self.add_arc("door-top", (18, 39), (30, 39), radius_x=6)
        self.add_line("door-right", (30, 39), (30, 46))
        self.add_contour("door", "door-left", "door-top", "door-right")
        self.relate("connect", "door", "outline")
