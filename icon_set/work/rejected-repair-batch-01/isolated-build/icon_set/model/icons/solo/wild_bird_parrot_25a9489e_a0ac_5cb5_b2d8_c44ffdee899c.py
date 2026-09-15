"""toucan: source silhouette re-authored on SOLO48.

Lucide bird informs coherent body arcs and sparse detail.
Keyshape SQUARE; extremes obtained from the SOLO48 contract.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '25a9489e-a0ac-5cb5-b2d8-c44ffdee899c'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird parrot_25a9489e-a0ac-5cb5-b2d8-c44ffdee899c.svg'
AUTHOR = 'gpt-6'


class Toucan(Solo48):
    icon_id = 'toucan'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/birds"
    aliases = ()
    keywords = ('toucan', 'bird', 'beak', 'tropical', 'rainforest', 'perch', 'parrot', 'exotic')

    def build(self) -> None:
        self.add_arc('head', (6, 24), (20, 6), radius_x=18, radius_y=22, sweep=True)
        self.add_arc('bill-top', (20, 6), (42, 18), radius_x=26, radius_y=16, sweep=True)
        self.add_line('bill-bottom', (42, 18), (23, 18))
        self.add_line('throat', (23, 18), (25, 29))
        self.add_arc('belly', (25, 29), (14, 40), radius_x=11, radius_y=11, sweep=True)
        self.add_line('tail', (14, 40), (6, 42))
        self.add_line('back-low', (6, 42), (6, 40))
        self.add_line('back-high', (6, 40), (6, 24))
        self.add_contour('outline', 'head', 'bill-top', 'bill-bottom', 'throat', 'belly', 'tail', 'back-low', 'back-high', closed=True)
        self.add_line('bill-root', (20, 6), (23, 18))
        self.relate("connect", 'outline', 'bill-root')
        self.add_dot('eye',(15,22))
        self.add_line('foot', (14, 40), (17, 42))
        self.relate("connect", 'outline', 'foot')
