"""Module (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ca74717c-d643-46df-99a4-bf0ae5577ead'
SOURCE_PATH = 'icons-json/design/module_ca74717c-d643-46df-99a4-bf0ae5577ead.json'
AUTHOR = 'json_to_solo'

class Module(Solo48):
    icon_id = 'module'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('module', 'design')

    def build(self):
        self.add_line('e0', (42, 13), (42, 35))
        self.add_line('e1', (42, 35), (24, 42))
        self.add_line('e2', (42, 13), (24, 19))
        self.add_line('e3', (42, 13), (24, 6))
        self.add_line('e4', (23, 6), (6, 13))
        self.add_line('e5', (24, 42), (24, 19))
        self.add_line('e6', (24, 42), (6, 35))
        self.add_line('e7', (6, 35), (6, 13))
        self.add_line('e8', (24, 19), (6, 13))
        self.add_line('e9', (24, 6), (23, 6))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3', 'e9', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6', 'e7')
        self.add_contour('c5', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
