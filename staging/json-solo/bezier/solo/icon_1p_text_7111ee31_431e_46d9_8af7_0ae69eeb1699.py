"""1p (text) (text), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7111ee31-431e-46d9-8af7-0ae69eeb1699'
SOURCE_PATH = 'icons-json/text/1P (text)_7111ee31-431e-46d9-8af7-0ae69eeb1699.json'
AUTHOR = 'json_to_solo'

class Icon1pTextText(Solo48):
    icon_id = 'icon-1p-text-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'text'
    aliases = ()
    keywords = ('1p', 'text')

    def build(self):
        self.add_line('e0', (12, 8), (12, 40))
        self.add_line('e1', (25, 25), (36, 25))
        self.add_line('e2', (36, 8), (25, 8))
        self.add_line('e3', (25, 8), (25, 40))
        self.add_bezier('e4', (4, 14), ((4.009, 14), (4.009, 13.886), (4.018, 13.886)), ((4.018, 13.869), (4.327, 13.752), (4.345, 13.743)), ((5.327, 13.297), (6.291, 12.825), (7.218, 12.286)), ((9.182, 11.166), (10.491, 9.583), (12, 8)))
        self.add_bezier('e5', (36, 25), ((36.5, 25), (37.064, 24.564), (37.573, 24.446)), ((41.464, 23.528), (43.991, 20.64), (43.991, 16.893)), ((43.991, 16.826), (44, 16.752), (44, 16.685)), ((44, 16.684), (44, 16.683), (44, 16.682)), ((44, 16.615), (43.991, 16.547), (43.991, 16.48)), ((43.991, 12.817), (41.791, 9.423), (37.9, 8.362)), ((37.218, 8.185), (36.7, 8), (36, 8)))
        self.add_contour('c0', 'e4', 'e0')
        self.add_contour('c1', 'e1', 'e5', 'e2', 'e3')
