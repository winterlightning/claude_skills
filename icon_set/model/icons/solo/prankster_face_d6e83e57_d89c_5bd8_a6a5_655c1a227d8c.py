"""Prankster Face; independently reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd6e83e57-d89c-5bd8-a6a5-655c1a227d8c'
SOURCE_PATH = 'pictographic-primitives/smileys/prank_d6e83e57-d89c-5bd8-a6a5-655c1a227d8c.svg'
AUTHOR = 'gpt-6'


class PranksterFace(Solo48):
    icon_id = 'prankster-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    categories = ("smileys", "primitives")
    aliases = ()
    keywords = ('prank', 'mischief', 'tongue', 'playful', 'face', 'emoji')

    def build(self) -> None:

        # CIRCLE: center (24,24), centerline radius20, visible radius22.
        axis,radius=24,20
        self.add_arc("head-top",(axis-radius,24),(axis+radius,24),radius_x=radius)
        self.add_arc("head-bottom",(axis+radius,24),(axis-radius,24),radius_x=radius)
        self.add_contour("head","head-top","head-bottom",closed=True)

        # The eyebrows and curled eyes share intentional inner attachment nodes.
        for side,sign in (("left",1),("right",-1)):
            def p(x,y):return (24+sign*(x-24),y)
            self.add_line(f"brow-{side}",p(17,15),p(19,17))
            self.add_arc(f"eye-{side}",p(19,17),p(18,20),radius_x=3,sweep=sign>0)
            self.add_contour(f"expression-{side}",f"brow-{side}",f"eye-{side}")
        self.add_arc("smile-left",(16,29),(20,30),radius_x=8,sweep=False)
        self.add_line("tongue-left",(20,30),(20,31))
        self.add_arc("tongue-tip",(20,31),(28,31),radius_x=4,sweep=False)
        self.add_line("tongue-right",(28,31),(28,30))
        self.add_arc("smile-right",(28,30),(32,29),radius_x=8,sweep=False)
        self.add_contour("mouth","smile-left","tongue-left","tongue-tip","tongue-right","smile-right")
