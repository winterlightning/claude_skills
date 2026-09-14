"""Sb letter pair with underline. Lucide type informs sparse monoline letters; strikethrough informs coherent S curves where applicable. Conventional case retained; no characters omitted.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4374c108-630e-4085-9b64-899ed4675f23'
SOURCE_PATH = 'pictographic-primitives/symbol/sb (text u)_4374c108-630e-4085-9b64-899ed4675f23.svg'
AUTHOR = 'gpt-6'


class SbLettersUnderlined(Solo48):
    icon_id = 'sb-letters-underlined'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('sb', 'letters', 'text', 'underline', 'typography', 'abbreviation', 'language')

    def build(self) -> None:

        self.add_arc('s-crown',(20,12),(6,12),radius_x=7,radius_y=6,sweep=False)
        self.add_arc('s-upper-turn',(6,12),(13,18),radius_x=7,radius_y=6,sweep=False)
        self.add_arc('s-lower-turn',(13,18),(20,24),radius_x=7,radius_y=6)
        self.add_arc('s-base',(20,24),(6,24),radius_x=7,radius_y=6)
        self.add_contour('s','s-crown','s-upper-turn','s-lower-turn','s-base')

        self.add_line('b-stem-top',(30,6),(30,14))
        self.add_line('b-stem-bottom',(30,14),(30,30))
        self.add_contour('b-stem','b-stem-top','b-stem-bottom')
        self.add_arc('b-bowl',(30,14),(30,30),radius_x=12,radius_y=8)
        self.relate('connect','b-stem','b-bowl')
        self.add_line('underline',(6,42),(42,42))
