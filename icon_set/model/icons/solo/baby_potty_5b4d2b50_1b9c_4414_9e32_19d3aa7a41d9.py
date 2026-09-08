from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5b4d2b50-1b9c-4414-9e32-19d3aa7a41d9'
SOURCE_PATH = 'pictographic-primitives/babies/urinal baby_5b4d2b50-1b9c-4414-9e32-19d3aa7a41d9.svg'
AUTHOR = 'gpt-6'

class BabyPotty(Solo48):
    icon_id = 'baby-potty'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/baby-care"
    aliases = ()
    keywords = ('potty', 'toilet', 'training', 'baby', 'toddler', 'bathroom', 'pot', 'hygiene')

    # Designed to centerline extremes (2, 5)–(46, 43).
    def build(self) -> None:
        self.add_arc('tub-1', (4, 22), (21, 5), radius_x=17, radius_y=17, sweep=True)
        self.add_arc('tub-2', (21, 5), (36, 12), radius_x=20, radius_y=20, sweep=True)
        self.add_line('tub-3', (36, 12), (44, 18))
        self.add_line('tub-4', (44, 18), (46, 34))
        self.add_arc('tub-5', (46, 34), (2, 34), radius_x=22, radius_y=9, sweep=True)
        self.add_line('tub-6', (2, 34), (4, 22))
        self.add_contour('tub', 'tub-1', 'tub-2', 'tub-3', 'tub-4', 'tub-5', 'tub-6', closed=True)
        self.add_arc('rim-1', (4, 22), (36, 22), radius_x=16, radius_y=6, sweep=True)
        self.add_arc('rim-2', (36, 22), (4, 22), radius_x=16, radius_y=6, sweep=True)
        self.add_contour('rim', 'rim-1', 'rim-2', closed=True)
        self.relate("connect", "tub", "rim")
