"""Cog 1 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3c5d9e7b-b736-46fd-9cd0-c46678889d84'
SOURCE_PATH = 'icons-json/interface-essential/cog 1_3c5d9e7b-b736-46fd-9cd0-c46678889d84.json'
AUTHOR = 'json_to_solo'

class Cog1InterfaceEssential(Solo48):
    icon_id = 'cog-1-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('cog', 'interface-essential')

    def build(self):
        self.add_bezier('sym-e0', (6, 24), ((6, 24.445), (6, 24.555), (6, 25)))
        self.add_bezier('sym-e1', (6, 25), ((6, 26.563), (6.92, 26.575), (8, 27)))
        self.add_bezier('sym-e2', (8, 27), ((8.867, 27.344), (10.607, 28.141), (11, 29)))
        self.add_bezier('sym-e3', (11, 29), ((12.235, 31.667), (8.871, 32.987), (10, 35)))
        self.add_bezier('sym-e4', (10, 35), ((10.466, 35.826), (11.985, 38), (13, 38)))
        self.add_bezier('sym-e5', (13, 38), ((13.687, 38), (14.435, 37.311), (15, 37)))
        self.add_bezier('sym-e6', (15, 37), ((16.129, 36.378), (17.912, 36.337), (19, 37)))
        self.add_bezier('sym-e7', (19, 37), ((21.495, 38.522), (19.285, 42), (23, 42)))
        self.add_bezier('sym-e8', (23, 42), ((23.176, 42), (23.827, 41.998), (24, 42)))
        self.add_bezier('sym-e9', (24, 42), ((24.173, 41.998), (24.824, 42), (25, 42)))
        self.add_bezier('sym-e10', (25, 42), ((28.715, 42), (26.505, 38.522), (29, 37)))
        self.add_bezier('sym-e11', (29, 37), ((30.088, 36.337), (31.871, 36.378), (33, 37)))
        self.add_bezier('sym-e12', (33, 37), ((33.565, 37.311), (34.313, 38), (35, 38)))
        self.add_bezier('sym-e13', (35, 38), ((36.015, 38), (37.534, 35.826), (38, 35)))
        self.add_bezier('sym-e14', (38, 35), ((39.129, 32.987), (35.765, 31.667), (37, 29)))
        self.add_bezier('sym-e15', (37, 29), ((37.393, 28.141), (39.133, 27.344), (40, 27)))
        self.add_bezier('sym-e16', (40, 27), ((41.08, 26.575), (42, 26.563), (42, 25)))
        self.add_bezier('sym-e17', (42, 25), ((42, 24.555), (42, 24.445), (42, 24)))
        self.add_bezier('sym-e18', (42, 24), ((42, 23.555), (42, 23.445), (42, 23)))
        self.add_bezier('sym-e19', (42, 23), ((42, 21.437), (41.08, 21.425), (40, 21)))
        self.add_bezier('sym-e20', (40, 21), ((39.133, 20.656), (37.393, 19.859), (37, 19)))
        self.add_bezier('sym-e21', (37, 19), ((35.765, 16.333), (39.129, 15.013), (38, 13)))
        self.add_bezier('sym-e22', (38, 13), ((37.534, 12.174), (36.015, 10), (35, 10)))
        self.add_bezier('sym-e23', (35, 10), ((34.313, 10), (33.565, 10.689), (33, 11)))
        self.add_bezier('sym-e24', (33, 11), ((31.871, 11.622), (30.088, 11.663), (29, 11)))
        self.add_bezier('sym-e25', (29, 11), ((26.505, 9.478), (28.715, 6), (25, 6)))
        self.add_bezier('sym-e26', (25, 6), ((24.824, 6), (24.173, 6.002), (24, 6)))
        self.add_bezier('sym-e27', (24, 6), ((23.827, 6.002), (23.176, 6), (23, 6)))
        self.add_bezier('sym-e28', (23, 6), ((19.285, 6), (21.495, 9.478), (19, 11)))
        self.add_bezier('sym-e29', (19, 11), ((17.912, 11.663), (16.129, 11.622), (15, 11)))
        self.add_bezier('sym-e30', (15, 11), ((14.435, 10.689), (13.687, 10), (13, 10)))
        self.add_bezier('sym-e31', (13, 10), ((11.985, 10), (10.466, 12.174), (10, 13)))
        self.add_bezier('sym-e32', (10, 13), ((8.871, 15.013), (12.235, 16.333), (11, 19)))
        self.add_bezier('sym-e33', (11, 19), ((10.607, 19.859), (8.867, 20.656), (8, 21)))
        self.add_bezier('sym-e34', (8, 21), ((6.92, 21.425), (6, 21.437), (6, 23)))
        self.add_bezier('sym-e35', (6, 23), ((6, 23.445), (6, 23.555), (6, 24)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33', 'sym-e34', 'sym-e35', closed=True)
