"""Capital L and lowercase u over an underline. SQUARE extremes (6,6)-(42,42). No useful exact Lucide match; use a semicircular lowercase bowl and retain the height contrast and long underline."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c0452867-4df0-44b3-9d49-f75cb007f9ca'
SOURCE_PATH = 'pictographic-primitives/symbol/lu (text u)_c0452867-4df0-44b3-9d49-f75cb007f9ca.svg'
AUTHOR = 'gpt-6'


class LuLettersUnderlined(Solo48):
    icon_id = 'lu-letters-underlined'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('lu', 'letters', 'text', 'underline', 'typography', 'abbreviation', 'language')

    def build(self) -> None:
        self.add_polyline('l',(6,6),(6,31),(18,31))
        self.add_line('u-left',(28,14),(28,24))
        self.add_arc('u-bottom',(28,24),(42,24),radius_x=7,sweep=False)
        self.add_contour('u-bowl','u-left','u-bottom')
        self.add_polyline('u-right',(42,14),(42,24),(42,31))
        self.relate('connect','u-bowl','u-right')
        self.add_line('underline',(6,42),(42,42))
