"""Direction button arrows (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '94d393c7-21fe-408e-8b1c-2e805481cd08'
SOURCE_PATH = 'icons-json/interface-essential/direction button arrows_94d393c7-21fe-408e-8b1c-2e805481cd08.json'
AUTHOR = 'json_to_solo'

class DirectionButtonArrowsInterfaceEssential(Solo48):
    icon_id = 'direction-button-arrows-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('direction', 'button', 'arrows', 'interface-essential')

    def build(self):
        self.add_line('e0', (19, 11), (24, 6))
        self.add_line('e1', (11, 19), (6, 24))
        self.add_line('e2', (11, 29), (6, 24))
        self.add_line('e3', (19, 37), (24, 42))
        self.add_line('e4', (29, 37), (24, 42))
        self.add_line('e5', (37, 29), (42, 24))
        self.add_line('e6', (37, 19), (42, 24))
        self.add_line('e7', (29, 11), (24, 6))
        self.add_line('e8', (24, 42), (24, 24))
        self.add_line('e9', (24, 6), (24, 24))
        self.add_line('e10', (24, 24), (42, 24))
        self.add_line('e11', (24, 24), (6, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6')
        self.add_contour('c7', 'e7')
        self.add_contour('c8', 'e8')
        self.add_contour('c9', 'e9')
        self.add_contour('c10', 'e10')
        self.add_contour('c11', 'e11')
        self.relate('connect', 'c0', 'c7')
        self.relate('connect', 'c0', 'c9')
        self.relate('connect', 'c7', 'c9')
        self.relate('connect', 'c1', 'c11')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c11', 'c2')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c8')
        self.relate('connect', 'c4', 'c8')
        self.relate('connect', 'c10', 'c5')
        self.relate('connect', 'c10', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c10', 'c11')
        self.relate('connect', 'c10', 'c8')
        self.relate('connect', 'c10', 'c9')
        self.relate('connect', 'c11', 'c8')
        self.relate('connect', 'c11', 'c9')
        self.relate('connect', 'c8', 'c9')
