"""Kissing Face; rebuilt from the supplied visual reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9bc2f7c9-9d3d-5587-a0c6-96cf98442f3a'
SOURCE_PATH = 'pictographic-primitives/smileys/kiss_9bc2f7c9-9d3d-5587-a0c6-96cf98442f3a.svg'
AUTHOR = 'gpt-6'


class KissingFace(Solo48):
    icon_id = 'kissing-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    categories = ("smileys", "primitives")
    aliases = ()
    keywords = ('kiss', 'kissing', 'lips', 'affection', 'face', 'emoji')

    def build(self) -> None:

        # CIRCLE: ink radius 22; shared center (24,24), centerline radius 20.
        axis, radius = 24, 20
        self.add_arc("head-top",(axis-radius,24),(axis+radius,24),radius_x=radius)
        self.add_arc("head-bottom",(axis+radius,24),(axis-radius,24),radius_x=radius)
        self.add_contour("head","head-top","head-bottom",closed=True)

        for side,x in (("left",17),("right",31)):
            self.add_arc(f"eye-{side}",(x-2,18),(x+2,18),radius_x=2)

        self.add_arc("lip-top",(23,26),(23,30),radius_x=2)
        self.add_arc("lip-bottom",(23,30),(23,34),radius_x=2)
        self.add_contour("lips","lip-top","lip-bottom")
