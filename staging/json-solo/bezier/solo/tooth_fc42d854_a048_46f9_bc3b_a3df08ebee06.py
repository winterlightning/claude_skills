"""Tooth (health), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fc42d854-a048-46f9-bc3b-a3df08ebee06'
SOURCE_PATH = 'icons-json/health/tooth_fc42d854-a048-46f9-bc3b-a3df08ebee06.json'
AUTHOR = 'json_to_solo'

class Tooth(Solo48):
    icon_id = 'tooth'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('tooth', 'health')

    def build(self):
        self.add_line('sym-e0', (18, 37), (16, 42))
        self.add_bezier('sym-e1', (16, 42), ((15.486, 42.755), (14.994, 44), (14, 44)))
        self.add_bezier('sym-e2', (14, 44), ((12.804, 44), (11.514, 43.027), (11, 42)))
        self.add_bezier('sym-e3', (11, 42), ((9.838, 39.664), (10.52, 34.582), (11, 32)))
        self.add_line('sym-e4', (11, 32), (11, 28))
        self.add_bezier('sym-e5', (11, 28), ((11.472, 25.464), (9.876, 22.218), (9, 20)))
        self.add_bezier('sym-e6', (9, 20), ((8.377, 18.436), (8, 16.709), (8, 15)))
        self.add_bezier('sym-e7', (8, 15), ((8, 14.782), (8, 14.209), (8, 14)))
        self.add_bezier('sym-e8', (8, 14), ((8, 13.709), (8, 13.282), (8, 13)))
        self.add_bezier('sym-e9', (8, 13), ((8, 8.036), (11.335, 4), (16, 4)))
        self.add_bezier('sym-e10', (16, 4), ((18.686, 4), (21.331, 6.036), (24, 6)))
        self.add_bezier('sym-e11', (24, 6), ((24.042, 5.999), (23.958, 6), (24, 6)))
        self.add_bezier('sym-e12', (24, 6), ((24.042, 6), (23.958, 5.999), (24, 6)))
        self.add_bezier('sym-e13', (24, 6), ((26.669, 6.036), (29.314, 4), (32, 4)))
        self.add_bezier('sym-e14', (32, 4), ((36.665, 4), (40, 8.036), (40, 13)))
        self.add_bezier('sym-e15', (40, 13), ((40, 13.282), (40, 13.709), (40, 14)))
        self.add_bezier('sym-e16', (40, 14), ((40, 14.209), (40, 14.782), (40, 15)))
        self.add_bezier('sym-e17', (40, 15), ((40, 16.709), (39.623, 18.436), (39, 20)))
        self.add_bezier('sym-e18', (39, 20), ((38.124, 22.218), (36.528, 25.464), (37, 28)))
        self.add_line('sym-e19', (37, 28), (37, 32))
        self.add_bezier('sym-e20', (37, 32), ((37.48, 34.582), (38.162, 39.664), (37, 42)))
        self.add_bezier('sym-e21', (37, 42), ((36.486, 43.027), (35.196, 44), (34, 44)))
        self.add_bezier('sym-e22', (34, 44), ((33.006, 44), (32.514, 42.755), (32, 42)))
        self.add_line('sym-e23', (32, 42), (30, 37))
        self.add_bezier('sym-e24', (30, 37), ((29.604, 35.718), (28.775, 34.073), (28, 33)))
        self.add_bezier('sym-e25', (28, 33), ((26.921, 31.52), (25.593, 31), (24, 31)))
        self.add_bezier('sym-e26', (24, 31), ((22.407, 31), (21.079, 31.52), (20, 33)))
        self.add_bezier('sym-e27', (20, 33), ((19.225, 34.073), (18.396, 35.718), (18, 37)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', closed=True)
