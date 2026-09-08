"""Round monocle and long U cord. SQUARE (2,2)-(46,46) balances lens and cord. Lens highlight omitted for negative space. Deliberately asymmetric as in source. Lucide glasses informed the circular lens."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6de5f671-ed10-481b-aa2c-27ba2fe17d98'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-04/glasses monocle_6de5f671-ed10-481b-aa2c-27ba2fe17d98.svg'
AUTHOR = 'astra-chatgpt'


class MonocleWithCord(Solo48):
    icon_id = 'monocle-with-cord'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('monocle', 'glasses', 'lens', 'eyeglass', 'cord', 'vintage', 'eyewear', 'accessory')

    def build(self) -> None:
        self.add_arc('lens-right', (16, 2), (30, 16), radius_x=14)
        self.add_arc('lens-lower', (30, 16), (16, 30), radius_x=14)
        self.add_arc('lens-left', (16, 30), (16, 2), radius_x=14, radius_y=14, sweep=True, large_arc=False)
        self.add_contour('lens', 'lens-right', 'lens-lower', 'lens-left', closed=True)
        self.add_line('cord-down', (30, 16), (30, 38))
        self.add_arc('cord-bottom', (30, 38), (46, 38), radius_x=8, radius_y=8, sweep=False, large_arc=False)
        self.add_line('cord-up', (46, 38), (46, 22))
        self.add_contour('cord', 'cord-down', 'cord-bottom', 'cord-up', closed=False)
        self.relate("connect", 'lens', 'cord')
