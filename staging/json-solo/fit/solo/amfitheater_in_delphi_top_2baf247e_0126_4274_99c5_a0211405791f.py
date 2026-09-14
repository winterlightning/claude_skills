"""Amfitheater in delphi top (_uncategorized_03), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2baf247e-0126-4274-99c5-a0211405791f'
SOURCE_PATH = 'icons-json/_uncategorized_03/amfitheater in delphi top_2baf247e-0126-4274-99c5-a0211405791f.json'
AUTHOR = 'json_to_solo'

class AmfitheaterInDelphiTopUncategorized03(Solo48):
    icon_id = 'amfitheater-in-delphi-top-uncategorized-03'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_03'
    aliases = ()
    keywords = ('amfitheater', 'in', 'delphi', 'top', '_uncategorized_03')

    def build(self):
        self.add_line('e0', (4, 39), (4, 27))
        self.add_line('e1', (44, 27), (44, 39))
        self.add_line('e2', (43, 40), (36, 40))
        self.add_line('e3', (35, 39), (35, 28))
        self.add_line('e4', (13, 28), (13, 39))
        self.add_line('e5', (12, 40), (5, 40))
        self.add_arc('e6-1', (4, 27), (23, 8), radius_x=20)
        self.add_line('e6-2', (23, 8), (30, 9))
        self.add_arc('e6-3', (30, 9), (37, 13), radius_x=20)
        self.add_arc('e6-4', (37, 13), (44, 27), radius_x=20)
        self.add_arc('e7', (44, 39), (43, 40), radius_x=1)
        self.add_arc('e8', (36, 40), (35, 39), radius_x=1)
        self.add_arc('e9', (35, 28), (13, 28), radius_x=11, sweep=False)
        self.add_arc('e10', (13, 39), (12, 40), radius_x=1)
        self.add_arc('e11', (5, 40), (4, 39), radius_x=2)
        self.add_contour('c0', 'e0', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e1', 'e7', 'e2', 'e8', 'e3', 'e9', 'e4', 'e10', 'e5', 'e11', closed=True)
