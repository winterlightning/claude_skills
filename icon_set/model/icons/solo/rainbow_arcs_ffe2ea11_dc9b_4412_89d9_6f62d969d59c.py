"""Three concentric semicircles. Lucide rainbow: shared centre and repeated radial spacing. Radial keyshape preserves true semicircles without stretching.

SOLO48 CIRCLE, live visible envelope (2, 2, 46, 46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ffe2ea11-dc9b-4412-89d9-6f62d969d59c'
SOURCE_PATH = 'pictographic-primitives/symbol/rainbow_ffe2ea11-dc9b-4412-89d9-6f62d969d59c.svg'
AUTHOR = 'gpt-6'


class RainbowArcs(Solo48):
    icon_id = 'rainbow-arcs'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol", "state")
    aliases = ()
    keywords = ('rainbow', 'arcs', 'weather', 'colors', 'pride', 'hope', 'sky', 'spectrum')

    def build(self) -> None:

        for index,radius in enumerate((20,11,2)):
            self.add_arc('rainbow-'+str(index),(24-radius,24),(24+radius,24),radius_x=radius)
