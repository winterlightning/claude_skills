"""Capital N and lowercase p above an underline. SQUARE extremes (6,6)-(42,42). Lucide case-sensitive informs mixed-case proportion and round lowercase bowl. Raise the letter baseline so the p descender remains above a clear underline gap."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd87e130a-25da-498e-924b-ceb9d5c0a211'
SOURCE_PATH = 'pictographic-primitives/symbol/np (text u)_d87e130a-25da-498e-924b-ceb9d5c0a211.svg'
AUTHOR = 'gpt-6'


class NpLettersUnderlined(Solo48):
    icon_id = 'np-letters-underlined'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('np', 'letters', 'text', 'underline', 'typography', 'abbreviation', 'language')

    def build(self) -> None:
        self.add_polyline('n',(6,27),(6,6),(22,27),(22,6))
        self.add_arc('p-upper',(32,20),(42,20),radius_x=5,radius_y=7)
        self.add_arc('p-lower',(42,20),(32,20),radius_x=5,radius_y=7)
        self.add_contour('p-bowl','p-upper','p-lower',closed=True)
        self.add_polyline('p-stem',(32,13),(32,20),(32,32))
        self.relate('connect','p-bowl','p-stem')
        self.add_line('underline',(6,42),(42,42))
