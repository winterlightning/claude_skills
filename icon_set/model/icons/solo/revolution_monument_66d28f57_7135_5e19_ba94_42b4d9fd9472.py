"""Revolution monument: reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '66d28f57-7135-5e19-ba94-42b4d9fd9472'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-03/revolution monument mexico_66d28f57-7135-5e19-ba94-42b4d9fd9472.svg'
AUTHOR = 'gpt-6'


class Landmark(Solo48):
    icon_id = 'revolution-monument'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('revolution monument', 'mexico city', 'monument', 'dome', 'arch', 'landmark', 'memorial', 'architecture')

    def build(self):
        # Centerline extremes: (2,2)-(46,46); domed arch monument.
        self.add_polyline("outline", (2,46), (2,28), (8,28), (24,28), (40,28), (46,28), (46,46), (32,46), (16,46), closed=True)
        self.add_line("drum-left", (8,28), (8,20))
        self.add_arc("dome-left", (8,20), (19,8), radius_x=11, radius_y=12)
        self.add_line("cap-left", (19,8), (19,2))
        self.add_line("cap-top", (19,2), (29,2))
        self.add_line("cap-right", (29,2), (29,8))
        self.add_arc("dome-right", (29,8), (40,20), radius_x=11, radius_y=12)
        self.add_line("drum-right", (40,20), (40,28))
        self.add_contour("dome", "drum-left", "dome-left", "cap-left", "cap-top", "cap-right", "dome-right", "drum-right")
        self.relate("connect", "dome", "outline")
        self.add_line("door-left", (16, 46), (16, 40))
        self.add_arc("door-top", (16, 40), (32, 40), radius_x=8)
        self.add_line("door-right", (32, 40), (32, 46))
        self.add_contour("door", "door-left", "door-top", "door-right")
        self.relate("connect", "door", "outline")
        self.add_polyline("drum-band", (8,20), (24,20), (40,20))
        self.relate("connect", "drum-band", "dome")
        self.add_line("drum-divider", (24,20), (24,28))
        self.relate("connect", "drum-divider", "drum-band")
        self.relate("connect", "drum-divider", "outline")
