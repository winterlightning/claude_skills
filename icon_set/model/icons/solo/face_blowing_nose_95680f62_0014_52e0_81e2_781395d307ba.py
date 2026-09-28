"""Face Blowing Nose; independently reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '95680f62-0014-52e0-81e2-781395d307ba'
SOURCE_PATH = 'pictographic-primitives/smileys/nose blow_95680f62-0014-52e0-81e2-781395d307ba.svg'
AUTHOR = 'gpt-6'


class FaceBlowingNose(Solo48):
    icon_id = 'face-blowing-nose'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    categories = ("smileys", "primitives")
    aliases = ()
    keywords = ('nose', 'tissue', 'sneezing', 'cold', 'face', 'emoji')

    def build(self) -> None:

        # SQUARE ink (4,4)-(44,44); open lower face is covered by held tissue.
        self.add_arc("head",(6,24),(42,24),radius_x=18)
        for side,x in (("left",18),("right",30)):
            self.add_arc(f"eye-{side}",(x-1,18),(x+1,18),radius_x=2,sweep=False)

        self.add_polyline("tissue",(24,26),(38,42),(10,42),closed=True)
