"""Architecture fence (building), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd123c4cf-199d-51d0-90b0-8f81734338b8'
SOURCE_PATH = 'icons-json/building/architecture fence_d123c4cf-199d-51d0-90b0-8f81734338b8.json'
AUTHOR = 'json_to_solo'

class ArchitectureFenceBuilding(Solo48):
    icon_id = 'architecture-fence-building'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('architecture', 'fence', 'building')

    def build(self):
        self.add_line('e0', (30, 18), (18, 18))
        self.add_line('e1', (30, 32), (18, 32))
        self.add_line('e2', (4, 19), (8, 19))
        self.add_line('e3', (4, 32), (8, 32))
        self.add_line('e4', (40, 32), (44, 32))
        self.add_line('e5', (40, 19), (44, 19))
        self.add_line('e6', (37, 40), (32, 40))
        self.add_line('e7', (30, 38), (30, 13))
        self.add_line('e8', (40, 14), (40, 38))
        self.add_line('e9', (18, 14), (18, 38))
        self.add_line('e10', (17, 40), (9, 40))
        self.add_line('e11', (8, 38), (8, 14))
        self.add_line('e12', (32, 40), (30, 38))
        self.add_arc('e13-1', (30, 13), (36, 9), radius_x=7)
        self.add_arc('e13-2', (36, 9), (40, 14), radius_x=13)
        self.add_arc('e14-1', (40, 38), (39, 40), radius_x=2)
        self.add_line('e14-2', (39, 40), (37, 40))
        self.add_line('e15', (18, 38), (17, 40))
        self.add_arc('e16', (9, 40), (8, 38), radius_x=2)
        self.add_arc('e17-1', (8, 14), (13, 8), radius_x=19)
        self.add_line('e17-2', (13, 8), (18, 14))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6', 'e12', 'e7', 'e13-1', 'e13-2', 'e8', 'e14-1', 'e14-2', closed=True)
        self.add_contour('c7', 'e9', 'e15', 'e10', 'e16', 'e11', 'e17-1', 'e17-2', closed=True)
        self.relate('connect', 'c0', 'c6')
        self.relate('connect', 'c0', 'c7')
        self.relate('connect', 'c1', 'c6')
        self.relate('connect', 'c1', 'c7')
        self.relate('connect', 'c2', 'c7')
        self.relate('connect', 'c3', 'c7')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c6')
