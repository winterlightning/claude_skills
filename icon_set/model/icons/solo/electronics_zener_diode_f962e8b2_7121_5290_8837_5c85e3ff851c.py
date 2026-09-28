"""Electronics zener diode (electronics), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f962e8b2-7121-5290-8837-5c85e3ff851c'
SOURCE_PATH = 'pictographic-primitives/electronics/electronics zener diode_f962e8b2-7121-5290-8837-5c85e3ff851c.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ElectronicsZenerDiode(Solo48):
    icon_id = 'electronics-zener-diode'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'electronics'
    categories = ('electronics', 'primitives')
    aliases = ()
    keywords = ('electronics', 'zener', 'diode')

    def build(self):
        self.add_line('e0', (32, 23), (14, 10))
        self.add_line('e1', (14, 10), (14, 36))
        self.add_line('e2', (14, 36), (32, 23))
        self.add_line('e3', (32, 23), (44, 23))
        self.add_line('e4', (31, 8), (35, 12))
        self.add_line('e5', (35, 12), (35, 36))
        self.add_line('e6', (35, 36), (38, 40))
        self.add_line('e7', (4, 23), (14, 23))
        self.add_contour('c0', 'e0', 'e1', 'e2', closed=True)
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4', 'e5', 'e6')
        self.add_contour('c3', 'e7')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c3', 'c0')
