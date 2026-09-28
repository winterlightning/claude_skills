"""Two diagonal chain links joined at the center. SQUARE extremes (6,6)-(42,42). Lucide link-2 informs open rounded links with a separate joining stroke; preserve the source diagonal orientation and opposed bows."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a1310a44-a79e-47db-836c-4e40111ae679'
SOURCE_PATH = 'pictographic-primitives/symbol/link_a1310a44-a79e-47db-836c-4e40111ae679.svg'
AUTHOR = 'gpt-6'


class LinkInterlocking(Solo48):
    icon_id = 'link-interlocking'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol", "state")
    aliases = ()
    keywords = ('link', 'chain', 'url', 'hyperlink', 'connect', 'join', 'web', 'attachment')

    def build(self) -> None:
        self.add_line('upper-tail',(20,14),(24,10))
        self.add_arc('upper-bow',(24,10),(40,22),radius_x=10)
        self.add_contour('upper','upper-tail','upper-bow')
        self.add_line('lower-tail',(12,22),(8,26))
        self.add_arc('lower-bow',(8,26),(24,38),radius_x=10,sweep=False)
        self.add_contour('lower','lower-tail','lower-bow')
        self.add_line('join',(18,30),(30,18))
