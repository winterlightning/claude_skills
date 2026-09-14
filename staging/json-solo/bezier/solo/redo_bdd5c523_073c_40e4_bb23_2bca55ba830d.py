"""Redo (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bdd5c523-073c-40e4-bb23-2bca55ba830d'
SOURCE_PATH = 'icons-json/interface-essential/redo_bdd5c523-073c-40e4-bb23-2bca55ba830d.json'
AUTHOR = 'json_to_solo'

class RedoInterfaceEssential(Solo48):
    icon_id = 'redo-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('redo', 'interface-essential')

    def build(self):
        self.add_line('e0', (40, 4), (40, 12))
        self.add_line('e1', (32, 14), (40, 14))
        self.add_bezier('e2', (40, 12), ((40, 12.609), (40, 13.391), (40, 14)))
        self.add_bezier('e3', (25, 44), ((24.865, 44), (24.564, 43.991), (24.429, 43.991)), ((22.745, 43.991), (21.002, 43.473), (19.436, 42.836)), ((12.994, 40.218), (8.017, 33.345), (8.017, 25.764)), ((8.017, 25.629), (8, 25.504), (8, 25.37)), ((8, 25.368), (8, 25.366), (8, 25.364)), ((8, 24.936), (8.017, 24.509), (8.017, 24.082)), ((8.017, 22.109), (8.455, 20.082), (9.053, 18.227)), ((11.747, 9.873), (19.655, 4.845), (27.705, 6.045)), ((33.112, 6.855), (36.455, 9.773), (40, 14)))
        self.add_contour('c0', 'e0', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e1')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
