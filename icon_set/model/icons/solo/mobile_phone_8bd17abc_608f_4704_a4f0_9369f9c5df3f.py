"""Mobile phone (mobile), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8bd17abc-608f-4704-a4f0-9369f9c5df3f'
SOURCE_PATH = 'icons-json/mobile/mobile phone_8bd17abc-608f-4704-a4f0-9369f9c5df3f.json'
AUTHOR = 'gpt-6'

class MobilePhone(Solo48):
    icon_id = 'mobile-phone'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'mobile'
    aliases = ()
    keywords = ('mobile', 'phone')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('sym-e0', (8, 36), (40, 36))
        self.add_line('sym-e1', (40, 36), (40, 40))
        self.add_arc('sym-e2', (40, 40), (35, 44), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('sym-e3', (35, 44), (24, 44))
        self.add_line('sym-e4', (24, 44), (13, 44))
        self.add_arc('sym-e5', (13, 44), (8, 40), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('sym-e6', (8, 40), (8, 36))
        self.add_line('sym-e7', (8, 36), (8, 8))
        self.add_arc('sym-e8', (8, 8), (13, 4), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('sym-e11', (13, 4), (24, 4))
        self.add_line('sym-e12', (24, 4), (35, 4))
        self.add_arc('sym-e15', (35, 4), (40, 8), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('sym-e16', (40, 8), (40, 36))
        self.add_line('sym-e17', (24, 13), (24, 13))
        self.add_contour('sym-c0', *('sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e11', 'sym-e12', 'sym-e15', 'sym-e16'), closed=False)
        self.add_contour('sym-c1', *('sym-e17',), closed=True)
