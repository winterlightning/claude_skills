"""A capital H and lowercase e share a long underline. SQUARE extremes (6,6)-(42,42). Lucide case-sensitive informs mixed-case proportion and round-bowl construction, not letter identity. Enlarge the e bowl and underline gap; preserve both letters and their cases."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5099a236-69df-4d18-a978-5f74d95d8836'
SOURCE_PATH = 'pictographic-primitives/symbol/he (text u)_5099a236-69df-4d18-a978-5f74d95d8836.svg'
AUTHOR = 'gpt-6'


class HeLettersUnderlined(Solo48):
    icon_id = 'he-letters-underlined'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('he', 'letters', 'hebrew', 'text', 'underline', 'language', 'typography', 'abbreviation')

    def build(self) -> None:
        self.add_polyline('h-left',(6,6),(6,19),(6,32))
        self.add_polyline('h-right',(18,6),(18,19),(18,32))
        self.add_line('h-crossbar',(6,19),(18,19))
        self.relate('connect','h-left','h-crossbar')
        self.relate('connect','h-right','h-crossbar')
        self.add_line('underline',(6,42),(42,42))
        self.add_arc('e-upper',(28,22),(42,22),radius_x=7,radius_y=10)
        self.add_line('e-bar',(42,22),(28,22))
        self.add_arc('e-lower',(28,22),(35,32),radius_x=7,radius_y=10,sweep=False)
        self.add_line('e-terminal',(35,32),(40,32))
        self.add_contour('e','e-upper','e-bar','e-lower','e-terminal')
