"""Capital R and lowercase f above an underline. Lucide type informs sparse monoline letter construction; no useful exact letter-pair match. No letters or underline omitted.

SOLO48 SQUARE, live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8242da2c-63f3-4dca-b0e7-542ae0f60a4f'
SOURCE_PATH = 'pictographic-primitives/symbol/rf (text u)_8242da2c-63f3-4dca-b0e7-542ae0f60a4f.svg'
AUTHOR = 'gpt-6'


class RfLettersUnderlined(Solo48):
    icon_id = 'rf-letters-underlined'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('rf', 'letters', 'text', 'underline', 'typography', 'abbreviation', 'language')

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

        self.add_arc('f-hook',(32,14),(40,6),radius_x=8)
        self.add_line('f-stem-top',(32,14),(32,18))
        self.add_line('f-stem-low',(32,18),(32,30))
        self.add_contour('f-stem','f-stem-top','f-stem-low')
        self.add_polyline('f-bar',(28,18),(32,18),(42,18))
        self.relate('connect','f-stem','f-hook')
        self.relate('connect','f-stem','f-bar')
