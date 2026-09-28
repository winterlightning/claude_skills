"""Lock (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ae80ad8e-78ff-4d1d-a60a-d6c106563f5d'
SOURCE_PATH = 'pictographic-primitives/interface-essential/lock_ae80ad8e-78ff-4d1d-a60a-d6c106563f5d.svg'
AUTHOR = 'gpt-6'

class LockAe80ad8e(Solo48):
    icon_id = 'lock-ae80ad8e'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('lock', 'interface-essential')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_arc('sym-e3', (24, 4), (14, 15), radius_x=11, radius_y=11, large_arc=False, sweep=False)
        self.add_line('sym-e4', (14, 15), (14, 20))
        self.add_line('sym-e5', (14, 20), (12, 20))
        self.add_arc('sym-e6', (12, 20), (8, 24), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('sym-e7', (8, 24), (8, 39))
        self.add_line('sym-e10', (8, 39), (8, 41))
        self.add_arc('sym-e11', (8, 41), (12, 44), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('sym-e13', (12, 44), (24, 44))
        self.add_line('sym-e14', (24, 44), (36, 44))
        self.add_arc('sym-e16', (36, 44), (40, 41), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('sym-e17', (40, 41), (40, 39))
        self.add_line('sym-e20', (40, 39), (40, 24))
        self.add_arc('sym-e21', (40, 24), (36, 20), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('sym-e22', (36, 20), (34, 20))
        self.add_line('sym-e23', (34, 20), (34, 15))
        self.add_arc('sym-e24', (34, 15), (24, 4), radius_x=11, radius_y=11, large_arc=False, sweep=False)
        self.add_line('sym-e26', (14, 20), (24, 20))
        self.add_line('sym-e27', (24, 20), (34, 20))
        self.add_contour('sym-c1', *('sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e10', 'sym-e11', 'sym-e13', 'sym-e14', 'sym-e16', 'sym-e17', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24'), closed=True)
        self.add_contour('sym-c2', *('sym-e26', 'sym-e27'), closed=False)
        self.relate('connect', *('sym-c1', 'sym-c2'))
        self.add_line('keyhole',(24,30),(24,34))
