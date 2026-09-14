"""Capital R and lowercase b above an underline. Lucide type informs sparse monoline letter construction; no useful exact letter-pair match. No letters or underline omitted.

SOLO48 SQUARE, live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c00033d9-12b6-41d1-a9cc-cbe615b46a96'
SOURCE_PATH = 'pictographic-primitives/symbol/rb (text u)_c00033d9-12b6-41d1-a9cc-cbe615b46a96.svg'
AUTHOR = 'gpt-6'


class RbLettersUnderlined(Solo48):
    icon_id = 'rb-letters-underlined'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('rb', 'letters', 'text', 'underline', 'typography', 'abbreviation', 'language')

    def build(self) -> None:

        self.add_line('r-stem-top',(6,6),(6,22))
        self.add_line('r-stem-bottom',(6,22),(6,30))
        self.add_contour('r-stem','r-stem-top','r-stem-bottom')
        self.add_line('r-top',(6,6),(12,6))
        self.add_arc('r-bowl',(12,6),(12,22),radius_x=8)
        self.add_line('r-return',(12,22),(6,22))
        self.add_contour('r-loop','r-top','r-bowl','r-return')
        self.add_line('r-leg',(12,22),(20,30))
        self.relate('connect','r-stem','r-loop')
        self.relate('connect','r-loop','r-leg')
        self.add_line('underline',(6,42),(42,42))

        self.add_line('b-stem-top',(30,6),(30,14))
        self.add_line('b-stem-low',(30,14),(30,30))
        self.add_contour('b-stem','b-stem-top','b-stem-low')
        self.add_arc('b-bowl',(30,14),(30,30),radius_x=12,radius_y=8)
        self.relate('connect','b-stem','b-bowl')
