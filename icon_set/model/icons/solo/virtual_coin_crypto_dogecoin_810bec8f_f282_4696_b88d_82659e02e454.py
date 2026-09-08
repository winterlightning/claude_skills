"""A Shiba Inu face with upright pointed ears and a smiling muzzle."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '810bec8f-f282-4696-b88d-82659e02e454'
SOURCE_PATH = 'pictographic-primitives/animals/virtual coin crypto dogecoin_810bec8f-f282-4696-b88d-82659e02e454.svg'
AUTHOR = 'gpt-6'


class ShibaInuFace(Solo48):
    icon_id = 'shiba-inu-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('dog', 'shiba inu', 'doge', 'face', 'head', 'pet', 'canine', 'breed')

    def build(self) -> None:
        # Visible keyshape extremes: (0, 0, 48, 48).
        self.add_line('ear-left-1', (4, 20), (4, 2))
        self.add_line('ear-left-2', (4, 2), (16, 10))
        self.add_arc("forehead",(16,10),(32,10),radius_x=26)
        self.add_line('ear-right-1', (32, 10), (44, 2))
        self.add_line('ear-right-2', (44, 2), (44, 20))
        self.add_arc("cheek-right",(44,20),(46,26),radius_x=10)
        self.add_arc("chin-right",(46,26),(24,46),radius_x=22,radius_y=20)
        self.add_arc("chin-left",(24,46),(2,26),radius_x=22,radius_y=20)
        self.add_arc("cheek-left",(2,26),(4,20),radius_x=10)
        self.add_contour("head","ear-left-1","ear-left-2","forehead","ear-right-1","ear-right-2","cheek-right","chin-right","chin-left","cheek-left",closed=True)
        self.add_dot("eye-left",(14,22))
        self.add_dot("eye-right",(34,22))
        self.add_line("nose",(22,28),(26,28))
        self.add_arc("smile-left",(16,35),(24,35),radius_x=5,sweep=False)
        self.add_arc("smile-right",(24,35),(32,35),radius_x=5,sweep=False)
        self.add_contour("smile","smile-left","smile-right")
