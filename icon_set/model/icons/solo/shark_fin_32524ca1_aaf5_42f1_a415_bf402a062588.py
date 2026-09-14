"""Curved dorsal fin above two water swells. No useful local Lucide shark or waves match; broad coherent arcs preserve the naturally asymmetric fin.

SOLO48 HRECT_L; live visible envelope (2, 6, 46, 42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '32524ca1-aaf5-42f1-a415-bf402a062588'
SOURCE_PATH = 'pictographic-primitives/symbol/shark tail_32524ca1-aaf5-42f1-a415-bf402a062588.svg'
AUTHOR = 'gpt-6'


class SharkFin(Solo48):
    icon_id = 'shark-fin'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('shark', 'fin', 'sea', 'ocean', 'danger', 'water', 'swimming', 'predator')

    def build(self) -> None:

        self.add_arc('fin-front',(8,25),(30,8),radius_x=30)
        self.add_arc('fin-rear',(30,8),(42,25),radius_x=17,sweep=False)
        self.add_contour('fin','fin-front','fin-rear')
        self.add_arc('water-left',(6,34),(24,34),radius_x=10,radius_y=6,sweep=False)
        self.add_arc('water-right',(24,34),(42,34),radius_x=10,radius_y=6,sweep=False)
        self.add_contour('water','water-left','water-right')
