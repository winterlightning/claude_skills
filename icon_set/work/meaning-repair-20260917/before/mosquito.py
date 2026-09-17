# Review candidate; original preserved.
"""mosquito: reconstructed at native SOLO48 size."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0145bda3-5e60-4e2f-b201-09ab64a9f332'
SOURCE_PATH = 'pictographic-primitives/animals/dragonfly_0145bda3-5e60-4e2f-b201-09ab64a9f332.svg'
AUTHOR = 'gpt-6'

class Mosquito(Solo48):
    icon_id = 'mosquito'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('mosquito', 'insect', 'bug', 'wings', 'pest', 'bite', 'fly', 'antennae')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_arc('head-1', (24, 11), (24, 21), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('head-2', (24, 21), (24, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('proboscis', (24, 6), (24, 11))
        self.add_line('abdomen', (24, 21), (24, 42))
        self.add_arc('leg-left', (12, 10), (7, 6), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_line('wing-left-1', (24, 21), (6, 31))
        self.add_bezier('wing-left-2', (6, 31), *(((6, 34.91328937), (6, 39.51512651), (8, 42)),))
        self.add_line('wing-left-3', (8, 42), (24, 21))
        self.add_arc('leg-right', (36, 10), (41, 6), radius_x=11, radius_y=11, large_arc=False, sweep=False)
        self.add_line('wing-right-1', (24, 21), (42, 31))
        self.add_bezier('wing-right-2', (42, 31), *(((42, 34.91328937), (42, 39.51512651), (40, 42)),))
        self.add_line('wing-right-3', (40, 42), (24, 21))
        self.add_contour('head', *('head-1', 'head-2'), closed=True)
        self.add_contour('wing-left', *('wing-left-1', 'wing-left-2', 'wing-left-3'), closed=True)
        self.add_contour('wing-right', *('wing-right-1', 'wing-right-2', 'wing-right-3'), closed=True)
        self.relate('connect', *('proboscis', 'head'))
        self.relate('connect', *('head', 'abdomen'))
        self.relate('connect', *('wing-left', 'head'))
        self.relate('connect', *('wing-left', 'abdomen'))
        self.relate('connect', *('wing-right', 'head'))
        self.relate('connect', *('wing-right', 'abdomen'))
        self.relate('connect', *('wing-left', 'wing-right'))
