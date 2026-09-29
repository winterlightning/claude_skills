"""A hand grips an upright claw hammer; finger wrinkles reduced to one clear grip line."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9c2e6a00-c352-4f4c-97df-5e296d00637d'
SOURCE_PATH = 'pictographic-primitives/tools/tools hammer hold_9c2e6a00-c352-4f4c-97df-5e296d00637d.svg'
AUTHOR = 'gpt-6'

class HandHoldingHammer(Solo48):
    icon_id = 'hand-holding-hammer'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools"
    categories = ("primitives", "tools")
    aliases = ()
    keywords = ('hammer', 'hand', 'holding', 'grip', 'construction', 'carpentry', 'build', 'tool')

    def build(self) -> None:


        self.add_polyline('head',(6,6),(30,6),(42,18),(30,14),(24,14),(24,24),(16,24),(16,14),(6,14),closed=True)
        self.add_polyline('thumb',(42,30),(34,30),(28,24),(16,24),(12,28),(16,32),(24,32))
        self.add_polyline('hand',(16,32),(12,36),(18,42),(32,42),(36,38),(42,38))
        self.relate('connect','head','thumb')
        self.relate('connect','thumb','hand')
