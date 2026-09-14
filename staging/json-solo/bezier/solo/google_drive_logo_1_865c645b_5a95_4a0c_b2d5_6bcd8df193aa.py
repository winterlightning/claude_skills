"""Google drive logo 1 (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '865c645b-5a95-4a0c-b2d5-6bcd8df193aa'
SOURCE_PATH = 'icons-json/logos/google drive logo 1_865c645b-5a95-4a0c-b2d5-6bcd8df193aa.json'
AUTHOR = 'json_to_solo'

class GoogleDriveLogo1Logos(Solo48):
    icon_id = 'google-drive-logo-1-logos'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('google', 'drive', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (19, 8), (32, 31))
        self.add_line('e1', (31, 31), (16, 31))
        self.add_line('e2', (14, 32), (9, 39))
        self.add_line('e3', (18, 9), (4, 31))
        self.add_line('e4', (4, 32), (9, 39))
        self.add_line('e5', (19, 8), (29, 8))
        self.add_line('e6', (30, 9), (44, 31))
        self.add_line('e7', (44, 32), (39, 39))
        self.add_line('e8', (38, 40), (10, 40))
        self.add_bezier('e9', (32, 31), ((31.7, 31), (31.3, 31), (31, 31)))
        self.add_bezier('e10', (16, 31), ((15.3, 31.219), (14.618, 31.604), (14, 32)))
        self.add_bezier('e11', (19, 8), ((18.7, 8.278), (18.3, 8.722), (18, 9)))
        self.add_bezier('e12', (4, 31), ((4, 31.278), (4, 31.722), (4, 32)))
        self.add_bezier('e13', (29, 8), ((29.055, 8), (28.664, 8), (28.718, 8)), ((29.409, 8), (29.527, 8.638), (30, 9)))
        self.add_bezier('e14', (44, 31), ((44, 31.185), (44, 31.099), (44, 31.284)), ((44, 31.453), (44, 31.629), (44, 31.806)), ((44, 32.008), (44, 31.789), (44, 32)))
        self.add_bezier('e15', (39, 39), ((38.745, 39.379), (38.345, 39.983), (37.864, 39.983)), ((37.827, 39.992), (37.782, 39.992), (37.745, 40)), ((37.709, 40), (38.036, 40), (38, 40)))
        self.add_bezier('e16', (10, 40), ((9.573, 40), (9.3, 39.278), (9, 39)))
        self.add_contour('c0', 'e0', 'e9', 'e1', 'e10', 'e2')
        self.add_contour('c1', 'e11', 'e3', 'e12', 'e4')
        self.add_contour('c2', 'e5', 'e13', 'e6', 'e14', 'e7', 'e15', 'e8', 'e16')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
