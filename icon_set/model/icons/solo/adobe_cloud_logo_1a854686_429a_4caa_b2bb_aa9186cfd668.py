"""Adobe cloud logo (_uncategorized_01), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1a854686-429a-4caa-b2bb-aa9186cfd668'
SOURCE_PATH = 'icons-json/_uncategorized_01/adobe cloud logo_1a854686-429a-4caa-b2bb-aa9186cfd668.json'
AUTHOR = 'json_to_solo'

class AdobeCloudLogo(Solo48):
    icon_id = 'adobe-cloud-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_01'
    aliases = ()
    keywords = ('adobe', 'cloud', 'logo', '_uncategorized_01')

    def build(self):
        self.add_line('e0', (27, 24), (19, 15))
        self.add_line('e1', (20, 40), (11, 29))
        self.add_line('e2', (16, 23), (30, 40))
        self.add_line('e3', (20, 40), (30, 40))
        self.add_bezier('e4', (11, 29), ((10.7, 28.335), (10.655, 27.729), (10.536, 26.942)), ((10.1, 24.049), (12.355, 21.514), (14.391, 21.994)), ((14.927, 22.117), (15.518, 22.692), (16, 23)))
        self.add_bezier('e5', (20, 40), ((19.273, 40), (18.909, 39.975), (18.182, 39.975)), ((18.118, 39.975), (18.045, 39.975), (17.982, 39.975)), ((17.536, 39.975), (17.082, 39.975), (16.636, 39.975)), ((16.391, 39.975), (16.155, 40), (15.909, 40)), ((15.355, 40), (14.8, 39.988), (14.245, 39.988)), ((14.173, 39.988), (14.109, 39.975), (14.036, 39.975)), ((9.091, 39.975), (4.009, 33.92), (4.009, 27.052)), ((4.009, 26.968), (4, 26.871), (4, 26.786)), ((4, 26.784), (4, 26.783), (4, 26.782)), ((4, 26.498), (4.009, 26.215), (4.009, 25.932)), ((4.009, 18.695), (9.709, 13.182), (14.727, 13.538)), ((16.109, 13.637), (17.955, 13.757), (19, 15)))
        self.add_bezier('e6', (30, 40), ((30.7, 40), (31.764, 39.988), (32.455, 39.988)), ((37.955, 39.988), (43.991, 32.812), (43.991, 25.169)), ((43.991, 25.084), (44, 25.012), (44, 24.927)), ((44, 24.926), (44, 24.924), (44, 24.923)), ((44, 24.542), (43.991, 24.172), (43.991, 23.791)), ((43.991, 15.262), (37.573, 8.025), (31.491, 8.025)), ((31.327, 8.025), (31.164, 8), (31, 8)), ((30.995, 8), (30.989, 8), (30.984, 8)), ((30.653, 8), (30.331, 8.025), (30, 8.025)), ((26.927, 8.025), (23.691, 9.994), (21.364, 12.603)), ((20.645, 13.415), (19.6, 14.04), (19, 15)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e4', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')
