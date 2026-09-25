"""Grumpy Face; rebuilt from the supplied visual reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7812138e-8e53-4637-b34d-3c3244ed3085'
SOURCE_PATH = 'pictographic-primitives/smileys/grumpy_7812138e-8e53-4637-b34d-3c3244ed3085.svg'
AUTHOR = 'gpt-6'


class GrumpyFace(Solo48):
    icon_id = 'grumpy-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    aliases = ()
    keywords = ('grumpy', 'tired', 'frown', 'stern', 'face', 'emoji')

    def build(self) -> None:

        # CIRCLE: ink radius 22; shared center (24,24), centerline radius 20.
        axis, radius = 24, 20
        self.add_arc("head-top",(axis-radius,24),(axis+radius,24),radius_x=radius)
        self.add_arc("head-bottom",(axis+radius,24),(axis-radius,24),radius_x=radius)
        self.add_contour("head","head-top","head-bottom",closed=True)

        for side,sign in (("left",1),("right",-1)):
            def p(x,y): return (24+sign*(x-24),y)
            self.add_line(f"brow-{side}",p(17,15),p(20,15))
            self.add_line(f"eye-{side}",p(15,24),p(19,24))
        self.add_arc("frown",(18,34),(30,34),radius_x=11)
