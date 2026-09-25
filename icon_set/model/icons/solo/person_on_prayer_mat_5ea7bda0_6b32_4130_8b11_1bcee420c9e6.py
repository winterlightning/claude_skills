"""A headscarf-wearing person kneels on a broad prayer mat. Keep covered head, compact body and trapezoidal mat; omit small arm and scarf folds."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5ea7bda0-6b32-4130-8b11-1bcee420c9e6'
SOURCE_PATH = 'pictographic-primitives/religion/islamic muslim pray salah_5ea7bda0-6b32-4130-8b11-1bcee420c9e6.svg'
AUTHOR = 'gpt-6'

class PersonOnPrayerMat(Solo48):
    icon_id = 'person-on-prayer-mat'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "religion"
    aliases = ()
    keywords = ('person', 'headscarf', 'prayer', 'mat', 'kneeling', 'worship')

    def oval(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def build(self) -> None:
        # Square centerline box (6,6)-(42,42); face and hood share x=24.
        self.add_arc('hood',(10,25),(38,25),radius_x=14,radius_y=19)
        self.add_polyline('body',(38,25),(32,33),(16,33),(10,25))
        self.relate('connect','hood','body')
        self.oval('face',24,19,4)
        self.add_polyline('mat',(6,35),(6,42),(42,42),(42,35))
