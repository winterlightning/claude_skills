"""Capital M and lowercase d above an underline. SQUARE centerline extremes (6,6)-(42,42). Lucide case-sensitive informs mixed-case proportions and a round lowercase bowl. Straighten the M outer stems to keep the two letters separated; preserve pointed peaks, tall d ascender and underline."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8f859757-d9ba-4d92-8889-0e22b2a1aeb2'
SOURCE_PATH = 'pictographic-primitives/symbol/md (text u)_8f859757-d9ba-4d92-8889-0e22b2a1aeb2.svg'
AUTHOR = 'gpt-6'


class MdLettersUnderlined(Solo48):
    icon_id = 'md-letters-underlined'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('md', 'letters', 'markdown', 'text', 'underline', 'typography', 'abbreviation')

    def build(self) -> None:
        self.add_polyline('m',(6,32),(6,6),(14,20),(22,6),(22,32))
        self.add_arc('d-upper',(32,24),(42,24),radius_x=5,radius_y=7)
        self.add_arc('d-lower',(42,24),(32,24),radius_x=5,radius_y=7)
        self.add_contour('d-bowl','d-upper','d-lower',closed=True)
        self.add_polyline('d-stem',(42,6),(42,24),(42,31))
        self.relate('connect','d-bowl','d-stem')
        self.add_line('underline',(6,42),(42,42))
