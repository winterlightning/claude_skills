"""Mobile phone (phones), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '70454eff-c88b-47e2-b376-ad91c78c22f0'
SOURCE_PATH = 'icons-json/phones/mobile phone_70454eff-c88b-47e2-b376-ad91c78c22f0.json'
AUTHOR = 'gpt-6'

class MobilePhone70454eff(Solo48):
    icon_id = 'mobile-phone-70454eff'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'phones'
    aliases = ()
    keywords = ('mobile', 'phone', 'phones')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('sym-e0', (8, 36), (40, 36))
        self.add_line('sym-e1', (40, 36), (40, 7))
        self.add_arc('sym-e2-1', (40, 7), (39, 5), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_arc('sym-e2-2', (39, 5), (36, 4), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('sym-e3', (36, 4), (24, 4))
        self.add_line('sym-e4', (24, 4), (12, 4))
        self.add_arc('sym-e5-1', (12, 4), (9, 5), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_arc('sym-e5-2', (9, 5), (8, 7), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('sym-e6', (8, 7), (8, 36))
        self.add_line('sym-e7', (8, 36), (8, 38))
        self.add_line('sym-e8', (8, 38), (8, 40))
        self.add_line('sym-e9-1', (8, 40), (9, 43))
        self.add_line('sym-e9-2', (9, 43), (11, 44))
        self.add_arc('sym-e11', (11, 44), (12, 44), radius_x=24, radius_y=24, large_arc=False, sweep=True)
        self.add_line('sym-e12', (12, 44), (24, 44))
        self.add_line('sym-e13', (24, 44), (36, 44))
        self.add_line('sym-e14', (36, 44), (37, 44))
        self.add_line('sym-e16-1', (37, 44), (39, 43))
        self.add_line('sym-e16-2', (39, 43), (40, 40))
        self.add_arc('sym-e17-1', (40, 40), (40, 39), radius_x=39, radius_y=39, large_arc=False, sweep=True)
        self.add_arc('sym-e17-2', (40, 39), (40, 38), radius_x=39, radius_y=39, large_arc=False, sweep=True)
        self.add_line('sym-e18', (40, 38), (40, 36))
        self.add_line('sym-e19', (20, 13), (28, 13))
        self.add_contour('sym-c0', *('sym-e0', 'sym-e1', 'sym-e2-1', 'sym-e2-2', 'sym-e3', 'sym-e4', 'sym-e5-1', 'sym-e5-2', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9-1', 'sym-e9-2', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e16-1', 'sym-e16-2', 'sym-e17-1', 'sym-e17-2', 'sym-e18'), closed=False)
        self.add_contour('sym-c1', *('sym-e19',), closed=False)
