"""Scrunched Face; independently reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2ac35bc8-5b94-5a5e-b358-b853fb1b7aca'
SOURCE_PATH = 'pictographic-primitives/smileys/shook_2ac35bc8-5b94-5a5e-b358-b853fb1b7aca.svg'
AUTHOR = 'gpt-6'


class ScrunchedFace(Solo48):
    icon_id = 'scrunched-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    categories = ("smileys", "primitives")
    aliases = ()
    keywords = ('scrunched', 'grimace', 'tense', 'distress', 'face', 'emoji')

    def build(self) -> None:

        # CIRCLE: visible radius22; shared center (24,24), centerline radius20.
        axis,radius=24,20
        self.add_arc("head-top",(axis-radius,24),(axis+radius,24),radius_x=radius)
        self.add_arc("head-bottom",(axis+radius,24),(axis-radius,24),radius_x=radius)
        self.add_contour("head","head-top","head-bottom",closed=True)

        for side,sign in (("left",1),("right",-1)):
            def p(x,y):return (24+sign*(x-24),y)
            self.add_polyline(f"eye-{side}",p(16,16),p(20,19),p(16,22))
        self.add_arc("mouth-left",(16,32),(22,32),radius_x=3,radius_y=2)
        self.add_arc("mouth-center",(22,32),(26,32),radius_x=2,radius_y=2,sweep=False)
        self.add_arc("mouth-right",(26,32),(32,32),radius_x=3,radius_y=2)
        self.add_contour("mouth","mouth-left","mouth-center","mouth-right")
