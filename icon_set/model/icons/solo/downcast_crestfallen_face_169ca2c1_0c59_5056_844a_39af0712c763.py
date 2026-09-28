"""Crestfallen Face; independently reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '169ca2c1-0c59-5056-844a-39af0712c763'
SOURCE_PATH = 'pictographic-primitives/smileys/sad face_169ca2c1-0c59-5056-844a-39af0712c763.svg'
AUTHOR = 'gpt-6'


class DowncastCrestfallenFace(Solo48):
    icon_id = 'downcast-crestfallen-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    categories = ("smileys", "primitives")
    aliases = ()
    keywords = ('crestfallen', 'sad', 'frown', 'disappointed', 'face', 'emoji')

    def build(self) -> None:

        # CIRCLE: center (24,24), centerline radius20, visible radius22.
        axis,radius=24,20
        self.add_arc("head-top",(axis-radius,24),(axis+radius,24),radius_x=radius)
        self.add_arc("head-bottom",(axis+radius,24),(axis-radius,24),radius_x=radius)
        self.add_contour("head","head-top","head-bottom",closed=True)

        for side,sign in (("left",1),("right",-1)):
            def p(x,y):return (24+sign*(x-24),y)
            self.add_arc(f"brow-{side}",p(18,15),p(19,14),radius_x=4,sweep=sign<0)
            self.add_arc(f"eye-{side}",p(15,24),p(19,24),radius_x=3,sweep=sign<0)
        self.add_arc("frown",(18,34),(30,34),radius_x=10)
