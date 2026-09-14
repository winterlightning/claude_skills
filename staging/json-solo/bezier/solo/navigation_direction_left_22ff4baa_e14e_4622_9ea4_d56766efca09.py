"""Navigation direction left (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '22ff4baa-e14e-4622-9ea4-d56766efca09'
SOURCE_PATH = 'icons-json/interface-essential/navigation direction left_22ff4baa-e14e-4622-9ea4-d56766efca09.json'
AUTHOR = 'json_to_solo'

class NavigationDirectionLeft22ff4baa(Solo48):
    icon_id = 'navigation-direction-left-22ff4baa'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'direction', 'left', 'interface-essential')

    def build(self):
        self.add_line('e0', (16, 8), (4, 20))
        self.add_line('e1', (15, 31), (4, 20))
        self.add_line('e2', (4, 20), (37, 20))
        self.add_line('e3', (44, 28), (44, 40))
        self.add_bezier('e4', (37, 20), ((41.509, 20), (43.982, 23.731), (43.982, 27.613)), ((43.982, 27.806), (44, 27.798), (44, 28)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e4', 'e3')
