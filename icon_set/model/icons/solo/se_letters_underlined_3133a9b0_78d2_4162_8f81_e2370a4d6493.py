"""Se letter pair with underline. Lucide type informs sparse monoline letters; strikethrough informs coherent S curves where applicable. Conventional case retained; no characters omitted.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3133a9b0-78d2-4162-8f81-e2370a4d6493'
SOURCE_PATH = 'pictographic-primitives/symbol/se (text u)_3133a9b0-78d2-4162-8f81-e2370a4d6493.svg'
AUTHOR = 'gpt-6'


class SeLettersUnderlined(Solo48):
    icon_id = 'se-letters-underlined'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('se', 'letters', 'text', 'underline', 'typography', 'abbreviation', 'language')

    def build(self) -> None:

        self.add_arc('s-crown',(20,12),(6,12),radius_x=7,radius_y=6,sweep=False)
        self.add_arc('s-upper-turn',(6,12),(13,18),radius_x=7,radius_y=6,sweep=False)
        self.add_arc('s-lower-turn',(13,18),(20,24),radius_x=7,radius_y=6)
        self.add_arc('s-base',(20,24),(6,24),radius_x=7,radius_y=6)
        self.add_contour('s','s-crown','s-upper-turn','s-lower-turn','s-base')

        self.add_arc('e-top',(30,22),(42,22),radius_x=6,radius_y=8)
        self.add_line('e-bar',(42,22),(30,22))
        self.add_contour('e-loop','e-top','e-bar',closed=True)
        self.add_arc('e-bottom-left',(30,22),(36,30),radius_x=6,radius_y=8,sweep=False)
        self.add_arc('e-bottom-right',(36,30),(42,26),radius_x=6,radius_y=4,sweep=False)
        self.add_contour('e-bottom','e-bottom-left','e-bottom-right')
        self.relate('connect','e-loop','e-bottom')
        self.add_line('underline',(6,42),(42,42))
