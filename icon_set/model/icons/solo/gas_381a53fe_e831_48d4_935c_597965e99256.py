"""Gas (_uncategorized), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '381a53fe-e831-48d4-935c-597965e99256'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_20/gas_381a53fe-e831-48d4-935c-597965e99256.svg'
AUTHOR = 'gpt-6'

class Gas(Solo48):
    icon_id = 'gas'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized'
    aliases = ()
    keywords = ('gas', '_uncategorized')

    def build(self):
        self.add_line('sym-e0', (24, 44), (25, 44))
        self.add_arc('sym-e1', (25, 44), (40, 30), radius_x=16, radius_y=16, large_arc=False, sweep=False)
        self.add_arc('sym-e2', (40, 30), (40, 29), radius_x=30, radius_y=30, large_arc=False, sweep=True)
        self.add_arc('sym-e3', (40, 29), (40, 28), radius_x=30, radius_y=30, large_arc=False, sweep=True)
        self.add_arc('sym-e4', (40, 28), (29, 9), radius_x=33, radius_y=33, large_arc=False, sweep=False)
        self.add_line('sym-e5', (29, 9), (25, 5))
        self.add_arc('sym-e6', (25, 5), (24, 4), radius_x=11, radius_y=11, large_arc=False, sweep=False)
        self.add_line('sym-e7', (24, 4), (19, 9))
        self.add_arc('sym-e9', (19, 9), (8, 28), radius_x=33, radius_y=33, large_arc=False, sweep=False)
        self.add_line('sym-e10', (8, 28), (8, 30))
        self.add_arc('sym-e12', (8, 30), (23, 44), radius_x=16, radius_y=16, large_arc=False, sweep=False)
        self.add_line('sym-e13', (23, 44), (24, 44))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e9', 'sym-e10', 'sym-e12', 'sym-e13', closed=True)
