"""An upright hammer with a broad striking face and down-curving claw; the long handle is unadorned."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4b20247a-adb8-5899-a5a8-311cf63d5873'
SOURCE_PATH = 'pictographic-primitives/tools/tools hammer_4b20247a-adb8-5899-a5a8-311cf63d5873.svg'
AUTHOR = 'gpt-6'

class UprightClawHammer(Solo48):
    icon_id = 'upright-claw-hammer'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools"
    categories = ("primitives", "tools")
    aliases = ()
    keywords = ('hammer', 'claw hammer', 'carpentry', 'construction', 'nail', 'build', 'hardware', 'tool')

    def build(self) -> None:


        self.add_polyline('head',(6,6),(26,6),(34,10))
        self.add_arc('claw',(34,10),(42,24),radius_x=22)
        self.add_polyline('claw-inner',(42,24),(30,16),(26,16))
        self.add_polyline('handle',(26,16),(26,42),(16,42),(16,16),(6,16),(6,6))
        self.relate('connect','head','claw')
        self.relate('connect','claw','claw-inner')
        self.relate('connect','claw-inner','handle')
        self.relate('connect','handle','head')
