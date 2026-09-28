"""Head with Monocle; rebuilt from the supplied visual reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8c354f7c-447b-4033-85e4-6924e236563c'
SOURCE_PATH = 'pictographic-primitives/smileys/face with monocle_8c354f7c-447b-4033-85e4-6924e236563c.svg'
AUTHOR = 'gpt-6'


class HeadWithMonocle(Solo48):
    icon_id = 'head-with-monocle'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    categories = ("smileys", "primitives")
    aliases = ()
    keywords = ('monocle', 'head', 'eyewear', 'face', 'emoji')

    def build(self) -> None:

        # CIRCLE with the right cheek interrupted for the monocle cord.
        self.add_arc("head",(24,4),(36,40),radius_x=20,large_arc=True,sweep=False)
        self.add_arc("lens-upper",(25,18),(37,18),radius_x=6)
        self.add_arc("lens-lower-right",(37,18),(31,24),radius_x=6)
        self.add_arc("lens-lower-left",(31,24),(25,18),radius_x=6)
        self.add_contour("monocle","lens-upper","lens-lower-right","lens-lower-left",closed=True)
        self.add_line("cord",(31,24),(31,32))
        self.relate("connect","cord","lens-lower-right")
        self.relate("connect","cord","lens-lower-left")
