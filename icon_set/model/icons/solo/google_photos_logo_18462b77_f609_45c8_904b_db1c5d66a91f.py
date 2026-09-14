"""Google photos logo (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '18462b77-f609-45c8-904b-db1c5d66a91f'
SOURCE_PATH = 'icons-json/logos/google photos logo_18462b77-f609-45c8-904b-db1c5d66a91f.json'
AUTHOR = 'json_to_solo'

class GooglePhotosLogo(Solo48):
    icon_id = 'google-photos-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('google', 'photos', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (23, 26), (22, 24))
        self.add_line('e1', (23, 26), (22, 32))
        self.add_line('e2', (22, 32), (22, 42))
        self.add_line('e3', (42, 24), (29, 24))
        self.add_line('e4', (29, 24), (27, 24))
        self.add_line('e5', (20, 24), (22, 24))
        self.add_line('e6', (20, 24), (6, 24))
        self.add_line('e7', (27, 24), (22, 24))
        self.add_line('e8', (22, 6), (22, 22))
        self.add_bezier('e9', (22, 42), ((21.771, 42), (21.897, 42), (21.668, 42)), ((21.447, 42), (21.226, 41.828), (21.022, 41.755)), ((19.238, 41.067), (18.076, 40.445), (16.874, 38.866)), ((14.419, 35.643), (14.067, 31.126), (16.285, 27.682)), ((17.25, 26.193), (18.658, 25.162), (20, 24)))
        self.add_bezier('e10', (23, 26), ((24.645, 28.806), (26.217, 31.634), (29.474, 32.689)), ((33.835, 34.105), (38.645, 31.895), (40.789, 27.919)), ((41.051, 27.428), (42, 25.301), (42, 24.794)), ((42, 24.532), (42, 24.262), (42, 24)))
        self.add_bezier('e11', (6, 24), ((6, 23.746), (6.016, 23.501), (6.016, 23.247)), ((6.016, 22.871), (6.9, 21.079), (7.154, 20.637)), ((8.986, 17.414), (13.282, 15.278), (16.898, 16.546)), ((19.713, 17.528), (20.486, 19.619), (22, 22)))
        self.add_bezier('e12', (27, 24), ((29.34, 22.445), (31.519, 21.185), (32.305, 18.355)), ((33.687, 13.347), (30.382, 8.635), (25.808, 6.835)), ((25.301, 6.638), (23.525, 6), (23.051, 6)), ((23.026, 6), (22.994, 6), (22.969, 6)), ((22.765, 6), (22.205, 6), (22, 6)))
        self.add_bezier('e13', (22, 22), ((22, 22.548), (22, 23.452), (22, 24)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e9')
        self.add_contour('c2', 'e10', 'e3', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6', 'e11')
        self.add_contour('c5', 'e7')
        self.add_contour('c6', 'e12', 'e8')
        self.add_contour('c7', 'e13')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c0', 'c7')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c3', 'c7')
        self.relate('connect', 'c5', 'c7')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c4', 'c7')
        self.relate('connect', 'c6', 'c7')
