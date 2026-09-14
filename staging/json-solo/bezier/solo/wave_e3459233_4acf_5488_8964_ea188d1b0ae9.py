"""Wave (wayfinding), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e3459233-4acf-5488-8964-ea188d1b0ae9'
SOURCE_PATH = 'icons-json/wayfinding/wave_e3459233-4acf-5488-8964-ea188d1b0ae9.json'
AUTHOR = 'json_to_solo'

class Wave(Solo48):
    icon_id = 'wave'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    aliases = ()
    keywords = ('wave', 'wayfinding')

    def build(self):
        self.add_line('e0', (21, 11), (26, 16))
        self.add_bezier('e1', (4, 16), ((4.082, 15.776), (4.155, 15.552), (4.236, 15.328)), ((4.464, 14.96), (4.791, 14.816), (5.036, 14.48)), ((6.918, 11.92), (8.855, 10.384), (11.127, 9.168)), ((12.082, 8.672), (13.027, 8.016), (14.036, 8.016)), ((14.108, 8), (14.188, 8), (14.26, 8)), ((14.261, 8), (14.262, 8), (14.264, 8)), ((14.418, 8), (14.573, 8.032), (14.727, 8.032)), ((16.155, 8.032), (19.764, 9.688), (21, 11)))
        self.add_bezier('e2', (26, 16), ((27.409, 17.488), (28.845, 18.24), (30.445, 18.688)), ((36.064, 20.224), (40.118, 16.768), (44, 10)))
        self.add_bezier('e3', (4, 37), ((8.509, 30.216), (14.418, 26.896), (20.118, 31.2)), ((24.264, 34.32), (27.073, 39.968), (31.927, 39.968)), ((32.127, 39.968), (32.327, 40), (32.527, 40)), ((32.53, 40), (32.534, 40), (32.537, 40)), ((32.734, 40), (32.93, 39.984), (33.127, 39.984)), ((37.264, 39.984), (40.791, 36.096), (43.691, 31.296)), ((43.845, 31.024), (43.864, 30.288), (44, 30)))
        self.add_contour('c0', 'e1', 'e0', 'e2')
        self.add_contour('c1', 'e3')
