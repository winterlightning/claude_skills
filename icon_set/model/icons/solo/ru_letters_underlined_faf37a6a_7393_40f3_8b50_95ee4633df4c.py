"""Ru letter pair with underline. Lucide type informs sparse monoline letters; strikethrough informs coherent S curves where applicable. Conventional case retained; no characters omitted.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'faf37a6a-7393-40f3-8b50-95ee4633df4c'
SOURCE_PATH = 'pictographic-primitives/symbol/ru (text u)_faf37a6a-7393-40f3-8b50-95ee4633df4c.svg'
AUTHOR = 'gpt-6'


class RuLettersUnderlined(Solo48):
    icon_id = 'ru-letters-underlined'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('ru', 'letters', 'text', 'underline', 'typography', 'abbreviation', 'language')

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

        self.add_line('u-left',(30,14),(30,24))
        self.add_arc('u-bowl',(30,24),(42,24),radius_x=6,sweep=False)
        self.add_line('u-right',(42,24),(42,14))
        self.add_contour('u','u-left','u-bowl','u-right')
        self.add_line('underline',(6,42),(42,42))
