"""Play button (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b593497e-6dda-4831-9cc0-f15dcd54f48c'
SOURCE_PATH = 'icons-json/symbol/play button_b593497e-6dda-4831-9cc0-f15dcd54f48c.json'
AUTHOR = 'json_to_solo'

class PlayButtonB593497e(Solo48):
    icon_id = 'play-button-b593497e'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('play', 'button', 'symbol')

    def build(self):
        self.add_line('e0', (40, 24), (8, 4))
        self.add_line('e1', (8, 4), (8, 44))
        self.add_line('e2', (8, 44), (40, 24))
        self.add_contour('c0', 'e0', 'e1', 'e2', closed=True)
