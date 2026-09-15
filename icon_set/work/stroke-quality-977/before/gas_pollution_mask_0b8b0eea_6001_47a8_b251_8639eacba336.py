"""Gas pollution mask (protection), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0b8b0eea-6001-47a8-b251-8639eacba336'
SOURCE_PATH = 'pictographic-primitives/protection/gas pollution mask_0b8b0eea-6001-47a8-b251-8639eacba336.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class GasPollutionMask(Solo48):
    icon_id = 'gas-pollution-mask'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('gas', 'pollution', 'mask', 'protection')

    def build(self):
        self.add_line('e0', (8, 28), (8, 20))
        self.add_line('e1', (40, 28), (40, 20))
        self.add_line('e2', (40, 20), (31, 20))
        self.add_bezier('e3', (10, 35), ((11.836, 33.627), (13.373, 32.245), (15.427, 31.282)), ((24.354, 27.127), (30.168, 29.391), (38, 35)))
        self.add_bezier('e4', (10, 35), ((10.514, 35.864), (10.703, 36.718), (11.326, 37.5)), ((14.198, 41.1), (18.787, 43.991), (23.284, 43.991)), ((23.425, 43.991), (23.558, 44), (23.699, 44)), ((23.701, 44), (23.703, 44), (23.705, 44)), ((23.916, 44), (24.135, 43.991), (24.345, 43.991)), ((28.749, 43.991), (33.356, 41.491), (36.295, 38.027)), ((37.103, 37.073), (37.394, 36.109), (38, 35)))
        self.add_bezier('e5', (10, 35), ((9.082, 32.764), (8, 30.491), (8, 28)))
        self.add_bezier('e6', (38, 35), ((38.901, 32.718), (40, 30.518), (40, 28)))
        self.add_bezier('e7', (31, 20), ((28.322, 20), (23.133, 18.427), (20.968, 16.864)), ((20.118, 16.255), (19.301, 15.591), (18.594, 14.791)), ((18.215, 14.364), (17.836, 13.927), (17.457, 13.5)), ((17.187, 13.973), (16.909, 14.455), (16.64, 14.927)), ((16.185, 15.727), (15.68, 16.509), (15.04, 17.155)), ((12.901, 19.327), (10.846, 19.555), (8, 20)))
        self.add_bezier('e8', (40, 20), ((40, 19.627), (39.992, 19.609), (39.992, 19.236)), ((39.992, 18.636), (39.352, 16.373), (39.158, 15.755)), ((37.095, 9.173), (31.057, 4.009), (24.48, 4.009)), ((24.414, 4.009), (24.339, 4), (24.273, 4)), ((24.272, 4), (24.271, 4), (24.269, 4)), ((23.949, 4), (23.638, 4.009), (23.318, 4.009)), ((17.272, 4.009), (11.916, 8.518), (9.482, 14.282)), ((9.027, 15.364), (8.758, 16.473), (8.446, 17.6)), ((8.337, 17.991), (8.008, 18.455), (8.008, 18.864)), ((8.008, 18.882), (8, 18.909), (8, 18.927)), ((8, 19.409), (8, 19.518), (8, 20)))
        self.add_contour('c0', 'e3')
        self.add_contour('c1', 'e4')
        self.add_contour('c2', 'e5', 'e0')
        self.add_contour('c3', 'e6', 'e1')
        self.add_contour('c4', 'e2', 'e7')
        self.add_contour('c5', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
