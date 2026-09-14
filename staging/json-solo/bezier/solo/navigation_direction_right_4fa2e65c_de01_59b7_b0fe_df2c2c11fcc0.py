"""Navigation direction right (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4fa2e65c-de01-59b7-b0fe-df2c2c11fcc0'
SOURCE_PATH = 'icons-json/interface-essential/navigation direction right_4fa2e65c-de01-59b7-b0fe-df2c2c11fcc0.json'
AUTHOR = 'json_to_solo'

class NavigationDirectionRightInterfaceEssential(Solo48):
    icon_id = 'navigation-direction-right-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'direction', 'right', 'interface-essential')

    def build(self):
        self.add_line('e0', (31, 44), (40, 33))
        self.add_line('e1', (40, 33), (21, 33))
        self.add_line('e2', (19, 4), (27, 4))
        self.add_line('e3', (31, 22), (40, 33))
        self.add_bezier('e4', (21, 33), ((20.326, 33), (19.141, 32.845), (18.476, 32.7)), ((12.589, 31.373), (8.017, 25.4), (8.017, 18.873)), ((8.017, 18.577), (8, 18.282), (8, 17.987)), ((8, 17.982), (8, 17.977), (8, 17.973)), ((8, 17.691), (8.017, 17.4), (8.017, 17.118)), ((8.017, 16.382), (8.227, 15.582), (8.387, 14.873)), ((9.28, 10.855), (11.731, 7.355), (15.116, 5.409)), ((16.042, 4.873), (16.952, 4.655), (17.928, 4.273)), ((18.097, 4.209), (18.223, 4), (18.408, 4)), ((18.585, 4), (18.823, 4), (19, 4)))
        self.add_contour('c0', 'e0', 'e1', 'e4', 'e2')
        self.add_contour('c1', 'e3')
