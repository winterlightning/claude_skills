"""A whale tail with broad flukes rising above scalloped waves."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9672a672-8e60-597a-b10e-94e04111186a'
SOURCE_PATH = 'pictographic-primitives/animals/whale tail_9672a672-8e60-597a-b10e-94e04111186a.svg'
AUTHOR = 'gpt-6'


class WhaleTail(Solo48):
    icon_id = 'whale-tail'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('whale', 'tail', 'fluke', 'water', 'waves', 'sea', 'dive', 'ocean')

    def build(self) -> None:
        # Visible keyshape extremes: (0, 0, 48, 48).
        self.add_line("stem-left",(16,34),(18,25))
        self.add_arc("fluke-left-bottom",(18,25),(2,2),radius_x=26,sweep=True)
        self.add_arc("fluke-left-top",(2,2),(24,14),radius_x=28,sweep=False)
        self.add_arc("fluke-right-top",(24,14),(46,2),radius_x=28,sweep=False)
        self.add_arc("fluke-right-bottom",(46,2),(30,25),radius_x=26,sweep=True)
        self.add_line("stem-right",(30,25),(32,34))
        self.add_contour("tail","stem-left","fluke-left-bottom","fluke-left-top","fluke-right-top","fluke-right-bottom","stem-right")
        self.add_arc("wave-left",(2,42),(16,42),radius_x=7,radius_y=4,sweep=False)
        self.add_arc("wave-middle",(16,42),(32,42),radius_x=8,radius_y=4,sweep=False)
        self.add_arc("wave-right",(32,42),(46,42),radius_x=7,radius_y=4,sweep=False)
        self.add_contour("water","wave-left","wave-middle","wave-right")
