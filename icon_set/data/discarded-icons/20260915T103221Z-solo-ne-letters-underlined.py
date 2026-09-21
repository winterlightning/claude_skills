"""Capital N and lowercase e above an underline. SQUARE extremes (6,6)-(42,42). Lucide case-sensitive informs mixed-case height; use coherent elliptical e curves, retaining the diagonal N and full underline."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a54812d2-f0ae-4c8c-aec5-a9e3a0071ab2'
SOURCE_PATH = 'pictographic-primitives/symbol/ne (text u)_a54812d2-f0ae-4c8c-aec5-a9e3a0071ab2.svg'
AUTHOR = 'gpt-6'


class NeLettersUnderlined(Solo48):
    icon_id = 'ne-letters-underlined'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('ne', 'letters', 'text', 'underline', 'typography', 'abbreviation', 'language')

    def build(self) -> None:
        self.add_polyline('n',(6,32),(6,6),(18,32),(18,6))
        self.add_arc('e-upper',(28,22),(42,22),radius_x=7,radius_y=10)
        self.add_line('e-bar',(42,22),(28,22))
        self.add_arc('e-lower',(28,22),(35,32),radius_x=7,radius_y=10,sweep=False)
        self.add_line('e-terminal',(35,32),(40,32))
        self.add_contour('e','e-upper','e-bar','e-lower','e-terminal')
        self.add_line('underline',(6,42),(42,42))
