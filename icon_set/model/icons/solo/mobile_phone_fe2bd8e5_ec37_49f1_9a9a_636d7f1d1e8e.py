"""Mobile phone (mobile), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fe2bd8e5-ec37-49f1-9a9a-636d7f1d1e8e'
SOURCE_PATH = 'pictographic-primitives/mobile/mobile phone_fe2bd8e5-ec37-49f1-9a9a-636d7f1d1e8e.svg'
AUTHOR = 'gpt-6'

class MobilePhoneFe2bd8e5(Solo48):
    icon_id = 'mobile-phone-fe2bd8e5'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'mobile'
    categories = ('mobile', 'primitives')
    aliases = ()
    keywords = ('mobile', 'phone')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('sym-e0', (22, 35), (26, 35))
        self.add_line('sym-e1', (35, 44), (24, 44))
        self.add_line('sym-e2', (24, 44), (13, 44))
        self.add_arc('sym-e4', (13, 44), (8, 40), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('sym-e5', (8, 40), (8, 8))
        self.add_arc('sym-e6', (8, 8), (13, 4), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('sym-e8', (13, 4), (24, 4))
        self.add_line('sym-e9', (24, 4), (35, 4))
        self.add_arc('sym-e11', (35, 4), (40, 8), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('sym-e12', (40, 8), (40, 40))
        self.add_arc('sym-e13', (40, 40), (35, 44), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('sym-c0', *('sym-e0',), closed=False)
        self.add_contour('sym-c1', *('sym-e1', 'sym-e2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e8', 'sym-e9', 'sym-e11', 'sym-e12', 'sym-e13'), closed=True)
