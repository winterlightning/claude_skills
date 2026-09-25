"""Sad Face with Glasses; independently reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ca0a75ab-88d3-50e5-88be-a787aaf67c94'
SOURCE_PATH = 'pictographic-primitives/smileys/sad nerd_ca0a75ab-88d3-50e5-88be-a787aaf67c94.svg'
AUTHOR = 'gpt-6'


class SadFaceWithGlasses(Solo48):
    icon_id = 'sad-face-with-glasses'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    aliases = ()
    keywords = ('sad', 'glasses', 'nerd', 'frown', 'face', 'emoji')

    def build(self) -> None:

        # CIRCLE: center (24,24), centerline radius20, visible radius22.
        axis,radius=24,20
        self.add_arc("head-top",(axis-radius,24),(axis+radius,24),radius_x=radius)
        self.add_arc("head-bottom",(axis+radius,24),(axis-radius,24),radius_x=radius)
        self.add_contour("head","head-top","head-bottom",closed=True)

        # Matched circular lenses and bridge, with the frown carrying sadness.
        for side,x in (("left",17),("right",31)):
            self.add_arc(f"lens-{side}-top",(x-3,19),(x+3,19),radius_x=3)
            self.add_arc(f"lens-{side}-bottom",(x+3,19),(x-3,19),radius_x=3)
            self.add_contour(f"lens-{side}",f"lens-{side}-top",f"lens-{side}-bottom",closed=True)
        self.add_line("bridge",(20,19),(28,19))
        for side in ("left","right"):
            for half in ("top","bottom"):self.relate("connect","bridge",f"lens-{side}-{half}")
        self.add_arc("frown",(18,33),(30,33),radius_x=9)
