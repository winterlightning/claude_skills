"""Roof (state), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '28805be1-8602-45ee-8af6-319ec08b0104'
SOURCE_PATH = 'icons-json/state/roof_28805be1-8602-45ee-8af6-319ec08b0104.json'
AUTHOR = 'json_to_solo'

class RoofState(Solo48):
    icon_id = 'roof-state'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('roof', 'state')

    def build(self):
        self.add_line('e0', (4, 40), (24, 8))
        self.add_line('e1', (24, 8), (44, 40))
        self.add_contour('c0', 'e0', 'e1')
