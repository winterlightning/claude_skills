"""Presentation microphone (office), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dc33bff7-8291-5e3a-956d-f632ad5d2bee'
SOURCE_PATH = 'pictographic-primitives/office/presentation microphone_dc33bff7-8291-5e3a-956d-f632ad5d2bee.svg'
AUTHOR = 'gpt-6'

class PresentationMicrophone(Solo48):
    icon_id = 'presentation-microphone'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('presentation', 'microphone', 'office')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (24, 43), (24, 44))
        self.add_line('e1', (17, 44), (31, 44))
        self.add_line('e2', (34, 21), (34, 11))
        self.add_line('e3', (14, 11), (14, 22))
        self.add_arc('e4-1', (40, 30), (24, 43), radius_x=15, radius_y=15, large_arc=False, sweep=True)
        self.add_arc('e4-2', (24, 43), (8, 30), radius_x=15, radius_y=15, large_arc=False, sweep=True)
        self.add_arc('e5-1', (14, 22), (24, 30), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_arc('e5-2', (24, 30), (34, 21), radius_x=9, radius_y=9, large_arc=False, sweep=False)
        self.add_arc('e6-1', (34, 11), (29, 5), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_line('e6-2', (29, 5), (24, 4))
        self.add_line('e6-3', (24, 4), (19, 5))
        self.add_arc('e6-4', (19, 5), (14, 11), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_contour('c0', *('e4-1', 'e4-2'), closed=False)
        self.add_contour('c1', *('e0',), closed=False)
        self.add_contour('c2', *('e1',), closed=False)
        self.add_contour('c3', *('e5-1', 'e5-2', 'e2', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e3'), closed=True)
        self.relate('connect', *('c1', 'c0'))
        self.relate('connect', *('c1', 'c2'))
