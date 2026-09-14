"""Navigation right (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '24bc3247-3213-54c7-9085-304a4536c87a'
SOURCE_PATH = 'icons-json/interface-essential/navigation right_24bc3247-3213-54c7-9085-304a4536c87a.json'
AUTHOR = 'json_to_solo'

class NavigationRightInterfaceEssential(Solo48):
    icon_id = 'navigation-right-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'right', 'interface-essential')

    def build(self):
        self.add_line('e0', (34, 40), (44, 28))
        self.add_line('e1', (43, 25), (34, 14))
        self.add_bezier('e2', (44, 28), ((44, 27.717), (43.991, 27.114), (43.991, 26.831)), ((43.991, 26.006), (43.409, 25.455), (43, 25)))
        self.add_bezier('e3', (35, 26), ((30.527, 26.8), (25.891, 27.975), (21.373, 28.062)), ((13.609, 28.209), (7.591, 27.286), (4.945, 15.766)), ((4.6, 14.252), (4.427, 12.702), (4.227, 11.151)), ((4.173, 10.658), (4, 10.129), (4, 9.625)), ((4, 9.083), (4, 8.542), (4, 8)))
        self.add_contour('c0', 'e0', 'e2', 'e1')
        self.add_contour('c1', 'e3')
