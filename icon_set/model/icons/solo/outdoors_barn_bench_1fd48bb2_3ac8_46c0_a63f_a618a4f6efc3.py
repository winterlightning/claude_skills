'Sheltered bench: straight structural edges and evenly spaced table and seat levels.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1fd48bb2-3ac8-46c0-a63f-a618a4f6efc3'
SOURCE_PATH = 'icons-json/outdoors/outdoors barn bench_1fd48bb2-3ac8-46c0-a63f-a618a4f6efc3.json'
AUTHOR = 'gpt-6'

class OutdoorsBarnBench(Solo48):
    icon_id = 'outdoors-barn-bench'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('outdoors', 'barn', 'bench')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('roof', (6, 18), (42, 6))
        self.add_line('shelter-1', (9, 17), (9, 42))
        self.add_line('shelter-2', (9, 42), (42, 42))
        self.add_line('table', (20, 24), (34, 24))
        self.add_line('bench', (16, 33), (38, 33))
        self.add_line('legs-1', (18, 42), (24, 24))
        self.add_line('legs-2', (24, 24), (30, 24))
        self.add_line('legs-3', (30, 24), (36, 42))
        self.add_contour('shelter', *('shelter-1', 'shelter-2'), closed=False)
        self.add_contour('legs', *('legs-1', 'legs-2', 'legs-3'), closed=False)
        self.relate('connect', *('roof', 'shelter'))
        self.relate('connect', *('legs', 'table'))
        self.relate('connect', *('legs', 'bench'))
        self.relate('connect', *('legs', 'shelter'))
