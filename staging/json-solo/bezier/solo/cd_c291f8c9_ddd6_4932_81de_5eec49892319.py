"""Batch-03/cd (computers), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c291f8c9-ddd6-4932-81de-5eec49892319'
SOURCE_PATH = 'icons-json/computers/batch-03/cd_c291f8c9-ddd6-4932-81de-5eec49892319.json'
AUTHOR = 'json_to_solo'

class Batch03Cd(Solo48):
    icon_id = 'batch-03-cd'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'computers'
    aliases = ()
    keywords = ('batch', 'cd', 'computers')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e1-top', (18, 24), (30, 24), radius_x=6)
        self.add_arc('e1-bottom', (30, 24), (18, 24), radius_x=6)
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
