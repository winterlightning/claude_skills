"""Use a square keyshape with two equal perpendicular legs. User explicitly authorized the complete framed icon. Lucide construction: straight runs, mirrored chevrons, tangent equal-radius corners."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cd850060-547e-5eb4-96ec-5dd3a191fde4'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow corner bottom_cd850060-547e-5eb4-96ec-5dd3a191fde4.svg'
AUTHOR = 'gpt-6'

class ArrowCornerBottom(Solo48):
    icon_id = 'arrow-corner-bottom'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'corner', 'bottom', 'arrows')

    def build(self):
        low, high = (6, 42)
        corner = (high, high)
        self.add_line('horizontal', (low, high), corner)
        self.add_line('vertical', corner, (high, low))
        self.add_contour('corner', 'horizontal', 'vertical')
