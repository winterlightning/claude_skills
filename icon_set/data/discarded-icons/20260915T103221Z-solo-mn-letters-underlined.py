"""Capital M and lowercase n above an underline. SQUARE extremes (6,6)-(42,42). Lucide case-sensitive informs mixed-case proportion; straighten M outer stems to allow separated letters. Preserve the rounded n arch and underline."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '29d5f990-d45a-4a45-b57d-009d40fb1d94'
SOURCE_PATH = 'pictographic-primitives/symbol/mn (text u)_29d5f990-d45a-4a45-b57d-009d40fb1d94.svg'
AUTHOR = 'gpt-6'


class MnLettersUnderlined(Solo48):
    icon_id = 'mn-letters-underlined'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('mn', 'letters', 'text', 'underline', 'typography', 'abbreviation', 'language')

    def build(self) -> None:
        self.add_polyline('m',(6,32),(6,6),(14,20),(22,6),(22,32))
        self.add_polyline('n-stem',(32,14),(32,22),(32,32))
        self.add_arc('n-arch',(32,22),(42,22),radius_x=5,radius_y=7)
        self.add_line('n-right',(42,22),(42,32))
        self.add_contour('n-round','n-arch','n-right')
        self.relate('connect','n-stem','n-round')
        self.add_line('underline',(6,42),(42,42))
