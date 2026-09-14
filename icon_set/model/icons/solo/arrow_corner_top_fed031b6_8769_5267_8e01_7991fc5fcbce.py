"""Arrow corner top (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fed031b6-8769-5267-8e01-7991fc5fcbce'
SOURCE_PATH = 'icons-json/arrows/arrow corner top_fed031b6-8769-5267-8e01-7991fc5fcbce.json'
AUTHOR = 'json_to_solo'

class ArrowCornerTop(Solo48):
    icon_id = 'arrow-corner-top'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'corner', 'top', 'arrows')

    def build(self):
        self.add_line('e0', (44, 8), (4, 8))
        self.add_line('e1', (4, 8), (4, 40))
        self.add_contour('c0', 'e0', 'e1')
