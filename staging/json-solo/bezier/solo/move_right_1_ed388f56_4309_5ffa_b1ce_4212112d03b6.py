"""Move right 1 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ed388f56-4309-5ffa-b1ce-4212112d03b6'
SOURCE_PATH = 'icons-json/interface-essential/move right 1_ed388f56-4309-5ffa-b1ce-4212112d03b6.json'
AUTHOR = 'json_to_solo'

class MoveRight1Ed388f56(Solo48):
    icon_id = 'move-right-1-ed388f56'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('move', 'right', 'interface-essential')

    def build(self):
        self.add_line('e0', (44, 8), (44, 40))
        self.add_line('e1', (22, 34), (33, 24))
        self.add_line('e2', (33, 24), (4, 24))
        self.add_line('e3', (33, 24), (22, 14))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.add_contour('c2', 'e3')
