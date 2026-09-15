"""Tags (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eb9aab75-b57d-5009-bb88-39158cb8ee4a'
SOURCE_PATH = 'pictographic-primitives/interface-essential/tags_eb9aab75-b57d-5009-bb88-39158cb8ee4a.svg'
AUTHOR = 'gpt-6'

class Tags(Solo48):
    icon_id = 'tags'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('tags', 'interface-essential')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_arc('sym-e0', (20, 19), (28, 19), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('sym-e1', (28, 19), (20, 19), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e2', (8, 39), (8, 40))
        self.add_arc('sym-e3', (8, 40), (12, 44), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e4', (12, 44), (13, 44))
        self.add_arc('sym-e5', (13, 44), (14, 44), radius_x=24, radius_y=24, large_arc=False, sweep=True)
        self.add_arc('sym-e6-1', (14, 44), (15, 44), radius_x=24, radius_y=24, large_arc=False, sweep=True)
        self.add_arc('sym-e6-2', (15, 44), (16, 44), radius_x=24, radius_y=24, large_arc=False, sweep=True)
        self.add_line('sym-e7', (16, 44), (24, 44))
        self.add_line('sym-e8', (24, 44), (32, 44))
        self.add_arc('sym-e9-1', (32, 44), (33, 44), radius_x=33, radius_y=33, large_arc=False, sweep=True)
        self.add_arc('sym-e9-2', (33, 44), (34, 44), radius_x=34, radius_y=34, large_arc=False, sweep=True)
        self.add_arc('sym-e10', (34, 44), (35, 44), radius_x=36, radius_y=36, large_arc=False, sweep=True)
        self.add_line('sym-e11', (35, 44), (36, 44))
        self.add_arc('sym-e12', (36, 44), (40, 40), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('sym-e13', (40, 40), (40, 39), radius_x=39, radius_y=39, large_arc=False, sweep=True)
        self.add_line('sym-e14', (40, 39), (40, 19))
        self.add_line('sym-e15', (40, 19), (40, 18))
        self.add_arc('sym-e17', (40, 18), (38, 15), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e18', (38, 15), (28, 6))
        self.add_arc('sym-e19', (28, 6), (24, 4), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_arc('sym-e22', (24, 4), (20, 6), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('sym-e23', (20, 6), (10, 15))
        self.add_arc('sym-e24', (10, 15), (8, 18), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e26', (8, 18), (8, 19))
        self.add_line('sym-e27', (8, 19), (8, 39))
        self.add_contour('sym-c0', *('sym-e0', 'sym-e1'), closed=True)
        self.add_contour('sym-c1', *('sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6-1', 'sym-e6-2', 'sym-e7', 'sym-e8', 'sym-e9-1', 'sym-e9-2', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e26', 'sym-e27'), closed=True)
