"""Sr (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2ae3aaea-c96d-4420-a757-abdfc64cfd21'
SOURCE_PATH = 'icons-json/symbol/sr (text u)_2ae3aaea-c96d-4420-a757-abdfc64cfd21.json'
AUTHOR = 'json_to_solo'

class SrTextUSymbol(Solo48):
    icon_id = 'sr-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('sr', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (16, 16), (12, 14))
        self.add_line('e1', (31, 13), (31, 27))
        self.add_line('e2', (8, 44), (40, 44))
        self.add_bezier('e3', (8, 23), ((8.17, 23.173), (8.18, 23.455), (8.39, 23.609)), ((8.9, 24), (9.4, 24.455), (9.94, 24.818)), ((11.93, 26.164), (14.78, 26.818), (17.2, 26.209)), ((20.96, 25.273), (23.34, 21.1), (20.44, 18.173)), ((19.3, 17.009), (17.49, 16.682), (16, 16)))
        self.add_bezier('e4', (12, 14), ((10.98, 13.318), (9.6, 12.6), (9.07, 11.5)), ((8, 8.164), (9.93, 4.009), (14.13, 4.009)), ((14.287, 4.009), (14.445, 4), (14.603, 4)), ((14.605, 4), (14.607, 4), (14.61, 4)), ((14.78, 4), (14.94, 4.009), (15.11, 4.009)), ((17.41, 4.009), (19.35, 5.791), (21, 7)))
        self.add_bezier('e5', (40, 13), ((40, 13), (39.99, 13.082), (39.99, 13.082)), ((39.99, 13.018), (39.71, 12.845), (39.67, 12.818)), ((38.61, 12.064), (37.25, 11.736), (35.93, 11.945)), ((33.19, 12.391), (31.76, 14.791), (31, 17)))
        self.add_contour('c0', 'e3', 'e0', 'e4')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e5')
        self.add_contour('c3', 'e2')
        self.relate('connect', 'c2', 'c1')
