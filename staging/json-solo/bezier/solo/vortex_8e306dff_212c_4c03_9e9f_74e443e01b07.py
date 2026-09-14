"""Vortex (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8e306dff-212c-4c03-9e9f-74e443e01b07'
SOURCE_PATH = 'icons-json/symbol/vortex_8e306dff-212c-4c03-9e9f-74e443e01b07.json'
AUTHOR = 'json_to_solo'

class VortexSymbol(Solo48):
    icon_id = 'vortex-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('vortex', 'symbol')

    def build(self):
        self.add_line('sym-e0', (8, 4), (21, 40))
        self.add_bezier('sym-e1', (21, 40), ((21.42, 41.164), (22.33, 44), (24, 44)))
        self.add_bezier('sym-e2', (24, 44), ((25.67, 44), (26.58, 41.164), (27, 40)))
        self.add_line('sym-e3', (27, 40), (40, 4))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3')
