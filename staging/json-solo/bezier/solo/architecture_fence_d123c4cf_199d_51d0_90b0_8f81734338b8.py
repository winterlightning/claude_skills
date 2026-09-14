"""Architecture fence (building), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e12', (32, 40), ((30.591, 39.545), (30.473, 39.331), (30, 38)))
        self.add_bezier('e13', (30, 13), ((30.536, 12.242), (33.945, 9.011), (34.8, 8.674)), ((35.055, 8.573), (35.527, 8.497), (35.8, 8.556)), ((36.018, 8.598), (38.245, 10.998), (38.536, 11.293)), ((39.227, 12.008), (40, 12.939), (40, 14)))
        self.add_bezier('e14', (40, 38), ((40, 39.659), (39, 39.983), (37.636, 39.983)), ((37.336, 39.983), (37.3, 40), (37, 40)))
        self.add_bezier('e15', (18, 38), ((18, 38.556), (17.7, 39.335), (17.209, 39.764)), ((17.064, 39.882), (17.145, 39.891), (17, 40)))
        self.add_bezier('e16', (9, 40), ((8.836, 39.949), (9.1, 39.975), (8.927, 39.924)), ((8.064, 39.672), (8.273, 38.682), (8, 38)))
        self.add_bezier('e17', (8, 14), ((8, 12.796), (10.464, 10.425), (11.282, 9.524)), ((11.409, 9.373), (12.618, 8), (12.745, 8)), ((12.746, 8), (12.748, 8), (12.749, 8)), ((12.846, 8), (13.993, 9.358), (14.109, 9.482)), ((14.991, 10.509), (18, 12.661), (18, 14)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6', 'e12', 'e7', 'e13', 'e8', 'e14', closed=True)
        self.add_contour('c7', 'e9', 'e15', 'e10', 'e16', 'e11', 'e17', closed=True)
        self.relate('connect', 'c0', 'c6')
        self.relate('connect', 'c0', 'c7')
        self.relate('connect', 'c1', 'c6')
        self.relate('connect', 'c1', 'c7')
        self.relate('connect', 'c2', 'c7')
        self.relate('connect', 'c3', 'c7')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c6')
