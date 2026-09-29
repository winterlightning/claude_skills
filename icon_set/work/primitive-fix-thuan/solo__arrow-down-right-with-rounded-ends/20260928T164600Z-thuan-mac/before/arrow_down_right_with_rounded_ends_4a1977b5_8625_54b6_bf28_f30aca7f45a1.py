"""Arrow Down Right with Rounded Ends.

Plan: SQUARE centerlines (6,6)-(42,42); continuous broad diagonal arrow with matching rounded arm ends and deliberate inner corners. The shaft uses a 4:3 direction and a radius-5 semicircular cap with exactly matching tangents.
Construction references: Lucide move-down-left: unified shaft/head direction; source supplies the thick outline.
Reduction: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4a1977b5-8625-54b6-bf28-f30aca7f45a1'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow thick corner bottom right_4a1977b5-8625-54b6-bf28-f30aca7f45a1.svg'
SOURCE_ICON_IDS = ('4a1977b5-8625-54b6-bf28-f30aca7f45a1',)
SOURCE_PATHS = ('pictographic-primitives/arrows/arrow thick corner bottom right_4a1977b5-8625-54b6-bf28-f30aca7f45a1.svg',)
AUTHOR = 'gpt-6'


class ArrowDownRightWithRoundedEnds(Solo48):
    icon_id = 'arrow-down-right-with-rounded-ends'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('arrow', 'down', 'right', 'with', 'rounded', 'ends')

    def build(self) -> None:
        self.add_line("arrow-1",(8,16),(32,34))
        self.add_line("arrow-2",(32,34),(10,34))
        self.add_arc("bottom-cap",(10,34),(10,42),radius_x=4,sweep=False)
        self.add_line("base",(10,42),(38,42))
        self.add_arc("corner",(38,42),(42,38),radius_x=4,sweep=False)
        self.add_line("right",(42,38),(42,10))
        self.add_arc("top-cap",(42,10),(34,10),radius_x=4,sweep=False)
        self.add_line("return-1",(34,10),(34,23))
        self.add_line("return-2",(34,23),(14,8))
        self.add_arc("shaft-cap",(14,8),(8,16),radius_x=5,sweep=False)
        self.add_contour("outline","arrow-1","arrow-2","bottom-cap","base","corner","right","top-cap","return-1","return-2","shaft-cap",closed=True)
