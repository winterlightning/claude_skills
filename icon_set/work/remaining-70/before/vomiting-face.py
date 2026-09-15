"""Vomiting Face; independently reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '062992ad-f866-48c1-b3db-7b22afb71752'
SOURCE_PATH = 'pictographic-primitives/smileys/throw up_062992ad-f866-48c1-b3db-7b22afb71752.svg'
AUTHOR = 'gpt-6'


class VomitingFace(Solo48):
    icon_id = 'vomiting-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/emotions"
    aliases = ()
    keywords = ('vomiting', 'sick', 'nausea', 'throw up', 'face', 'emoji')

    def build(self) -> None:

        # SQUARE: open lower head with one broad continuous stream and uneven pool.
        self.add_arc("head",(6,24),(42,24),radius_x=18)
        for side,sign in (("left",1),("right",-1)):
            def p(x,y):return (24+sign*(x-24),y)
            self.add_polyline(f"eye-{side}",p(18,17),p(20,19),p(18,21))
        self.add_polyline("flow",(16,30),(32,30),(32,35),(40,39),(40,42),(32,40),(24,42),(16,40),(8,42),(8,39),(16,35),closed=True)
