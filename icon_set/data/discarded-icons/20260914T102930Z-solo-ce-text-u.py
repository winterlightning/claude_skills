"""Ce (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c8302404-8bb0-4abd-ad0a-69790af88bfe'
SOURCE_PATH = 'icons-json/symbol/ce (text u)_c8302404-8bb0-4abd-ad0a-69790af88bfe.json'
AUTHOR = 'json_to_solo'

class CeTextU(Solo48):
    icon_id = 'ce-text-u'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('ce', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 9), (8, 21))
        self.add_line('e1', (8, 44), (40, 44))
        self.add_bezier('e2', (19, 8), ((18.01, 6.136), (16.33, 4), (13.83, 4)), ((13.829, 4), (13.828, 4), (13.826, 4)), ((13.748, 4), (13.679, 4), (13.6, 4)), ((13.45, 4.009), (13.3, 4.009), (13.15, 4.018)), ((10.37, 4.018), (8, 6.864), (8, 9.236)), ((8, 9.309), (8, 8.927), (8, 9)))
        self.add_bezier('e3', (8, 21), ((8, 22.009), (8.5, 23.391), (9.13, 24.209)), ((11.26, 26.973), (15.77, 27.482), (18.5, 25.127)), ((19.18, 24.536), (19.59, 23.764), (20, 23)))
        self.add_bezier('e4', (29, 19), ((31.03, 19.236), (37.22, 20.427), (38.74, 19.282)), ((40, 18.045), (39.53, 14.755), (38.34, 13.536)), ((36.5, 11.655), (33.36, 11.727), (31.31, 13.227)), ((30.37, 13.909), (29.64, 14.836), (29.2, 15.855)), ((27.92, 18.864), (28.3, 24.836), (32.27, 26.082)), ((34.6, 26.809), (38.13, 26.118), (39.52, 24.145)), ((39.7, 23.891), (39.99, 23.473), (39.99, 23.155)), ((39.99, 23.136), (40, 23.018), (40, 23)))
        self.add_contour('c0', 'e2', 'e0', 'e3')
        self.add_contour('c1', 'e4')
        self.add_contour('c2', 'e1')
