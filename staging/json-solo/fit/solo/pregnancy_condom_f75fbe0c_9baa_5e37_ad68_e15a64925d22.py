"""Pregnancy condom (health), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f75fbe0c-9baa-5e37-ad68-e15a64925d22'
SOURCE_PATH = 'icons-json/health/pregnancy condom_f75fbe0c-9baa-5e37-ad68-e15a64925d22.json'
AUTHOR = 'json_to_solo'

class PregnancyCondomHealth(Solo48):
    icon_id = 'pregnancy-condom-health'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('pregnancy', 'condom', 'health')

    def build(self):
        self.add_line('e0', (17, 40), (8, 31))
        self.add_line('e1', (8, 31), (26, 13))
        self.add_line('e2', (37, 20), (17, 40))
        self.add_line('e3', (17, 40), (19, 42))
        self.add_line('e4', (6, 29), (8, 31))
        self.add_arc('e5-1', (26, 13), (29, 10), radius_x=49)
        self.add_arc('e5-2', (29, 10), (33, 8), radius_x=8)
        self.add_line('e5-3', (33, 8), (37, 8))
        self.add_arc('e5-4', (37, 8), (40, 6), radius_x=5)
        self.add_arc('e5-5', (40, 6), (42, 8), radius_x=2)
        self.add_arc('e5-6', (42, 8), (40, 15), radius_x=6, sweep=False)
        self.add_arc('e5-7', (40, 15), (37, 20), radius_x=9)
        self.add_contour('c0', 'e0', 'e1', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6', 'e5-7', 'e2', 'e3')
        self.add_contour('c1', 'e4')
