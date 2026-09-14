"""Package (shipping), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '74975c3d-4711-563d-ae30-cdae3669b11b'
SOURCE_PATH = 'icons-json/shipping/package_74975c3d-4711-563d-ae30-cdae3669b11b.json'
AUTHOR = 'json_to_solo'

class PackageShipping(Solo48):
    icon_id = 'package-shipping'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shipping'
    aliases = ()
    keywords = ('package', 'shipping')

    def build(self):
        self.add_line('e0', (40, 13), (40, 34))
        self.add_line('e1', (40, 34), (24, 44))
        self.add_line('e2', (24, 44), (24, 22))
        self.add_line('e3', (24, 44), (8, 34))
        self.add_line('e4', (8, 34), (8, 13))
        self.add_line('e5', (40, 13), (24, 22))
        self.add_line('e6', (24, 22), (8, 13))
        self.add_line('e7', (8, 13), (24, 4))
        self.add_line('e8', (24, 4), (40, 13))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3', 'e4')
        self.add_contour('c3', 'e5', 'e6', 'e7', 'e8', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
