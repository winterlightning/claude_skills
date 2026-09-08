"""A baby dinosaur rising out of a cracked egg."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1f496c94-6b6c-4e5e-abaf-34bc8a91c90b'
SOURCE_PATH = 'pictographic-primitives/animals/dinosaur egg hatch_1f496c94-6b6c-4e5e-abaf-34bc8a91c90b.svg'
AUTHOR = 'gpt-6'


class HatchingDinosaurEgg(Solo48):
    icon_id = 'hatching-dinosaur-egg'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('dinosaur', 'egg', 'hatch', 'baby', 'shell', 'prehistoric', 'birth', 'jurassic')

    def build(self) -> None:
        # Centerline extremes: (5,2)-(43,46).
        self.add_arc("shell-bottom",(43,28),(5,28),radius_x=19,radius_y=18)
        self.add_line("crack-1",(5,28),(14,34))
        self.add_line("crack-2",(14,34),(24,26))
        self.add_line("crack-3",(24,26),(33,34))
        self.add_line("crack-4",(33,34),(43,28))
        self.add_contour("shell","shell-bottom",*["crack-"+str(i) for i in range(1,5)],closed=True)
        self.add_line("neck",(33,34),(33,12))
        self.add_arc("skull",(33,12),(23,2),radius_x=10,sweep=False)
        self.add_arc("forehead",(23,2),(13,10),radius_x=10,radius_y=8,sweep=False)
        self.add_line("snout-top",(13,10),(11,10))
        self.add_arc("snout",(11,10),(11,22),radius_x=6,sweep=False)
        self.add_line("jaw-1",(11,22),(21,22))
        self.add_line("jaw-2",(21,22),(21,28))
        self.add_contour("hatchling","neck","skull","forehead","snout-top","snout","jaw-1","jaw-2")
        self.relate("connect","hatchling","shell")
        self.add_dot("eye",(24,12))
