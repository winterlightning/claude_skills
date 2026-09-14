"""911 (text) (state), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '53668ec4-a104-4d57-8154-81e216c068e3'
SOURCE_PATH = 'icons-json/state/911 (text)_53668ec4-a104-4d57-8154-81e216c068e3.json'
AUTHOR = 'json_to_solo'

class Icon911TextState(Solo48):
    icon_id = 'icon-911-text-state'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('text', 'state')

    def build(self):
        self.add_line('e0', (30, 8), (30, 40))
        self.add_line('e1', (44, 8), (44, 40))
        self.add_bezier('e2', (16, 17), ((16, 17.406), (15.791, 17.44), (15.818, 17.846)), ((16.255, 23.778), (17.064, 30.326), (14.673, 35.717)), ((13.818, 37.625), (12.364, 39.988), (10.555, 39.988)), ((10.291, 39.988), (10.027, 40), (9.773, 40)), ((9.645, 40), (9.527, 39.988), (9.409, 39.988)), ((7.309, 39.988), (5.918, 38.437), (5, 36)))
        self.add_bezier('e3', (25, 14), ((27.427, 12.277), (28.236, 10.769), (30, 8)))
        self.add_bezier('e4', (39, 14), ((41.427, 12.277), (42.236, 10.782), (44, 8)))
        self.add_bezier('e5', (16, 18), ((16, 17.594), (15.864, 17.022), (15.818, 16.615)), ((15.364, 12.849), (13.609, 8.012), (10.318, 8.012)), ((10.227, 8.012), (10.127, 8), (10.027, 8)), ((9.836, 8), (9.645, 8.025), (9.455, 8.025)), ((6.245, 8.025), (4.009, 13.637), (4.009, 17.502)), ((4.009, 17.562), (4, 17.635), (4, 17.696)), ((4, 17.697), (4, 17.697), (4, 17.698)), ((4, 17.969), (4.009, 18.24), (4.009, 18.498)), ((4.009, 19.409), (4.218, 20.406), (4.4, 21.268)), ((5.155, 24.923), (7.036, 28), (10.036, 28)), ((11.045, 28), (12.064, 27.68), (12.909, 26.917)), ((15.082, 24.972), (15.873, 21.286), (16, 18)))
        self.add_contour('c0', 'e2')
        self.add_contour('c1', 'e3', 'e0')
        self.add_contour('c2', 'e4', 'e1')
        self.add_contour('c3', 'e5', closed=True)
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c3', 'c0')
