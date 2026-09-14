"""Clip (office), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '61ccd621-bbc0-4581-842b-098e1372d4ff'
SOURCE_PATH = 'icons-json/office/clip_61ccd621-bbc0-4581-842b-098e1372d4ff.json'
AUTHOR = 'json_to_solo'

class ClipOffice(Solo48):
    icon_id = 'clip-office'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('clip', 'office')

    def build(self):
        self.add_line('e0', (19, 19), (7, 19))
        self.add_line('e1', (4, 21), (4, 37))
        self.add_line('e2', (7, 40), (13, 40))
        self.add_line('e3', (15, 38), (19, 20))
        self.add_line('e4', (17, 8), (31, 8))
        self.add_line('e5', (29, 17), (29, 19))
        self.add_line('e6', (19, 19), (29, 19))
        self.add_line('e7', (29, 19), (41, 19))
        self.add_line('e8', (44, 21), (44, 37))
        self.add_line('e9', (41, 40), (35, 40))
        self.add_line('e10', (33, 38), (29, 20))
        self.add_line('e11', (19, 40), (29, 40))
        self.add_bezier('e12', (7, 19), ((5.845, 19.413), (4, 19.644), (4, 21)))
        self.add_bezier('e13', (4, 37), ((4, 38.095), (5.827, 40), (7, 40)))
        self.add_bezier('e14', (13, 40), ((13.173, 39.916), (13.473, 39.933), (13.655, 39.848)), ((14.227, 39.554), (14.882, 38.615), (15, 38)))
        self.add_bezier('e15', (19, 20), ((19.3, 19.722), (18.7, 19.278), (19, 19)))
        self.add_bezier('e16', (19, 19), ((18.682, 18.469), (18.764, 17.549), (18.227, 17.044)), ((17.227, 16.109), (15.782, 15.747), (14.9, 14.686)), ((13.482, 12.977), (13.3, 10.021), (15.3, 8.606)), ((15.755, 8.286), (16.473, 8.168), (17, 8)))
        self.add_bezier('e17', (31, 8), ((31.464, 8.16), (32.109, 8.211), (32.536, 8.497)), ((34.536, 9.836), (34.4, 12.733), (33.091, 14.434)), ((32.291, 15.478), (31.045, 15.907), (30.018, 16.691)), ((29.791, 16.859), (29.2, 16.815), (29, 17)))
        self.add_bezier('e18', (41, 19), ((42, 19), (44, 19.88), (44, 21)))
        self.add_bezier('e19', (44, 37), ((43.945, 37.143), (43.973, 37.777), (43.927, 37.92)), ((43.655, 38.779), (42.527, 39.992), (41.464, 39.992)), ((41.4, 39.992), (41.064, 40), (41, 40)))
        self.add_bezier('e20', (35, 40), ((34.191, 39.646), (33.182, 38.943), (33, 38)))
        self.add_bezier('e21', (29, 20), ((28.7, 19.722), (29.3, 19.278), (29, 19)))
        self.add_contour('c0', 'e0', 'e12', 'e1', 'e13', 'e2', 'e14', 'e3', 'e15', closed=True)
        self.add_contour('c1', 'e16', 'e4', 'e17', 'e5')
        self.add_contour('c2', 'e6')
        self.add_contour('c3', 'e7', 'e18', 'e8', 'e19', 'e9', 'e20', 'e10', 'e21', closed=True)
        self.add_contour('c4', 'e11')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
