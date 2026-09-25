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
    category = "landmarks"
    aliases = ()
    keywords = ('revolution monument', 'mexico city', 'monument', 'dome', 'arch', 'landmark', 'memorial', 'architecture')

    def build(self):
        # SQUARE centerline extremes (6,6)-(42,42).
        # Building owns silhouette and attached architecture; repeat pairs share axes.
        self.add_polyline("outline", (6,42), (6,28), (10,28), (24,28), (38,28), (42,28), (42,42), (30,42), (18,42), closed=True)
        self.add_line("drum-left", (10,28), (10,20))
        self.add_arc("dome-left", (10,20), (24,6), radius_x=14)
        self.add_arc("dome-right", (24,6), (38,20), radius_x=14)
        self.add_line("drum-right", (38,20), (38,28))
        self.add_contour("dome", "drum-left", "dome-left", "dome-right", "drum-right")
        self.relate("connect", "dome", "outline")
        self.add_polyline("drum-band", (10,20), (24,20), (38,20))
        self.relate("connect", "drum-band", "dome")
        self.add_line("drum-divider", (24,20), (24,28))
        self.relate("connect", "drum-divider", "drum-band")
        self.relate("connect", "drum-divider", "outline")
        self.add_line("door-left", (18,42), (18,38))
        self.add_arc("door-top", (18,38), (30,38), radius_x=6)
        self.add_line("door-right", (30,38), (30,42))
        self.add_contour("door", "door-left", "door-top", "door-right")
        self.relate("connect", "door", "outline")
