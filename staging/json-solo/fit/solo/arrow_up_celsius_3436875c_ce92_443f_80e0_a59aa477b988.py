"""Arrow up celsius (state), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3436875c-ce92-443f-80e0-a59aa477b988'
SOURCE_PATH = 'icons-json/state/arrow up celsius_3436875c-ce92-443f-80e0-a59aa477b988.json'
AUTHOR = 'json_to_solo'

class ArrowUpCelsiusState(Solo48):
    icon_id = 'arrow-up-celsius-state'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('arrow', 'up', 'celsius', 'state')

    def build(self):
        self.add_line('e0', (8, 17), (24, 4))
        self.add_line('e1', (24, 44), (24, 4))
        self.add_line('e2', (39, 17), (24, 4))
        self.add_line('e3', (24, 4), (40, 4))
        self.add_line('e4', (24, 4), (8, 4))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3')
        self.add_contour('c3', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
