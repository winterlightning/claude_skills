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
    category = "animals"
    categories = ("animals", "primitives")
    aliases = ()
    keywords = ('dog', 'shiba inu', 'doge', 'face', 'head', 'pet', 'canine', 'breed')

    def build(self) -> None:
        # Visible keyshape extremes: (0, 0, 48, 48).
        self.add_line('ear-left-1', (6, 20), (6, 6))
        self.add_line('ear-left-2', (6, 6), (16, 10))
        self.add_arc("forehead",(16,10),(32,10),radius_x=26)
        self.add_line('ear-right-1', (32, 10), (42, 6))
        self.add_line('ear-right-2', (42, 6), (42, 20))
        self.add_bezier('cheek-right', (42, 20), *(((42, 21.9528534), (42, 24.0471466), (42, 26)),))
        self.add_arc("chin-right",(42,26),(24,42),radius_x=22,radius_y=20)
        self.add_arc("chin-left",(24,42),(6,26),radius_x=22,radius_y=20)
        self.add_bezier('cheek-left', (6, 26), *(((6, 24.0471466), (6, 21.9528534), (6, 20)),))
        self.add_contour("head","ear-left-1","ear-left-2","forehead","ear-right-1","ear-right-2","cheek-right","chin-right","chin-left","cheek-left",closed=True)
        self.add_dot('eye-left',(16,21))
        self.add_dot('eye-right',(32,21))
        self.add_bezier('muzzle',(19,30),((20,33),(23,33),(24,30)),((25,33),(28,33),(29,30)))
