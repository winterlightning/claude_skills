"""Synchronize arrows three (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '92f7fa78-def1-430b-a511-f011591c78a6'
SOURCE_PATH = 'icons-json/interface-essential/synchronize arrows three_92f7fa78-def1-430b-a511-f011591c78a6.json'
AUTHOR = 'gpt-6'

class SynchronizeArrowsThree(Solo48):
    icon_id = 'synchronize-arrows-three'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('synchronize', 'arrows', 'three', 'interface-essential')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (16, 6), (14, 12))
        self.add_line('e1', (20, 13), (15, 13))
        self.add_line('e2', (13, 39), (14, 40))
        self.add_line('e3', (8, 41), (14, 40))
        self.add_line('e4', (13, 34), (14, 40))
        self.add_line('e5', (35, 26), (39, 22))
        self.add_line('e6', (42, 26), (39, 22))
        self.add_line('e7', (15, 13), (14, 12))
        self.add_arc('e8', (36, 14), (14, 12), radius_x=16, radius_y=16, large_arc=False, sweep=False)
        self.add_arc('e9-1', (8, 18), (6, 26), radius_x=19, radius_y=19, large_arc=False, sweep=False)
        self.add_arc('e9-2', (6, 26), (13, 39), radius_x=16, radius_y=16, large_arc=False, sweep=False)
        self.add_arc('e11', (23, 42), (39, 22), radius_x=18, radius_y=18, large_arc=False, sweep=False)
        self.add_contour('c0', *('e0',), closed=False)
        self.add_contour('c1', *('e1', 'e7'), closed=False)
        self.add_contour('c2', *('e8',), closed=False)
        self.add_contour('c3', *('e9-1', 'e9-2', 'e2'), closed=False)
        self.add_contour('c4', *('e3',), closed=False)
        self.add_contour('c5', *('e4',), closed=False)
        self.add_contour('c6', *('e5',), closed=False)
        self.add_contour('c7', *('e11',), closed=False)
        self.add_contour('c8', *('e6',), closed=False)
        self.relate('connect', *('c0', 'c1'))
        self.relate('connect', *('c0', 'c2'))
        self.relate('connect', *('c1', 'c2'))
        self.relate('connect', *('c3', 'c4'))
        self.relate('connect', *('c3', 'c5'))
        self.relate('connect', *('c4', 'c5'))
        self.relate('connect', *('c6', 'c7'))
        self.relate('connect', *('c6', 'c8'))
        self.relate('connect', *('c7', 'c8'))
