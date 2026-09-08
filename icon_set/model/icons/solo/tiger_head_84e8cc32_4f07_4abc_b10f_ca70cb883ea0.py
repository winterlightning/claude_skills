"""A right-facing sabre-tooth cat head with an open jaw and long fang."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '84e8cc32-4f07-4abc-b10f-ca70cb883ea0'
SOURCE_PATH = 'pictographic-primitives/animals/tiger head_84e8cc32-4f07-4abc-b10f-ca70cb883ea0.svg'
AUTHOR = 'gpt-6'


class SabreToothHead(Solo48):
    icon_id = 'sabre-tooth-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('sabre tooth', 'tiger', 'fang', 'head', 'profile', 'prehistoric', 'big cat', 'extinct')

    def build(self) -> None:
        # Visible keyshape extremes: (0, 0, 48, 48).
        self.add_line("skull", (2,20), (32,7))
        self.add_arc("ear", (32,7), (42,7), radius_x=5)
        self.add_arc("cheek", (46,20), (36,38), radius_x=10, radius_y=18)
        self.add_arc("jaw", (36,38), (16,36), radius_x=20, sweep=False)
        self.add_line("lower-jaw", (16,36), (20,46))
        self.add_arc("fang-outer", (20,46), (10,30), radius_x=20)
        self.add_line("muzzle", (10,30), (6,32))
        self.add_arc("nose", (6,32), (2,28), radius_x=4)
        self.add_line("nose-front", (2,28), (2,20))
        self.add_contour("head", "cheek", "jaw", "lower-jaw", "fang-outer", "muzzle", "nose", "nose-front", "skull", "ear")
        self.add_arc("upper-jaw", (10,30), (26,26), radius_x=24)
        self.relate("connect", "head", "upper-jaw")
        self.add_dot("eye", (30,18))
