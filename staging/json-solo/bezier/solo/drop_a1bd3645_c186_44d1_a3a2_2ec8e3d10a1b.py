"""Drop (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a1bd3645-c186-44d1-a3a2-2ec8e3d10a1b'
SOURCE_PATH = 'icons-json/smileys/drop_a1bd3645-c186-44d1-a3a2-2ec8e3d10a1b.json'
AUTHOR = 'json_to_solo'

class Drop(Solo48):
    icon_id = 'drop'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('drop', 'smileys')

    def build(self):
        self.add_bezier('e0', (24, 36), ((28.37, 34.918), (30.08, 32.909), (31, 29)))
        self.add_bezier('e1', (23, 5), ((18.06, 9.327), (13.51, 14.891), (10.56, 20.527)), ((9.26, 23), (8.01, 25.791), (8.01, 28.582)), ((8.01, 28.671), (8, 28.761), (8, 28.85)), ((8, 28.852), (8, 28.853), (8, 28.855)), ((8, 29.155), (8.02, 29.455), (8.02, 29.755)), ((8.02, 36.964), (15.41, 43.991), (23.41, 43.991)), ((23.518, 43.991), (23.627, 44), (23.735, 44)), ((23.737, 44), (23.738, 44), (23.74, 44)), ((23.95, 44), (24.15, 43.991), (24.36, 43.991)), ((32.7, 43.991), (39.99, 36.955), (39.99, 29.436)), ((39.99, 29.347), (40, 29.257), (40, 29.168)), ((40, 29.166), (40, 29.165), (40, 29.164)), ((40, 28.973), (39.99, 28.773), (39.99, 28.582)), ((39.99, 22.336), (33.35, 13.391), (28.95, 8.855)), ((27.78, 7.645), (26.49, 6.536), (25.29, 5.345)), ((24.85, 4.891), (24.41, 4.445), (23.96, 4)), ((23.955, 4.005), (23.95, 4), (23.945, 4)), ((23.63, 4), (23.315, 4.705), (23, 5)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', closed=True)
