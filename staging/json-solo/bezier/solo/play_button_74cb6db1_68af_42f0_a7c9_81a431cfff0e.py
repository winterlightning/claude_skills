"""Play button (state), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '74cb6db1-68af-42f0-a7c9-81a431cfff0e'
SOURCE_PATH = 'icons-json/state/play button_74cb6db1-68af-42f0-a7c9-81a431cfff0e.json'
AUTHOR = 'json_to_solo'

class PlayButtonState(Solo48):
    icon_id = 'play-button-state'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('play', 'button', 'state')

    def build(self):
        self.add_line('e0', (40, 24), (8, 4))
        self.add_line('e1', (8, 4), (8, 44))
        self.add_line('e2', (8, 44), (40, 24))
        self.add_contour('c0', 'e0', 'e1', 'e2', closed=True)
