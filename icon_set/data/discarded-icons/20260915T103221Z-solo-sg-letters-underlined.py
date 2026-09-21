"""Sg letter pair with underline. Lucide type informs sparse monoline letters; strikethrough informs coherent S curves where applicable. Conventional case retained; no characters omitted.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3569420b-b180-4388-8019-22de44d27527'
SOURCE_PATH = 'pictographic-primitives/symbol/sg (text u)_3569420b-b180-4388-8019-22de44d27527.svg'
AUTHOR = 'gpt-6'


class SgLettersUnderlined(Solo48):
    icon_id = 'sg-letters-underlined'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('sg', 'letters', 'text', 'underline', 'typography', 'abbreviation', 'language')

    def build(self) -> None:

        self.add_arc('s-crown',(20,12),(6,12),radius_x=7,radius_y=6,sweep=False)
        self.add_arc('s-upper-turn',(6,12),(13,18),radius_x=7,radius_y=6,sweep=False)
        self.add_arc('s-lower-turn',(13,18),(20,24),radius_x=7,radius_y=6)
        self.add_arc('s-base',(20,24),(6,24),radius_x=7,radius_y=6)
        self.add_contour('s','s-crown','s-upper-turn','s-lower-turn','s-base')

        self.add_arc('g-bowl',(42,12),(42,24),radius_x=12,radius_y=6,sweep=False)
        self.add_line('g-stem-upper',(42,12),(42,24))
        self.add_line('g-stem-lower',(42,24),(42,28))
        self.add_contour('g-stem','g-stem-upper','g-stem-lower')
        self.add_arc('g-tail',(42,28),(30,28),radius_x=6,radius_y=5)
        self.relate('connect','g-bowl','g-stem')
        self.relate('connect','g-stem','g-tail')
        self.add_line('underline',(6,42),(42,42))
