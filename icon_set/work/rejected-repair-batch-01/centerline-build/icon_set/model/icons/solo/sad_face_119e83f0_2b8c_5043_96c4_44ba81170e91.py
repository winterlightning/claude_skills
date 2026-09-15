"""Sad Face; independently reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '119e83f0-2b8c-5043-96c4-44ba81170e91'
SOURCE_PATH = 'pictographic-primitives/smileys/sad_119e83f0-2b8c-5043-96c4-44ba81170e91.svg'
AUTHOR = 'gpt-6'


class SadFace(Solo48):
    icon_id = 'sad-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/emotions"
    aliases = ()
    keywords = ('sad', 'sorrow', 'frown', 'worried', 'face', 'emoji')

    def build(self) -> None:

        # CIRCLE: center (24,24), centerline radius20, visible radius22.
        axis,radius=24,20
        self.add_arc("head-top",(axis-radius,24),(axis+radius,24),radius_x=radius)
        self.add_arc("head-bottom",(axis+radius,24),(axis-radius,24),radius_x=radius)
        self.add_contour("head","head-top","head-bottom",closed=True)

        for side,sign in (("left",1),("right",-1)):
            def p(x,y):return (24+sign*(x-24),y)
            self.add_arc(f"brow-{side}",p(17,16),p(19,14),radius_x=5,sweep=sign<0)
            self.add_dot(f"eye-{side}",p(16,24))
        self.add_arc("frown",(20,34),(28,34),radius_x=6)
