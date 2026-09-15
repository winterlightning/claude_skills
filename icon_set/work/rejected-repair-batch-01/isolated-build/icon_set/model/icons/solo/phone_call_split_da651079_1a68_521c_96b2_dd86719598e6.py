"""Phone call split (phones), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'da651079-1a68-521c-96b2-dd86719598e6'
SOURCE_PATH = 'pictographic-primitives/phones/phone call split_da651079-1a68-521c-96b2-dd86719598e6.svg'
AUTHOR = 'gpt-6'

class PhoneCallSplit(Solo48):
    icon_id = 'phone-call-split'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'phones'
    aliases = ()
    keywords = ('phone', 'call', 'split', 'phones')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('sym-e0', (24, 42), (24, 37))
        self.add_arc('sym-e1', (24, 37), (22, 29), radius_x=29, radius_y=29, large_arc=False, sweep=False)
        self.add_arc('sym-e2', (22, 29), (13, 13), radius_x=42, radius_y=42, large_arc=False, sweep=False)
        self.add_arc('sym-e3', (13, 13), (11, 10), radius_x=24, radius_y=24, large_arc=False, sweep=False)
        self.add_line('sym-e4', (11, 10), (6, 6))
        self.add_line('sym-e5', (6, 6), (6, 17))
        self.add_line('sym-e6', (24, 37), (24, 33))
        self.add_line('sym-e7', (6, 6), (16, 6))
        self.add_arc('sym-e8', (24, 37), (26, 29), radius_x=28, radius_y=28, large_arc=False, sweep=True)
        self.add_arc('sym-e9', (26, 29), (35, 13), radius_x=42, radius_y=42, large_arc=False, sweep=True)
        self.add_arc('sym-e10', (35, 13), (37, 10), radius_x=25, radius_y=25, large_arc=False, sweep=True)
        self.add_line('sym-e11', (37, 10), (42, 6))
        self.add_line('sym-e12', (42, 6), (42, 17))
        self.add_line('sym-e13', (42, 6), (32, 6))
        self.add_contour('sym-c0', *('sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5'), closed=False)
        self.add_contour('sym-c1', *('sym-e6',), closed=False)
        self.add_contour('sym-c2', *('sym-e7',), closed=False)
        self.add_contour('sym-c3', *('sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12'), closed=False)
        self.add_contour('sym-c4', *('sym-e13',), closed=False)
        self.relate('connect', *('sym-c0', 'sym-c3'))
        self.relate('connect', *('sym-c0', 'sym-c2'))
        self.relate('connect', *('sym-c3', 'sym-c4'))
