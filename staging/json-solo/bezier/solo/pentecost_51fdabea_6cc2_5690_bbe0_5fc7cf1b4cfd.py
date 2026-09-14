"""Pentecost (holidays), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '51fdabea-6cc2-5690-bbe0-5fc7cf1b4cfd'
SOURCE_PATH = 'icons-json/holidays/pentecost_51fdabea-6cc2-5690-bbe0-5fc7cf1b4cfd.json'
AUTHOR = 'json_to_solo'

class PentecostHolidays(Solo48):
    icon_id = 'pentecost-holidays'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'holidays'
    aliases = ()
    keywords = ('pentecost', 'holidays')

    def build(self):
        self.add_line('e0', (16, 28), (12, 26))
        self.add_line('e1', (4, 15), (19, 15))
        self.add_line('e2', (19, 15), (17, 8))
        self.add_line('e3', (17, 8), (31, 8))
        self.add_line('e4', (29, 15), (44, 15))
        self.add_line('e5', (26, 35), (24, 40))
        self.add_bezier('e6', (24, 40), ((22.636, 35.126), (20.945, 30.671), (17.227, 28.517)), ((16.773, 28.258), (16.473, 28.16), (16, 28)))
        self.add_bezier('e7', (12, 26), ((7.718, 24.548), (5.264, 20.551), (4, 15)))
        self.add_bezier('e8', (31, 8), ((30.9, 8.135), (31.082, 8.258), (30.982, 8.394)), ((30.845, 8.702), (30.809, 9.071), (30.691, 9.391)), ((30.209, 10.782), (29.273, 11.988), (28.945, 13.477)), ((28.809, 14.117), (29.136, 14.36), (29, 15)))
        self.add_bezier('e9', (44, 15), ((43.191, 18.643), (41.764, 22.388), (39.3, 24.492)), ((37.045, 26.425), (34.4, 26.178), (31.927, 27.138)), ((29.018, 28.271), (27.3, 31.48), (26, 35)))
        self.add_contour('c0', 'e6', 'e0', 'e7', 'e1', 'e2', 'e3', 'e8', 'e4', 'e9', 'e5', closed=True)
