"""Rn letter pair with underline. Lucide type informs sparse monoline letters; strikethrough informs coherent S curves where applicable. Conventional case retained; no characters omitted.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '65550daf-4dd0-4b5a-999f-640ed02a8414'
SOURCE_PATH = 'pictographic-primitives/symbol/rn (text u)_65550daf-4dd0-4b5a-999f-640ed02a8414.svg'
AUTHOR = 'gpt-6'


class RnLettersUnderlined(Solo48):
    icon_id = 'rn-letters-underlined'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('rn', 'letters', 'text', 'underline', 'typography', 'abbreviation', 'language')

    def build(self) -> None:

        self.add_line('r-stem-upper',(6,6),(6,22))
        self.add_line('r-stem-lower',(6,22),(6,30))
        self.add_contour('r-stem','r-stem-upper','r-stem-lower')
        self.add_line('r-top',(6,6),(12,6))
        self.add_arc('r-bowl',(12,6),(12,22),radius_x=8)
        self.add_line('r-return',(12,22),(6,22))
        self.add_contour('r-loop','r-top','r-bowl','r-return')
        self.add_line('r-leg',(12,22),(20,30))
        self.relate('connect','r-stem','r-loop')
        self.relate('connect','r-loop','r-leg')

        self.add_line('n-left',(30,30),(30,20))
        self.add_arc('n-arch',(30,20),(42,20),radius_x=6)
        self.add_line('n-right',(42,20),(42,30))
        self.add_contour('n','n-left','n-arch','n-right')
        self.add_line('underline',(6,42),(42,42))
