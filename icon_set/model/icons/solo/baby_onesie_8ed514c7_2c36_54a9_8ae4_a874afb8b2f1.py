from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8ed514c7-2c36-54a9-8ae4-a874afb8b2f1'
SOURCE_PATH = 'pictographic-primitives/babies/baby care clothes_8ed514c7-2c36-54a9-8ae4-a874afb8b2f1.svg'
AUTHOR = 'gpt-6'

class BabyOnesie(Solo48):
    icon_id = 'baby-onesie'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/baby-care"
    aliases = ()
    keywords = ('onesie', 'bodysuit', 'baby', 'clothes', 'romper', 'garment', 'infant', 'laundry')

    # Designed to centerline extremes (2, 2)–(46, 46).
    def build(self) -> None:
        self.add_line('suit-1', (16, 2), (8, 5))
        self.add_line('suit-2', (8, 5), (2, 16))
        self.add_line('suit-3', (2, 16), (10, 20))
        self.add_line('suit-4', (10, 20), (12, 16))
        self.add_line('suit-5', (12, 16), (12, 32))
        self.add_arc('suit-6', (12, 32), (20, 40), radius_x=8, radius_y=8, sweep=True)
        self.add_line('suit-7', (20, 40), (20, 46))
        self.add_line('suit-8', (20, 46), (28, 46))
        self.add_line('suit-9', (28, 46), (28, 40))
        self.add_arc('suit-10', (28, 40), (36, 32), radius_x=8, radius_y=8, sweep=True)
        self.add_line('suit-11', (36, 32), (36, 16))
        self.add_line('suit-12', (36, 16), (38, 20))
        self.add_line('suit-13', (38, 20), (46, 16))
        self.add_line('suit-14', (46, 16), (40, 5))
        self.add_line('suit-15', (40, 5), (32, 2))
        self.add_arc('suit-16', (32, 2), (16, 2), radius_x=8, radius_y=8, sweep=True)
        self.add_contour('suit', 'suit-1', 'suit-2', 'suit-3', 'suit-4', 'suit-5', 'suit-6', 'suit-7', 'suit-8', 'suit-9', 'suit-10', 'suit-11', 'suit-12', 'suit-13', 'suit-14', 'suit-15', 'suit-16', closed=True)
