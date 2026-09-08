"""birds-in-nest: source silhouette re-authored on SOLO48.

Lucide bird informs coherent body arcs and sparse detail.
Keyshape HRECT_L; extremes obtained from the SOLO48 contract.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '86f74b9e-984f-4e95-959a-f8f27b3d1de8'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird nest_86f74b9e-984f-4e95-959a-f8f27b3d1de8.svg'
AUTHOR = 'gpt-6'


class BirdsInNest(Solo48):
    icon_id = 'birds-in-nest'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/birds"
    aliases = ()
    keywords = ('nest', 'birds', 'chicks', 'baby', 'hatchling', 'nurture', 'home', 'family')

    def build(self) -> None:
        self.add_arc('bowl', (46, 27), (2, 27), radius_x=22, radius_y=13, sweep=True)
        self.add_line('rim-a', (2, 27), (6, 27))
        self.add_line('rim-b', (6, 27), (20, 27))
        self.add_line('rim-c', (20, 27), (28, 27))
        self.add_line('rim-d', (28, 27), (42, 27))
        self.add_line('rim-e', (42, 27), (46, 27))
        self.add_contour('nest', 'rim-a', 'rim-b', 'rim-c', 'rim-d', 'rim-e', 'bowl', closed=True)
        self.add_line('chick-left-a', (6, 27), (6, 15))
        self.add_arc('chick-left-head', (6, 15), (20, 15), radius_x=7, radius_y=7, sweep=True)
        self.add_line('chick-left-b', (20, 15), (20, 27))
        self.add_contour('chick-left', 'chick-left-a', 'chick-left-head', 'chick-left-b', closed=False)
        self.add_line('chick-right-a', (28, 27), (28, 15))
        self.add_arc('chick-right-head', (28, 15), (42, 15), radius_x=7, radius_y=7, sweep=True)
        self.add_line('chick-right-b', (42, 15), (42, 27))
        self.add_contour('chick-right', 'chick-right-a', 'chick-right-head', 'chick-right-b', closed=False)
        self.relate("connect", 'chick-left', 'nest')
        self.relate("connect", 'chick-right', 'nest')
        self.add_line('beak-left', (6, 15), (2, 17))
        self.add_line('beak-right', (42, 15), (46, 17))
        self.relate("connect", 'chick-left', 'beak-left')
        self.relate("connect", 'chick-right', 'beak-right')
        self.add_dot('eye-left', (13, 15))
        self.add_dot('eye-right', (35, 15))
