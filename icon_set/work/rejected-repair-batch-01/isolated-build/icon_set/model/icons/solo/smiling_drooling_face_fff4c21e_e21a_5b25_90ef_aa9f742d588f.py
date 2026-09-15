"""Smiling Drooling Face; rebuilt from the supplied visual reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fff4c21e-e21a-5b25-90ef-aa9f742d588f'
SOURCE_PATH = 'pictographic-primitives/smileys/drool_fff4c21e-e21a-5b25-90ef-aa9f742d588f.svg'
AUTHOR = 'gpt-6'


class SmilingDroolingFace(Solo48):
    icon_id = 'smiling-drooling-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/emotions"
    aliases = ()
    keywords = ('drooling', 'smiling', 'drool', 'hungry', 'face', 'emoji')

    def build(self) -> None:

        # CIRCLE: ink radius 22; shared center (24,24), centerline radius 20.
        axis, radius = 24, 20
        self.add_arc("head-top",(axis-radius,24),(axis+radius,24),radius_x=radius)
        self.add_arc("head-bottom",(axis+radius,24),(axis-radius,24),radius_x=radius)
        self.add_contour("head","head-top","head-bottom",closed=True)

        for side,x in (("left",17),("right",31)):
            self.add_arc(f"eye-{side}",(x-2,18),(x+2,18),radius_x=2)

        self.add_arc("smile-left",(16,28),(30,30),radius_x=10,sweep=False)
        self.add_arc("smile-right",(30,30),(32,28),radius_x=10,sweep=False)
        self.add_contour("smile","smile-left","smile-right")
        self.add_line("drool",(30,30),(30,34))
        self.relate("connect","drool","smile-left")
        self.relate("connect","drool","smile-right")
