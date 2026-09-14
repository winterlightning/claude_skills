"""Drop (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3057870d-1409-44b0-8369-04ad03f65bba'
SOURCE_PATH = 'icons-json/smileys/drop_3057870d-1409-44b0-8369-04ad03f65bba.json'
AUTHOR = 'json_to_solo'

class Drop3057870d(Solo48):
    icon_id = 'drop-3057870d'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('drop', 'smileys')

    def build(self):
        self.add_line('e0', (26, 6), (24, 4))
        self.add_bezier('e1', (24, 4), ((19.18, 8.482), (14.92, 13.618), (11.5, 19.064)), ((9.79, 21.782), (8, 24.964), (8, 28.191)), ((8, 28.192), (8, 28.193), (8, 28.194)), ((8, 28.266), (8, 28.337), (8, 28.4)), ((8, 28.691), (8.02, 28.973), (8.02, 29.264)), ((8.02, 37.064), (15.44, 43.991), (24.06, 43.991)), ((24.139, 44), (24.218, 44), (24.287, 44)), ((24.288, 44), (24.289, 44), (24.29, 44)), ((24.45, 43.991), (24.6, 43.991), (24.76, 43.982)), ((32.6, 43.982), (39.99, 36.818), (39.99, 29.791)), ((39.99, 29.585), (40, 29.379), (40, 29.165)), ((40, 29.161), (40, 29.158), (40, 29.155)), ((40, 28.873), (39.98, 28.591), (39.98, 28.309)), ((39.98, 25.409), (38.58, 22.573), (37.1, 20.073)), ((34.98, 16.464), (32.32, 13.073), (29.59, 9.836)), ((28.44, 8.473), (27.34, 7.218), (26, 6)))
        self.add_contour('c0', 'e0', 'e1', closed=True)
