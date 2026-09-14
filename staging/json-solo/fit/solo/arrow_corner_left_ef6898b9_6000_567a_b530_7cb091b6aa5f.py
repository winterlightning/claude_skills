"""Arrow corner left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ef6898b9-6000-567a-b530-7cb091b6aa5f'
SOURCE_PATH = 'icons-json/arrows/arrow corner left_ef6898b9-6000-567a-b530-7cb091b6aa5f.json'
AUTHOR = 'json_to_solo'

class ArrowCornerLeftEf6898b9(Solo48):
    icon_id = 'arrow-corner-left-ef6898b9'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'corner', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (40, 4), (8, 24))
        self.add_line('e1', (8, 24), (40, 44))
        self.add_contour('c0', 'e0', 'e1')
