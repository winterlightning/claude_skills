"""Sneezing Face with Tissue; independently reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c599cef4-d857-592c-9a9b-c8fc87fd39c3'
SOURCE_PATH = 'pictographic-primitives/smileys/nose blow_c599cef4-d857-592c-9a9b-c8fc87fd39c3.svg'
AUTHOR = 'gpt-6'


class SneezingFaceWithTissue(Solo48):
    icon_id = 'sneezing-face-with-tissue'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    aliases = ()
    keywords = ('sneezing', 'tissue', 'nose', 'cold', 'face', 'emoji')

    def build(self) -> None:

        # SQUARE ink (4,4)-(44,44); open lower face is covered by held tissue.
        self.add_arc("head",(6,24),(42,24),radius_x=18)
        for side,x in (("left",18),("right",30)):
            self.add_arc(f"eye-{side}",(x-1,18),(x+1,18),radius_x=2,sweep=False)

        self.add_polyline("tissue",(24,26),(34,38),(25,42),(14,40),closed=True)
