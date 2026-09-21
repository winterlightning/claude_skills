"""Sc letter pair with underline. Lucide type informs sparse monoline letters; strikethrough informs coherent S curves where applicable. Conventional case retained; no characters omitted.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e8cbbf5a-0ea4-44b3-8f38-77598d857116'
SOURCE_PATH = 'pictographic-primitives/symbol/sc (text u)_e8cbbf5a-0ea4-44b3-8f38-77598d857116.svg'
AUTHOR = 'gpt-6'


class ScLettersUnderlined(Solo48):
    icon_id = 'sc-letters-underlined'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('sc', 'letters', 'text', 'underline', 'typography', 'abbreviation', 'language')

    def build(self) -> None:

        self.add_arc('s-crown',(20,12),(6,12),radius_x=7,radius_y=6,sweep=False)
        self.add_arc('s-upper-turn',(6,12),(13,18),radius_x=7,radius_y=6,sweep=False)
        self.add_arc('s-lower-turn',(13,18),(20,24),radius_x=7,radius_y=6)
        self.add_arc('s-base',(20,24),(6,24),radius_x=7,radius_y=6)
        self.add_contour('s','s-crown','s-upper-turn','s-lower-turn','s-base')

        self.add_arc('c-top',(42,16),(30,22),radius_x=8,radius_y=8,sweep=False)
        self.add_arc('c-bottom',(30,22),(42,28),radius_x=8,radius_y=8,sweep=False)
        self.add_contour('c','c-top','c-bottom')
        self.add_line('underline',(6,42),(42,42))
