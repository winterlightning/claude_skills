'Diode: restore the actual shared triangle-to-cathode junction and straight leads instead of a near-miss gap.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '48d7386c-376e-5c40-998e-a110f5cf84d3'
SOURCE_PATH = 'icons-json/electronics/electronics shottkey diode_48d7386c-376e-5c40-998e-a110f5cf84d3.json'
AUTHOR = 'gpt-6'

class ElectronicsShottkeyDiode(Solo48):
    icon_id = 'electronics-shottkey-diode'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'electronics'
    aliases = ()
    keywords = ('electronics', 'shottkey', 'diode')

    def build(self) -> None:
        # HRECT_L: triangular diode, shared cathode contact, and split leads.
        self.add_polyline('diode',(14,8),(35,24),(14,40),(14,24),closed=True)
        self.add_polyline('cathode',(35,8),(35,24),(35,40))
        self.add_line('lead-left',(4,24),(14,24))
        self.add_line('lead-right',(35,24),(44,24))
        self.relate('connect','diode','cathode')
        self.relate('connect','diode','lead-left')
        self.relate('connect','cathode','lead-right')
        self.relate('connect','diode','lead-right')
