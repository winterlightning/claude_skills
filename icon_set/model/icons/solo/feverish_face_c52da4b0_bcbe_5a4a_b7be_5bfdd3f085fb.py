"""Feverish Face; rebuilt from the supplied visual reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c52da4b0-bcbe-5a4a-b7be-5bfdd3f085fb'
SOURCE_PATH = 'pictographic-primitives/smileys/fever_c52da4b0-bcbe-5a4a-b7be-5bfdd3f085fb.svg'
AUTHOR = 'gpt-6'


class FeverishFace(Solo48):
    icon_id = 'feverish-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    categories = ("smileys", "primitives")
    aliases = ()
    keywords = ('fever', 'ill', 'sick', 'frown', 'face', 'emoji')

    def build(self) -> None:

        # CIRCLE: ink radius 22; shared center (24,24), centerline radius 20.
        axis, radius = 24, 20
        self.add_arc("head-top",(axis-radius,24),(axis+radius,24),radius_x=radius)
        self.add_arc("head-bottom",(axis+radius,24),(axis-radius,24),radius_x=radius)
        self.add_contour("head","head-top","head-bottom",closed=True)

        # A single smooth forehead wave contrasts with paired weary eyes.
        self.add_arc("brow-left",(18,15),(24,15),radius_x=6)
        self.add_arc("brow-right",(24,15),(30,15),radius_x=6,sweep=False)
        self.add_contour("brow","brow-left","brow-right")
        for side,sign in (("left",1),("right",-1)):
            self.add_arc(f"eye-{side}",(24+sign*(15-24),24),(24+sign*(19-24),24),radius_x=3,sweep=sign<0)
        self.add_arc("frown",(20,34),(28,34),radius_x=6)
