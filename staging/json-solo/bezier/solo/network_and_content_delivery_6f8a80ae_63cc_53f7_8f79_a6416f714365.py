"""Network and content delivery (websites), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6f8a80ae-63cc-53f7-8f79-a6416f714365'
SOURCE_PATH = 'icons-json/websites/network and content delivery_6f8a80ae-63cc-53f7-8f79-a6416f714365.json'
AUTHOR = 'json_to_solo'

class NetworkAndContentDeliveryWebsites(Solo48):
    icon_id = 'network-and-content-delivery-websites'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'websites'
    aliases = ()
    keywords = ('network', 'and', 'content', 'delivery', 'websites')

    def build(self):
        self.add_line('e0', (13, 39), (24, 29))
        self.add_line('e1', (24, 28), (24, 40))
        self.add_line('e2', (24, 29), (36, 39))
        self.add_line('e3', (16, 28), (26, 28))
        self.add_line('e4', (26, 28), (35, 28))
        self.add_arc('e5-top', (22, 42), (26, 42), radius_x=2)
        self.add_arc('e5-bottom', (26, 42), (22, 42), radius_x=2)
        self.add_bezier('e6', (35, 28), ((35.657, 27.736), (36.295, 27.127), (36.876, 26.682)), ((38.787, 25.227), (40, 22.4), (40, 19.891)), ((40, 19.89), (40, 19.889), (40, 19.888)), ((40, 19.816), (39.992, 19.744), (39.992, 19.673)), ((39.992, 15.536), (36.985, 11.873), (33.103, 11.691)), ((32.362, 11.655), (31.528, 11.718), (30.813, 11.936)), ((30.291, 12.1), (29.768, 12.273), (29.246, 12.436)), ((29.213, 12.345), (29.171, 12.255), (29.137, 12.155)), ((28.96, 11.736), (28.783, 11.327), (28.589, 10.918)), ((28.16, 9.982), (27.705, 9.109), (27.091, 8.318)), ((25.103, 5.718), (22.232, 4.009), (19.065, 4.009)), ((18.833, 4.009), (18.609, 4), (18.385, 4)), ((18.382, 4), (18.378, 4), (18.375, 4)), ((18.307, 4.009), (18.232, 4.009), (18.164, 4.018)), ((12.775, 4.018), (8.008, 9.782), (8.008, 15.455)), ((8.008, 15.669), (8, 15.875), (8, 16.09)), ((8, 16.093), (8, 16.097), (8, 16.1)), ((8, 16.436), (8.008, 16.764), (8.008, 17.1)), ((8.008, 20.8), (10.459, 24.6), (13.364, 26.382)), ((14.316, 26.973), (14.973, 27.664), (16, 28)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e4', 'e6', closed=True)
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'e5')
