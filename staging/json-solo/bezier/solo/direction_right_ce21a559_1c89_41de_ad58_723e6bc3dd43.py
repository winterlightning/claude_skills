"""Direction right (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ce21a559-1c89-41de-ad58-723e6bc3dd43'
SOURCE_PATH = 'icons-json/arrows/direction right_ce21a559-1c89-41de-ad58-723e6bc3dd43.json'
AUTHOR = 'json_to_solo'

class DirectionRightArrows(Solo48):
    icon_id = 'direction-right-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('direction', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (33, 8), (44, 24))
        self.add_line('e1', (4, 24), (44, 24))
        self.add_line('e2', (33, 40), (44, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
