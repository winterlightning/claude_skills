"""Single capital S in one tangent-continuous contour. Lucide strikethrough informs coherent curved letter construction, excluding its unrelated strike bar.

SOLO48 VRECT_L; live visible envelope (6, 2, 42, 46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e6159229-6c64-41b4-ba85-0806880f179d'
SOURCE_PATH = 'pictographic-primitives/symbol/s (text)_e6159229-6c64-41b4-ba85-0806880f179d.svg'
AUTHOR = 'gpt-6'


class LetterS(Solo48):
    icon_id = 'letter-s'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('s', 'letter', 'alphabet', 'text', 'character', 'typography', 'initial')

    def build(self) -> None:

        self.add_arc('crown',(40,14),(8,14),radius_x=16,radius_y=10,sweep=False)
        self.add_arc('upper-turn',(8,14),(24,24),radius_x=16,radius_y=10,sweep=False)
        self.add_arc('lower-turn',(24,24),(40,34),radius_x=16,radius_y=10)
        self.add_arc('base',(40,34),(8,34),radius_x=16,radius_y=10)
        self.add_contour('letter','crown','upper-turn','lower-turn','base')
