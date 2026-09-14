"""Architecture door retro (building), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e4', (36, 16), ((36, 15.409), (35.571, 14.509), (35.444, 13.927)), ((34.375, 9.1), (30.577, 5.145), (26.038, 4.245)), ((25.541, 4.145), (24.994, 4), (24.488, 4)), ((24.485, 4), (24.482, 4), (24.479, 4)), ((24.289, 4), (24.098, 4.018), (23.916, 4.018)), ((18.754, 4.018), (14.585, 8.055), (12.943, 13.145)), ((12.598, 14.236), (12, 15.836), (12, 17)))
        self.add_contour('c0', 'e0', 'e4', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
