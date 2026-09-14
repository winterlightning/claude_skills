"""Angle brackets (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7173b451-8abc-5d28-bf77-d7caa41bbb6a'
SOURCE_PATH = 'icons-json/interface-essential/angle brackets_7173b451-8abc-5d28-bf77-d7caa41bbb6a.json'
AUTHOR = 'json_to_solo'

class AngleBracketsInterfaceEssential(Solo48):
    icon_id = 'angle-brackets-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('angle', 'brackets', 'interface-essential')

    def build(self):
        self.add_line('e0', (18, 8), (4, 24))
        self.add_line('e1', (4, 24), (18, 40))
        self.add_line('e2', (30, 8), (44, 24))
        self.add_line('e3', (44, 24), (31, 40))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3')
