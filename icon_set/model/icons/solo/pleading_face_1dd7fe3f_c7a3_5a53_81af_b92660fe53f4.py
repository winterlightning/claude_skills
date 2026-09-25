"""Pleading Face; independently reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1dd7fe3f-c7a3-5a53-81af-b92660fe53f4'
SOURCE_PATH = 'pictographic-primitives/smileys/smoji pleading face_1dd7fe3f-c7a3-5a53-81af-b92660fe53f4.svg'
AUTHOR = 'gpt-6'


class PleadingFace(Solo48):
    icon_id = 'pleading-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    aliases = ()
    keywords = ('pleading', 'begging', 'sad', 'eyes', 'face', 'emoji')

    def build(self) -> None:

        # CIRCLE: visible radius22; shared center (24,24), centerline radius20.
        axis,radius=24,20
        self.add_arc("head-top",(axis-radius,24),(axis+radius,24),radius_x=radius)
        self.add_arc("head-bottom",(axis+radius,24),(axis-radius,24),radius_x=radius)
        self.add_contour("head","head-top","head-bottom",closed=True)

        # Raised inner brows continue into two large open eye curls.
        for side,sign in (("left",1),("right",-1)):
            def p(x,y):return (24+sign*(x-24),y)
            self.add_line(f"brow-{side}",p(18,14),p(15,17))
            self.add_arc(f"eye-{side}-top",p(15,17),p(19,21),radius_x=4,sweep=sign>0)
            self.add_arc(f"eye-{side}-bottom",p(19,21),p(15,25),radius_x=4,sweep=sign>0)
            self.add_contour(f"expression-{side}",f"brow-{side}",f"eye-{side}-top",f"eye-{side}-bottom")
        self.add_arc("frown",(20,34),(28,34),radius_x=6)
