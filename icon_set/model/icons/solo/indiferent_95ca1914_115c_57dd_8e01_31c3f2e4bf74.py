"""Indiferent (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '95ca1914-115c-57dd-8e01-31c3f2e4bf74'
SOURCE_PATH = 'pictographic-primitives/smileys/indiferent_95ca1914-115c-57dd-8e01-31c3f2e4bf74.svg'
AUTHOR = 'gpt-6'

class Indiferent(Solo48):
    icon_id = 'indiferent'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('indiferent', 'smileys')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('sym-e0', (16, 32), (32, 32))
        self.add_line('sym-e3-1', (24, 4), (28, 5))
        self.add_arc('sym-e3-2', (28, 5), (43, 19), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('sym-e4-1', (43, 19), (43, 20), radius_x=26, radius_y=26, large_arc=False, sweep=False)
        self.add_arc('sym-e4-2', (43, 20), (43, 21), radius_x=19, radius_y=19, large_arc=False, sweep=False)
        self.add_line('sym-e4-3', (43, 21), (43, 22))
        self.add_line('sym-e4-4', (43, 22), (43, 23))
        self.add_arc('sym-e5', (43, 23), (44, 24), radius_x=23, radius_y=23, large_arc=False, sweep=False)
        self.add_line('sym-e6', (44, 24), (43, 25))
        self.add_line('sym-e7-1', (43, 25), (43, 27))
        self.add_arc('sym-e7-2', (43, 27), (43, 29), radius_x=16, radius_y=16, large_arc=False, sweep=True)
        self.add_arc('sym-e7-3', (43, 29), (24, 44), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('sym-e10-1', (24, 44), (5, 29), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('sym-e10-2', (5, 29), (5, 27), radius_x=17, radius_y=17, large_arc=False, sweep=True)
        self.add_line('sym-e10-3', (5, 27), (5, 25))
        self.add_arc('sym-e11', (5, 25), (4, 24), radius_x=13, radius_y=13, large_arc=False, sweep=False)
        self.add_arc('sym-e12', (4, 24), (5, 23), radius_x=22, radius_y=22, large_arc=False, sweep=False)
        self.add_line('sym-e13-1', (5, 23), (5, 22))
        self.add_arc('sym-e13-2', (5, 22), (5, 21), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_arc('sym-e13-3', (5, 21), (5, 20), radius_x=18, radius_y=18, large_arc=False, sweep=True)
        self.add_arc('sym-e13-4', (5, 20), (5, 19), radius_x=27, radius_y=27, large_arc=False, sweep=True)
        self.add_arc('sym-e14-1', (5, 19), (20, 5), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_line('sym-e14-2', (20, 5), (24, 4))
        self.add_line('sym-e17', (28, 20), (34, 20))
        self.add_line('sym-e18', (20, 20), (14, 20))
        self.add_contour('sym-c0', *('sym-e0',), closed=False)
        self.add_contour('sym-c1', *('sym-e3-1', 'sym-e3-2', 'sym-e4-1', 'sym-e4-2', 'sym-e4-3', 'sym-e4-4', 'sym-e5', 'sym-e6', 'sym-e7-1', 'sym-e7-2', 'sym-e7-3', 'sym-e10-1', 'sym-e10-2', 'sym-e10-3', 'sym-e11', 'sym-e12', 'sym-e13-1', 'sym-e13-2', 'sym-e13-3', 'sym-e13-4', 'sym-e14-1', 'sym-e14-2'), closed=True)
        self.add_contour('sym-c2', *('sym-e17',), closed=False)
        self.add_contour('sym-c3', *('sym-e18',), closed=False)
