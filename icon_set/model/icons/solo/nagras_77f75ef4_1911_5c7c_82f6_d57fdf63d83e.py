"""Nagras (money), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '77f75ef4-1911-5c7c-82f6-d57fdf63d83e'
SOURCE_PATH = 'icons-json/money/nagras_77f75ef4-1911-5c7c-82f6-d57fdf63d83e.json'
AUTHOR = 'json_to_solo'

class Nagras(Solo48):
    icon_id = 'nagras'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('nagras', 'money')

    def build(self):
        self.add_line('e0', (8, 30), (35, 30))
        self.add_line('e1', (35, 30), (35, 44))
        self.add_line('e2', (35, 44), (13, 4))
        self.add_line('e3', (13, 4), (13, 44))
        self.add_line('e4', (40, 23), (8, 23))
        self.add_line('e5', (35, 4), (35, 30))
        self.add_line('e6', (35, 30), (40, 30))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3')
        self.add_contour('c1', 'e4')
        self.add_contour('c2', 'e5', 'e6')
        self.relate('connect', 'c0', 'c2')
