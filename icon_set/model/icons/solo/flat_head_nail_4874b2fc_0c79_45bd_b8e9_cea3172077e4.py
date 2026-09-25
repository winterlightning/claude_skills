"""A diagonal nail with flat crosswise head and pointed shank; head kept as a clear rectangular bar."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4874b2fc-0c79-45bd-b8e9-cea3172077e4'
SOURCE_PATH = 'pictographic-primitives/tools/hardware nail_4874b2fc-0c79-45bd-b8e9-cea3172077e4.svg'
AUTHOR = 'gpt-6'

class FlatHeadNail(Solo48):
    icon_id = 'flat-head-nail'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools"
    aliases = ()
    keywords = ('nail', 'flat head', 'hardware', 'fastener', 'spike', 'construction', 'carpentry', 'metal')

    def build(self) -> None:
        self.add_polyline('head',(26,6),(42,22),(36,28),(20,12),closed=True)
        self.add_polyline('shank',(24,16),(8,32),(6,42),(16,40),(32,24))
        self.relate('connect','shank','head')
