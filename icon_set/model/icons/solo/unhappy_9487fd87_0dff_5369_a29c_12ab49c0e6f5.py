"""Unhappy (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9487fd87-0dff-5369-a29c-12ab49c0e6f5'
SOURCE_PATH = 'pictographic-primitives/smileys/unhappy_9487fd87-0dff-5369-a29c-12ab49c0e6f5.svg'
AUTHOR = 'gpt-6'

class UnhappySmileys(Solo48):
    icon_id = 'unhappy-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('unhappy', 'smileys')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_arc('sym-e0', (4, 24), (44, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('sym-e1', (44, 24), (4, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('sym-e2', (15, 22), (18, 17), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('sym-e3', (16, 32), (18, 30))
        self.add_arc('sym-e4', (18, 30), (24, 28), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_arc('sym-e5', (24, 28), (30, 30), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_arc('sym-e6', (30, 30), (32, 32), radius_x=17, radius_y=17, large_arc=False, sweep=False)
        self.add_arc('sym-e7', (33, 22), (30, 17), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('sym-c0', *('sym-e0', 'sym-e1'), closed=True)
        self.add_contour('sym-c1', *('sym-e2',), closed=False)
        self.add_contour('sym-c2', *('sym-e3', 'sym-e4', 'sym-e5', 'sym-e6'), closed=False)
        self.add_contour('sym-c3', *('sym-e7',), closed=False)
