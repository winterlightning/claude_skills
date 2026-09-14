"""Meeting headphone wireless (office), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5b320b4e-ed89-4f2f-be89-6e9fdbbeecce'
SOURCE_PATH = 'icons-json/office/meeting headphone wireless_5b320b4e-ed89-4f2f-be89-6e9fdbbeecce.json'
AUTHOR = 'json_to_solo'

class MeetingHeadphoneWirelessOffice(Solo48):
    icon_id = 'meeting-headphone-wireless-office'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('meeting', 'headphone', 'wireless', 'office')

    def build(self):
        self.add_line('e0', (27, 42), (27, 43))
        self.add_line('e1', (26, 44), (22, 44))
        self.add_line('e2', (22, 40), (26, 40))
        self.add_line('e3', (27, 40), (27, 42))
        self.add_line('e4', (34, 39), (34, 29))
        self.add_line('e5', (14, 39), (14, 29))
        self.add_bezier('e6', (14, 8), ((16.754, 5.645), (20.034, 4.009), (23.571, 4.009)), ((23.67, 4.009), (23.761, 4), (23.861, 4)), ((23.862, 4), (23.864, 4), (23.865, 4)), ((24.101, 4), (24.328, 4.009), (24.564, 4.009)), ((28.025, 4.009), (31.331, 5.636), (34, 8)))
        self.add_bezier('e7', (17, 12), ((21.093, 8.755), (26.941, 8.764), (31, 12)))
        self.add_bezier('e8', (27, 43), ((26.815, 43.245), (26.379, 44), (26, 44)))
        self.add_bezier('e9', (22, 44), ((21.832, 43.909), (21.954, 43.918), (21.785, 43.809)), ((20.724, 43.136), (20.488, 41.636), (21.482, 40.755)), ((21.743, 40.527), (21.705, 40.136), (22, 40)))
        self.add_bezier('e10', (26, 40), ((26.269, 40), (26.731, 40), (27, 40)))
        self.add_bezier('e11', (27, 42), ((28.735, 42.091), (30.922, 42.191), (32.387, 41.045)), ((33.002, 40.564), (33.411, 39.5), (34, 39)))
        self.add_bezier('e12', (34, 39), ((36.24, 39.364), (37.971, 39.136), (39.251, 37.036)), ((39.638, 36.418), (39.992, 35.664), (39.992, 34.9)), ((39.992, 34.827), (40, 34.755), (40, 34.691)), ((40, 34.69), (40, 34.689), (40, 34.688)), ((40, 34.616), (40, 34.544), (40, 34.473)), ((40, 33.664), (39.596, 32.818), (39.192, 32.155)), ((37.811, 29.909), (36.349, 29.091), (34, 29)))
        self.add_bezier('e13', (34, 29), ((34, 26.855), (33.903, 25.382), (33.002, 23.418)), ((30.147, 17.227), (21.794, 15.464), (17.095, 20.264)), ((14.745, 22.664), (14, 25.6), (14, 29)))
        self.add_bezier('e14', (14, 29), ((13.183, 29.073), (12.244, 29.527), (11.461, 29.809)), ((10.055, 30.318), (8.008, 32.391), (8.008, 34.091)), ((8.008, 34.127), (8, 34.154), (8, 34.189)), ((8, 34.19), (8, 34.19), (8, 34.191)), ((8, 34.309), (8.008, 34.436), (8.008, 34.555)), ((8.008, 36.527), (9.987, 38.791), (11.646, 39.327)), ((12.396, 39.564), (13.234, 39.036), (14, 39)))
        self.add_contour('c0', 'e6')
        self.add_contour('c1', 'e7')
        self.add_contour('c2', 'e0', 'e8', 'e1', 'e9', 'e2', 'e10', 'e3', closed=True)
        self.add_contour('c3', 'e11')
        self.add_contour('c4', 'e12')
        self.add_contour('c5', 'e4')
        self.add_contour('c6', 'e13')
        self.add_contour('c7', 'e14', 'e5', closed=True)
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c6', 'c7')
