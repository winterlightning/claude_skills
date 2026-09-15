'Two buildings: consistent verticals, an 8-unit doorway and aligned foundation.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2377450f-7d02-5301-a252-bf36ac99587f'
SOURCE_PATH = 'pictographic-primitives/office/building double_2377450f-7d02-5301-a252-bf36ac99587f.svg'
AUTHOR = 'gpt-6'

class BuildingDouble(Solo48):
    icon_id = 'building-double'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('building', 'double', 'office')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('main-1', (6, 42), (6, 6))
        self.add_line('main-2', (6, 6), (30, 6))
        self.add_line('main-3', (30, 6), (30, 42))
        self.add_line('main-4', (30, 42), (6, 42))
        self.add_line('annex-1', (30, 22), (42, 22))
        self.add_line('annex-2', (42, 22), (42, 42))
        self.add_line('annex-3', (42, 42), (30, 42))
        self.add_line('window-14', (14, 14), (14, 18))
        self.add_line('window-22', (22, 14), (22, 18))
        self.add_line('door-1', (14, 42), (14, 30))
        self.add_line('door-2', (14, 30), (22, 30))
        self.add_line('door-3', (22, 30), (22, 42))
        self.add_contour('main', *('main-1', 'main-2', 'main-3', 'main-4'), closed=False)
        self.add_contour('annex', *('annex-1', 'annex-2', 'annex-3'), closed=False)
        self.add_contour('door', *('door-1', 'door-2', 'door-3'), closed=False)
        self.relate('connect', *('annex', 'main'))
        self.relate('connect', *('door', 'main'))
