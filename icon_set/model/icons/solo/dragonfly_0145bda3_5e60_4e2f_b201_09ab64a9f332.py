"""mosquito: reconstructed at native SOLO48 size."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0145bda3-5e60-4e2f-b201-09ab64a9f332'
SOURCE_PATH = 'pictographic-primitives/animals/dragonfly_0145bda3-5e60-4e2f-b201-09ab64a9f332.svg'
AUTHOR = 'gpt-6'


class Mosquito(Solo48):
    icon_id = 'mosquito'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('mosquito', 'insect', 'bug', 'wings', 'pest', 'bite', 'fly', 'antennae')

    def build(self):
        self.add_arc('head-1', (24, 11), (24, 21), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('head-2', (24, 21), (24, 11), radius_x=5, radius_y=5, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', closed=True)
        self.add_line('proboscis', (24, 2), (24, 11))
        self.relate("connect", 'proboscis', 'head')
        self.add_line('abdomen', (24, 21), (24, 46))
        self.relate("connect", 'head', 'abdomen')
        self.add_arc('leg-left', (13, 10), (4, 2), radius_x=13, radius_y=13, sweep=True)
        self.add_line('wing-left-1', (24, 21), (2, 31))
        self.add_arc('wing-left-2', (2, 31), (8, 38), radius_x=6, radius_y=7, sweep=False)
        self.add_line('wing-left-3', (8, 38), (24, 21))
        self.add_contour('wing-left', 'wing-left-1', 'wing-left-2', 'wing-left-3', closed=True)
        self.relate("connect", 'wing-left', 'head')
        self.relate("connect", 'wing-left', 'abdomen')
        self.add_arc('leg-right', (35, 10), (44, 2), radius_x=13, radius_y=13, sweep=False)
        self.add_line('wing-right-1', (24, 21), (46, 31))
        self.add_arc('wing-right-2', (46, 31), (40, 38), radius_x=6, radius_y=7, sweep=True)
        self.add_line('wing-right-3', (40, 38), (24, 21))
        self.add_contour('wing-right', 'wing-right-1', 'wing-right-2', 'wing-right-3', closed=True)
        self.relate("connect", 'wing-right', 'head')
        self.relate("connect", 'wing-right', 'abdomen')
        self.relate("connect", 'wing-left', 'wing-right')
