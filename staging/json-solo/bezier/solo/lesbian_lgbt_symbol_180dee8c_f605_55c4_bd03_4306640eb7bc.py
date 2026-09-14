"""Lesbian lgbt symbol (romance), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '180dee8c-f605-55c4-bd03-4306640eb7bc'
SOURCE_PATH = 'icons-json/romance/lesbian lgbt symbol_180dee8c-f605-55c4-bd03-4306640eb7bc.json'
AUTHOR = 'json_to_solo'

class LesbianLgbtSymbolRomance(Solo48):
    icon_id = 'lesbian-lgbt-symbol-romance'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'romance'
    aliases = ()
    keywords = ('lesbian', 'lgbt', 'symbol', 'romance')

    def build(self):
        self.add_line('e0', (16, 42), (16, 28))
        self.add_line('e1', (12, 36), (21, 36))
        self.add_line('e2', (32, 28), (32, 42))
        self.add_line('e3', (27, 36), (36, 36))
        self.add_line('e4', (18, 19), (23, 25))
        self.add_line('e5', (25, 25), (30, 19))
        self.add_bezier('e6', (23, 25), ((20.922, 26.849), (18.682, 28.075), (15.818, 28.091)), ((10.263, 28.124), (6.016, 22.601), (6.016, 17.315)), ((6.016, 17.13), (6, 16.945), (6, 16.76)), ((6, 16.757), (6, 16.754), (6, 16.751)), ((6, 16.563), (6.016, 16.375), (6.016, 16.186)), ((6.016, 11.187), (10.557, 6.008), (15.695, 6.008)), ((15.816, 6.008), (15.937, 6), (16.058, 6)), ((16.06, 6), (16.062, 6), (16.064, 6)), ((16.186, 6), (16.309, 6.008), (16.432, 6.008)), ((17.626, 6.008), (18.895, 6.599), (20, 7)))
        self.add_bezier('e7', (28, 7), ((29.064, 6.607), (30.284, 6.008), (31.437, 6.008)), ((31.552, 6.008), (31.666, 6), (31.781, 6)), ((31.953, 6), (32.125, 6.008), (32.296, 6.008)), ((37.451, 6.008), (41.984, 11.457), (41.984, 16.399)), ((41.984, 16.587), (42, 16.767), (42, 16.955)), ((42, 16.958), (42, 16.961), (42, 16.964)), ((42, 17.15), (41.984, 17.335), (41.984, 17.52)), ((41.984, 22.642), (37.394, 27.976), (32.182, 28.091)), ((29.31, 28.156), (27.045, 26.898), (25, 25)))
        self.add_bezier('e8', (23, 25), ((23.548, 25), (24.452, 25), (25, 25)))
        self.add_bezier('e9', (30, 19), ((30.237, 18.73), (30.12, 18.404), (30.284, 18.085)), ((31.699, 15.327), (30.611, 11.875), (27.068, 12.161)), ((26.168, 12.235), (25.399, 12.791), (24.72, 13.347)), ((24.515, 13.519), (23.984, 14.067), (23.902, 14.051)), ((23.705, 14.018), (23.615, 13.781), (23.468, 13.65)), ((22.666, 12.93), (21.783, 12.185), (20.662, 12.128)), ((18.469, 12.014), (16.522, 13.519), (16.677, 15.859)), ((16.751, 17.054), (17.239, 18.116), (18, 19)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e6')
        self.add_contour('c3', 'e7')
        self.add_contour('c4', 'e2')
        self.add_contour('c5', 'e3')
        self.add_contour('c6', 'e4', 'e8', 'e5', 'e9', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c4', 'c3')
