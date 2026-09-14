"""Samsung (phones), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '89fcd972-9564-46c5-a760-343d18f6558b'
SOURCE_PATH = 'icons-json/phones/samsung_89fcd972-9564-46c5-a760-343d18f6558b.json'
AUTHOR = 'json_to_solo'

class SamsungPhones(Solo48):
    icon_id = 'samsung-phones'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'phones'
    aliases = ()
    keywords = ('samsung', 'phones')

    def build(self):
        self.add_line('sym-e0', (8, 34), (40, 34))
        self.add_line('sym-e1', (40, 34), (40, 8))
        self.add_arc('sym-e3', (40, 8), (36, 4), radius_x=4, sweep=False)
        self.add_line('sym-e5', (36, 4), (24, 4))
        self.add_line('sym-e6', (24, 4), (12, 4))
        self.add_arc('sym-e8', (12, 4), (8, 8), radius_x=4, sweep=False)
        self.add_line('sym-e10', (8, 8), (8, 34))
        self.add_line('sym-e11', (8, 34), (8, 40))
        self.add_arc('sym-e12', (8, 40), (12, 44), radius_x=5, sweep=False)
        self.add_line('sym-e14', (12, 44), (24, 44))
        self.add_line('sym-e15', (24, 44), (36, 44))
        self.add_arc('sym-e17', (36, 44), (40, 40), radius_x=5, sweep=False)
        self.add_line('sym-e18', (40, 40), (40, 34))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e3', 'sym-e5', 'sym-e6', 'sym-e8', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e14', 'sym-e15', 'sym-e17', 'sym-e18')
