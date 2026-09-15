"""Subtract (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9f632c5f-0d4e-502e-9710-3d4446d843c1'
SOURCE_PATH = 'pictographic-primitives/interface-essential/subtract_9f632c5f-0d4e-502e-9710-3d4446d843c1.svg'
AUTHOR = 'gpt-6'

class SubtractInterfaceEssential(Solo48):
    icon_id = 'subtract-interface-essential'
    keyshape = Keyshape.FREE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('subtract', 'interface-essential')

    def build(self):
        self.add_line('e0', (4, 24), (44, 24))
        self.add_contour('c0', 'e0')
