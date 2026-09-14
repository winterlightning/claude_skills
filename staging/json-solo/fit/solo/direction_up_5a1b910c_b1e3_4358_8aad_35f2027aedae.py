"""Direction up (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5a1b910c-b1e3-4358-8aad-35f2027aedae'
SOURCE_PATH = 'icons-json/arrows/direction up_5a1b910c-b1e3-4358-8aad-35f2027aedae.json'
AUTHOR = 'json_to_solo'

class DirectionUpArrows(Solo48):
    icon_id = 'direction-up-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('direction', 'up', 'arrows')

    def build(self):
        self.add_line('e0', (8, 16), (24, 4))
        self.add_line('e1', (24, 44), (24, 4))
        self.add_line('e2', (40, 16), (24, 4))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
