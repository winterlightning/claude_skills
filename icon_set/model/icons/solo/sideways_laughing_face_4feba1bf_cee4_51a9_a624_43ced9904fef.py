"""Sideways Laughing Face; rebuilt from the supplied visual reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4feba1bf-cee4-51a9-a624-43ced9904fef'
SOURCE_PATH = 'pictographic-primitives/smileys/lol sideways_4feba1bf-cee4-51a9-a624-43ced9904fef.svg'
AUTHOR = 'gpt-6'


class SidewaysLaughingFace(Solo48):
    icon_id = 'sideways-laughing-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    aliases = ()
    keywords = ('laughing', 'sideways', 'laugh', 'grin', 'face', 'emoji')

    def build(self) -> None:

        # CIRCLE: ink radius 22; shared center (24,24), centerline radius 20.
        axis, radius = 24, 20
        self.add_arc("head-top",(axis-radius,24),(axis+radius,24),radius_x=radius)
        self.add_arc("head-bottom",(axis+radius,24),(axis-radius,24),radius_x=radius)
        self.add_contour("head","head-top","head-bottom",closed=True)

        # Eyes follow a vertical pair; mouth is authored for this orientation.
        for side,y in (("top",17),("bottom",31)):
            self.add_arc(f"eye-{side}",(18,y-2),(18,y+2),radius_x=2,sweep=False)
        self.add_line("mouth-flat",(27,15),(27,33))
        self.add_arc("mouth-bowl",(27,33),(27,15),radius_x=8,radius_y=9,sweep=False)
        self.add_contour("mouth","mouth-flat","mouth-bowl",closed=True)
