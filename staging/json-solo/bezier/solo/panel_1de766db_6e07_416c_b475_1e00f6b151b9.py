"""Panel (state), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1de766db-6e07-416c-b475-1e00f6b151b9'
SOURCE_PATH = 'icons-json/state/panel_1de766db-6e07-416c-b475-1e00f6b151b9.json'
AUTHOR = 'json_to_solo'

class PanelState(Solo48):
    icon_id = 'panel-state'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('panel', 'state')

    def build(self):
        self.add_line('e0', (23, 8), (34, 8))
        self.add_line('e1', (35, 9), (39, 18))
        self.add_line('e2', (23, 8), (14, 8))
        self.add_line('e3', (13, 9), (9, 18))
        self.add_line('e4', (23, 8), (23, 28))
        self.add_line('e5', (23, 28), (5, 28))
        self.add_line('e6', (4, 27), (9, 18))
        self.add_line('e7', (39, 18), (44, 27))
        self.add_line('e8', (43, 28), (23, 28))
        self.add_line('e9', (23, 28), (23, 40))
        self.add_line('e10', (39, 18), (9, 18))
        self.add_bezier('e11', (34, 8), ((34.1, 8.02), (34.209, 8.05), (34.309, 8.07)), ((34.745, 8.24), (34.773, 8.65), (35, 9)))
        self.add_bezier('e12', (14, 8), ((13.891, 8.02), (13.791, 8.05), (13.682, 8.07)), ((13.236, 8.24), (13.227, 8.64), (13, 9)))
        self.add_bezier('e13', (5, 28), ((4.682, 27.84), (4, 28.06), (4, 27.3)), ((4, 27.2), (4, 27.1), (4, 27)))
        self.add_bezier('e14', (44, 27), ((44, 27.1), (44, 27.2), (44, 27.3)), ((44, 28.08), (43.318, 27.83), (43, 28)))
        self.add_contour('c0', 'e0', 'e11', 'e1')
        self.add_contour('c1', 'e2', 'e12', 'e3')
        self.add_contour('c2', 'e4', 'e5', 'e13', 'e6')
        self.add_contour('c3', 'e7', 'e14', 'e8', 'e9')
        self.add_contour('c4', 'e10')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c3')
