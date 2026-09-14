"""Rim (_uncategorized), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5cd23b26-10aa-4dbd-8ddc-818520089ef7'
SOURCE_PATH = 'icons-json/_uncategorized_32/rim_5cd23b26-10aa-4dbd-8ddc-818520089ef7.json'
AUTHOR = 'json_to_solo'

class Rim(Solo48):
    icon_id = 'rim'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized'
    aliases = ()
    keywords = ('rim', '_uncategorized')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
