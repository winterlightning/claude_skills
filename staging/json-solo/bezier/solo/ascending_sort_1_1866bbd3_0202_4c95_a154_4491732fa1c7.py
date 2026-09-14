"""Ascending sort 1 (_uncategorized_04), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1866bbd3-0202-4c95-a154-4491732fa1c7'
SOURCE_PATH = 'icons-json/_uncategorized_04/ascending sort 1_1866bbd3-0202-4c95-a154-4491732fa1c7.json'
AUTHOR = 'json_to_solo'

class AscendingSort1Uncategorized04(Solo48):
    icon_id = 'ascending-sort-1-uncategorized-04'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_04'
    aliases = ()
    keywords = ('ascending', 'sort', '_uncategorized_04')

    def build(self):
        self.add_line('e0', (24, 8), (44, 8))
        self.add_line('e1', (14, 24), (34, 24))
        self.add_line('e2', (4, 40), (24, 40))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
