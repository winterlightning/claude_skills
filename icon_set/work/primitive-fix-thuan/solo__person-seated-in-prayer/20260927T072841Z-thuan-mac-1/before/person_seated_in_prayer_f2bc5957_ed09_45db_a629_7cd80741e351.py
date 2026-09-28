"""A left-facing person sits back on folded legs with an arm resting toward the knees. Keep the upright back and low hand placement; omit duplicate limb outlines."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f2bc5957-ed09-45db-a629-7cd80741e351'
SOURCE_PATH = 'pictographic-primitives/religion/islamic before bowing_f2bc5957-ed09-45db-a629-7cd80741e351.svg'
AUTHOR = 'gpt-6'

class PersonSeatedInPrayer(Solo48):
    icon_id = 'person-seated-in-prayer'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "religion"
    categories = ("primitives", "religion")
    aliases = ()
    keywords = ('person', 'prayer', 'kneeling', 'seated', 'worship', 'posture')

    def oval(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def build(self) -> None:
        # Centerline box (8,4)-(40,44), left-facing resting prayer posture.
        self.oval('head',23,10,6)
        self.add_polyline('back',(28,25),(32,35),(25,44),(40,44))
        self.add_polyline('arm',(28,25),(17,36),(8,36))
        self.relate('connect','back','arm')
        self.add_polyline('legs',(17,36),(14,44),(25,44));self.relate('connect','legs','arm');self.relate('connect','legs','back')
