"""Cs (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9c2ec6b1-ebb1-498d-ab11-45b453e4546a'
SOURCE_PATH = 'icons-json/symbol/cs (text u)_9c2ec6b1-ebb1-498d-ab11-45b453e4546a.json'
AUTHOR = 'json_to_solo'

class CsTextU(Solo48):
    icon_id = 'cs-text-u'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('cs', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 9), (8, 21))
        self.add_line('e1', (8, 44), (40, 44))
        self.add_bezier('e2', (21, 8), ((19.79, 5.982), (17.74, 4.009), (15.06, 4.009)), ((14.9, 4.009), (14.74, 4), (14.58, 4)), ((14.579, 4), (14.577, 4), (14.576, 4)), ((14.497, 4), (14.419, 4), (14.34, 4.009)), ((11.38, 4.009), (8, 6.382), (8, 9.236)), ((8, 9.309), (8, 8.927), (8, 9)))
        self.add_bezier('e3', (8, 21), ((8, 21.982), (8.53, 23.355), (9.16, 24.127)), ((11.55, 27.073), (16.54, 27.491), (19.5, 25.009)), ((20.17, 24.445), (20.57, 23.709), (21, 23)))
        self.add_bezier('e4', (40, 16), ((40, 15.982), (39.99, 15.791), (39.99, 15.773)), ((39.99, 15.291), (39.56, 14.627), (39.31, 14.218)), ((38.78, 13.345), (38, 12.564), (36.95, 12.209)), ((34.41, 11.345), (30.9, 12.864), (30.89, 15.509)), ((30.87, 18.709), (34.59, 19.191), (37.14, 20.236)), ((38.35, 20.727), (39.99, 21.564), (39.99, 22.964)), ((40, 23.018), (40, 23.073), (40, 23.127)), ((40, 23.182), (40, 23.245), (40, 23.3)), ((40, 26.736), (33.76, 27.291), (31.77, 25.209)), ((31.16, 24.573), (31.1, 23.782), (31, 23)))
        self.add_contour('c0', 'e2', 'e0', 'e3')
        self.add_contour('c1', 'e4')
        self.add_contour('c2', 'e1')
