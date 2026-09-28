"""Samsung (phones), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '89fcd972-9564-46c5-a760-343d18f6558b'
SOURCE_PATH = 'pictographic-primitives/phones/samsung_89fcd972-9564-46c5-a760-343d18f6558b.svg'
AUTHOR = 'gpt-6'

class Samsung(Solo48):
    icon_id = 'samsung'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'phones'
    categories = ('phones', 'primitives')
    aliases = ()
    keywords = ('samsung', 'phones')

    def build(self):
        self.add_line('sym-e0', (8, 34), (40, 34))
        self.add_line('sym-e1', (40, 34), (40, 8))
        self.add_arc('sym-e3', (40, 8), (36, 4), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e5', (36, 4), (12, 4))
        self.add_arc('sym-e8', (12, 4), (8, 8), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e10', (8, 8), (8, 40))
        self.add_arc('sym-e12', (8, 40), (12, 44), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('sym-e14', (12, 44), (36, 44))
        self.add_arc('sym-e17', (36, 44), (40, 40), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('sym-e18', (40, 40), (40, 34))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e3', 'sym-e5', 'sym-e8', 'sym-e10', 'sym-e12', 'sym-e14', 'sym-e17', 'sym-e18', closed=False)
