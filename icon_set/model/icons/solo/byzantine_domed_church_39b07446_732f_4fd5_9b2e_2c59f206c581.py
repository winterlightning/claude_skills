"""Byzantine Domed Church. Rebuilt from the supplied silhouette."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '39b07446-732f-4fd5-9b2e-2c59f206c581'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-01/mystras_39b07446-732f-4fd5-9b2e-2c59f206c581.svg'
AUTHOR = 'gpt-6'


class Landmark(Solo48):
    icon_id = 'byzantine-domed-church'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('mystras', 'byzantine', 'church', 'dome', 'greece', 'monastery', 'heritage', 'religion')

    def build(self):
        self.add_arc("dome", (10,20), (38,20), radius_x=14, radius_y=18)
        self.add_arc("left-outer", (2,28), (10,20), radius_x=8)
        self.add_arc("left-inner", (10,20), (18,28), radius_x=8)
        self.add_line("bridge", (18,28), (30,28))
        self.add_arc("right-inner", (30,28), (38,20), radius_x=8)
        self.add_arc("right-outer", (38,20), (46,28), radius_x=8)
        self.add_line("right-wall", (46,28), (46,46))
        self.add_line("left-wall", (2,46), (2,28))
        self.add_contour("outline", "left-wall", "left-outer", "left-inner", "bridge", "right-inner", "right-outer", "right-wall")
        self.relate("connect", "dome", "outline")
        self.add_polyline("band", (2,34), (46,34))
        self.relate("connect", "band", "outline")
        self.add_arc("arch-left", (9,46), (19,46), radius_x=5)
        self.add_arc("arch-center", (19,46), (29,46), radius_x=5)
        self.add_arc("arch-right", (29,46), (39,46), radius_x=5)
        self.add_contour("arcade", "arch-left", "arch-center", "arch-right")
