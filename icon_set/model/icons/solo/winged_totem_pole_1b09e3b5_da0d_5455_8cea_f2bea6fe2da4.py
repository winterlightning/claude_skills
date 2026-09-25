'Rounded carved pole with paired eyes and outstretched wings. One shared silhouette opens the wing joins; small feather steps omitted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1b09e3b5-da0d-5455-8cea-f2bea6fe2da4'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-05/totem pole_1b09e3b5-da0d-5455-8cea-f2bea6fe2da4.svg'
AUTHOR = 'gpt-6'

class WingedTotemPole(Solo48):
    icon_id = 'winged-totem-pole'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "landmarks"
    aliases = ()
    keywords = ('totem', 'pole', 'carving', 'wings', 'indigenous', 'monument', 'tribal', 'landmark')

    def build(self) -> None:
        # SQUARE centerline extremes (6,6)-(42,42), mirrored about 24.
        self.add_arc("head", (11,19), (37,19), radius_x=13)
        points = [(37,19), (37,23), (42,23), (42,26), (31,30), (31,42), (17,42), (17,30), (6,26), (6,23), (11,23), (11,19)]
        for n,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f"right-wing-{n}", a, b)
        self.add_contour("outline", "head", *[f"right-wing-{n}" for n in range(1, 12)], closed=True)
        for side,x in (("left",20),("right",28)):
            self.add_dot("eye-"+side, (x,20))
