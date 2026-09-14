"""Arrow thick corner 2 top right (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7c10af49-a37e-5db5-8381-50dc08c0925d'
SOURCE_PATH = 'icons-json/arrows/arrow thick corner 2 top right_7c10af49-a37e-5db5-8381-50dc08c0925d.json'
AUTHOR = 'json_to_solo'

class ArrowThickCorner2TopRight(Solo48):
    icon_id = 'arrow-thick-corner-2-top-right'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'corner', 'top', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (6, 42), (42, 6))
        self.add_line('e1', (42, 6), (42, 42))
        self.add_line('e2', (42, 6), (6, 6))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
