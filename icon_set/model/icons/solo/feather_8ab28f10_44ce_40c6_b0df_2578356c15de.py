"""Feather (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8ab28f10-44ce-40c6-b0df-2578356c15de'
SOURCE_PATH = 'icons-json/symbol/feather_8ab28f10-44ce-40c6-b0df-2578356c15de.json'
AUTHOR = 'json_to_solo'

class Feather(Solo48):
    icon_id = 'feather'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('feather', 'symbol')

    def build(self):
        self.add_line('e0', (8, 44), (13, 37))
        self.add_line('e1', (13, 37), (31, 14))
        self.add_bezier('e2', (13, 37), ((12.175, 35.7), (11.298, 34.173), (10.917, 32.755)), ((8.431, 23.409), (18.166, 14.827), (27.385, 9.464)), ((29.969, 7.964), (32.652, 6.573), (35.446, 5.282)), ((35.858, 5.094), (37.999, 4), (38.219, 4)), ((38.222, 4), (38.225, 4), (38.228, 4)), ((38.326, 4.291), (38.437, 4.573), (38.535, 4.864)), ((38.634, 5.155), (38.745, 5.436), (38.843, 5.727)), ((39.508, 7.609), (39.988, 9.655), (39.988, 11.6)), ((39.988, 11.663), (40, 11.734), (40, 11.797)), ((40, 11.798), (40, 11.799), (40, 11.8)), ((40, 12.073), (39.988, 12.336), (39.988, 12.609)), ((39.988, 14.345), (39.311, 18.727), (37.945, 20.073)), ((37.563, 20.445), (36.923, 20.755), (36.406, 21.027)), ((33.662, 22.527), (31.04, 23.855), (28, 25)))
        self.add_bezier('e3', (36, 24), ((31.323, 31.618), (24.323, 36.218), (13, 37)))
        self.add_contour('c0', 'e0', 'e2')
        self.add_contour('c1', 'e3', 'e1')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c0')
