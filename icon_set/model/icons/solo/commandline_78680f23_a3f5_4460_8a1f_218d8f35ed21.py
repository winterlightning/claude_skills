"""Commandline (programing), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '78680f23-a3f5-4460-8a1f-218d8f35ed21'
SOURCE_PATH = 'pictographic-primitives/programing/commandline_78680f23-a3f5-4460-8a1f-218d8f35ed21.svg'
AUTHOR = 'gpt-6'

class Commandline(Solo48):
    icon_id = 'commandline'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('commandline', 'programing')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (13, 18), (17, 24))
        self.add_line('e1', (17, 24), (13, 29))
        self.add_line('e2', (22, 31), (29, 31))
        self.add_line('e3', (42, 40), (6, 40))
        self.add_line('e4', (4, 38), (4, 11))
        self.add_line('e5', (6, 8), (42, 8))
        self.add_line('e6', (44, 10), (44, 38))
        self.add_arc('e7', (6, 40), (4, 38), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('e8', (4, 11), (6, 8), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('e9', (42, 8), (44, 10), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('e10', (44, 38), (42, 40), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('c0', *('e0', 'e1'), closed=False)
        self.add_contour('c1', *('e2',), closed=False)
        self.add_contour('c2', *('e3', 'e7', 'e4', 'e8', 'e5', 'e9', 'e6', 'e10'), closed=True)
