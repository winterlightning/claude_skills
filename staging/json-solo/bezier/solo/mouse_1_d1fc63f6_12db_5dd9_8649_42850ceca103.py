"""Mouse 1 (animals), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd1fc63f6-12db-5dd9-8649-42850ceca103'
SOURCE_PATH = 'icons-json/animals/mouse 1_d1fc63f6-12db-5dd9-8649-42850ceca103.json'
AUTHOR = 'json_to_solo'

class Mouse1(Solo48):
    icon_id = 'mouse-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('mouse', 'animals')

    def build(self):
        self.add_line('e0', (31, 23), (41, 34))
        self.add_line('e1', (41, 40), (13, 40))
        self.add_bezier('e2', (23, 28), ((22.245, 27.535), (21.636, 27.447), (20.982, 26.647)), ((18.673, 23.811), (17.291, 18.269), (18.545, 13.818)), ((19.3, 11.156), (20.936, 8.029), (22.964, 8.029)), ((23.164, 8.029), (23.373, 8), (23.582, 8)), ((23.59, 8), (23.597, 8), (23.605, 8)), ((24.097, 8), (24.59, 8.015), (25.091, 8.015)), ((28.655, 8.015), (31.627, 12.582), (31.736, 18.356)), ((31.755, 19.753), (31.2, 21.662), (31, 23)))
        self.add_bezier('e3', (41, 34), ((41.4, 34.465), (44, 38.342), (44, 38.429)), ((44, 38.433), (44, 38.437), (44, 38.441)), ((44, 38.703), (41.884, 39.985), (41.427, 39.985)), ((41.373, 39.985), (41.055, 40), (41, 40)))
        self.add_bezier('e4', (13, 40), ((12.855, 40), (12.8, 39.985), (12.645, 39.985)), ((8.264, 39.985), (4.009, 33.469), (4.009, 26.385)), ((4.009, 26.171), (4, 25.956), (4, 25.727)), ((4, 25.724), (4, 25.72), (4, 25.716)), ((4, 25.498), (4.009, 25.28), (4.009, 25.047)), ((4.009, 16.625), (9.645, 10.589), (14.536, 11.404)), ((16.027, 11.651), (17.736, 12.764), (19, 14)))
        self.add_bezier('e5', (29, 31), ((29.3, 31.48), (29.7, 32.52), (30, 33)))
        self.add_contour('c0', 'e2', 'e0', 'e3', 'e1', 'e4')
        self.add_contour('c1', 'e5')
