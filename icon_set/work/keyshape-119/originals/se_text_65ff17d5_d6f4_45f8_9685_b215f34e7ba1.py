"""Capital S and E. Lucide type and strikethrough inform monoline terminals and coherent curves. E middle arm shortened as in the source.

SOLO48 HRECT_L; live visible envelope (2, 6, 46, 42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '65ff17d5-d6f4-45f8-9685-b215f34e7ba1'
SOURCE_PATH = 'pictographic-primitives/symbol/se (text)_65ff17d5-d6f4-45f8-9685-b215f34e7ba1.svg'
AUTHOR = 'gpt-6'


class SeText(Solo48):
    icon_id = 'se-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('se', 'letters', 'text', 'abbreviation', 'typography', 'label', 'language')

    def build(self) -> None:

        self.add_arc('s-crown',(18,16),(6,16),radius_x=7,radius_y=8,sweep=False)
        self.add_arc('s-upper-turn',(6,16),(11,24),radius_x=7,radius_y=8,sweep=False)
        self.add_arc('s-lower-turn',(11,24),(18,32),radius_x=7,radius_y=8)
        self.add_arc('s-base',(18,32),(6,32),radius_x=7,radius_y=8)
        self.add_contour('s','s-crown','s-upper-turn','s-lower-turn','s-base')
        self.add_polyline('e-outline',(42,8),(28,8),(28,24),(28,40),(42,40))
        self.add_line('e-middle',(28,24),(40,24))
        self.relate('connect','e-outline','e-middle')
