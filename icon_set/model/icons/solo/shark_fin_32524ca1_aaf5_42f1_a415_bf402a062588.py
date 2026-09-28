'Shark fin: smooth swept fin above two broad waves; exact HRECT_L envelope and clear water gap.'
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
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('shark', 'fin', 'sea', 'ocean', 'danger', 'water', 'swimming', 'predator')

    def build(self) -> None:
        self.add_bezier('front',(6,25),((11,16),(20,8),(30,8)))
        self.add_bezier('rear',(30,8),((30,17),(35,23),(44,25)))
        self.add_contour('fin','front','rear')
        self.add_arc('water-left',(4,36),(24,36),radius_x=10,radius_y=4,sweep=False)
        self.add_arc('water-right',(24,36),(44,36),radius_x=10,radius_y=4,sweep=False)
        self.add_contour('water','water-left','water-right')
