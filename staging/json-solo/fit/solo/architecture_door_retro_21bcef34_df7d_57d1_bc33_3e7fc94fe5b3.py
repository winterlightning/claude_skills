"""Architecture door retro (building), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '21bcef34-df7d-57d1-bc33-3e7fc94fe5b3'
SOURCE_PATH = 'icons-json/building/architecture door retro_21bcef34-df7d-57d1-bc33-3e7fc94fe5b3.json'
AUTHOR = 'json_to_solo'

class ArchitectureDoorRetroBuilding(Solo48):
    icon_id = 'architecture-door-retro-building'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('architecture', 'door', 'retro', 'building')

    def build(self):
        self.add_line('e0', (36, 44), (36, 16))
        self.add_line('e1', (12, 17), (12, 44))
        self.add_line('e2', (40, 44), (8, 44))
        self.add_line('e3', (28, 29), (28, 26))
        self.add_arc('e4-1', (36, 16), (24, 4), radius_x=12, sweep=False)
        self.add_arc('e4-2', (24, 4), (12, 17), radius_x=13, sweep=False)
        self.add_contour('c0', 'e0', 'e4-1', 'e4-2', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
