"""Left-pointing arrow. Lucide arrow-left: one open chevron and connected shaft; no omissions.

SOLO48 HRECT_L, live visible envelope (2, 6, 46, 42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6e524b3f-7b92-47ac-8db1-6f2da73b9fd5'
SOURCE_PATH = 'pictographic-primitives/symbol/return arrow with line_6e524b3f-7b92-47ac-8db1-6f2da73b9fd5.svg'
AUTHOR = 'gpt-6'


class ArrowLeftSolo(Solo48):
    icon_id = 'arrow-left-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('arrow', 'left', 'back', 'previous', 'return', 'direction', 'navigation', 'west')

    def build(self) -> None:

        self.add_polyline('head',(20,8),(4,24),(20,40))
        self.add_line('shaft',(4,24),(44,24))
        self.relate('connect','head','shaft')
