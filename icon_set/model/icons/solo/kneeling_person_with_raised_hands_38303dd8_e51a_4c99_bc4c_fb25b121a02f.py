"""A left-facing kneeling worshipper with hands raised before the chest. Keep folded legs, forward arms and head; combine the paired arms into one readable gesture."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '38303dd8-e51a-4c99-bc4c-fb25b121a02f'
SOURCE_PATH = 'pictographic-primitives/religion/islam pray_38303dd8-e51a-4c99-bc4c-fb25b121a02f.svg'
AUTHOR = 'gpt-6'

class KneelingPersonWithRaisedHands(Solo48):
    icon_id = 'kneeling-person-with-raised-hands'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture/religion"
    aliases = ()
    keywords = ('person', 'kneeling', 'prayer', 'hand', 'gesture', 'worship')

    def oval(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def build(self) -> None:
        # Centerline box (8,4)-(40,44), left-facing prayer posture.
        self.oval('head',23,10,6)
        self.add_polyline('back',(28,25),(33,34),(25,44),(40,44))
        self.add_polyline('arm',(28,25),(17,31),(8,22))
        self.relate('connect','back','arm')
        self.add_polyline('front',(21,34),(24,39),(17,44),(25,44))
        self.relate('connect','front','back')
