from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '145df94c-38fe-4a63-b878-f9b0d6c352db'
SOURCE_PATH = 'pictographic-primitives/babies/poo poop station waste_145df94c-38fe-4a63-b878-f9b0d6c352db.svg'
AUTHOR = 'gpt-6'

class PottyWithSteam(Solo48):
    icon_id = 'potty-with-steam'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/baby-care"
    aliases = ()
    keywords = ('potty', 'toilet', 'poop', 'steam', 'smell', 'training', 'baby', 'bathroom')

    # Designed to centerline extremes (2, 2)–(46, 46).
    def build(self) -> None:
        self.add_line('pot-1', (2, 46), (4, 24))
        self.add_arc('pot-2', (4, 24), (8, 24), radius_x=2, radius_y=2, sweep=True)
        self.add_arc('pot-3', (8, 24), (18, 32), radius_x=10, radius_y=10, sweep=False)
        self.add_line('pot-4', (18, 32), (30, 32))
        self.add_arc('pot-5', (30, 32), (40, 22), radius_x=10, radius_y=10, sweep=False)
        self.add_line('pot-6', (40, 22), (40, 18))
        self.add_arc('pot-7', (40, 18), (44, 18), radius_x=2, radius_y=2, sweep=True)
        self.add_line('pot-8', (44, 18), (46, 46))
        self.add_line('pot-9', (46, 46), (36, 46))
        self.add_arc('pot-10', (36, 46), (12, 46), radius_x=15, radius_y=10, sweep=False)
        self.add_line('pot-11', (12, 46), (2, 46))
        self.add_contour('pot', 'pot-1', 'pot-2', 'pot-3', 'pot-4', 'pot-5', 'pot-6', 'pot-7', 'pot-8', 'pot-9', 'pot-10', 'pot-11', closed=True)
        self.add_arc('steam-left-1', (17, 2), (17, 10), radius_x=7, radius_y=7, sweep=True)
        self.add_arc('steam-left-2', (17, 10), (17, 18), radius_x=7, radius_y=7, sweep=False)
        self.add_contour('steam-left', 'steam-left-1', 'steam-left-2', closed=False)
        self.add_arc('steam-right-1', (28, 5), (28, 13), radius_x=7, radius_y=7, sweep=True)
        self.add_arc('steam-right-2', (28, 13), (28, 21), radius_x=7, radius_y=7, sweep=False)
        self.add_contour('steam-right', 'steam-right-1', 'steam-right-2', closed=False)
