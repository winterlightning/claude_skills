from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd52f9e99-f622-424a-9d14-4baa6755de91'
SOURCE_PATH = 'pictographic-primitives/babies/poo poop station waste lid_d52f9e99-f622-424a-9d14-4baa6755de91.svg'
AUTHOR = 'gpt-6'

class PottyWithLid(Solo48):
    icon_id = 'potty-with-lid'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/baby-care"
    aliases = ()
    keywords = ('potty', 'toilet', 'training', 'baby', 'lid', 'seat', 'bathroom', 'toddler')

    # Designed to centerline extremes (2, 2)–(46, 46).
    def build(self) -> None:
        self.add_line('seat-1', (6, 26), (42, 26))
        self.add_arc('seat-2', (42, 26), (42, 34), radius_x=4, radius_y=4, sweep=True)
        self.add_line('seat-3', (42, 34), (6, 34))
        self.add_arc('seat-4', (6, 34), (6, 26), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('seat', 'seat-1', 'seat-2', 'seat-3', 'seat-4', closed=True)
        self.add_line('lid-1', (12, 26), (12, 14))
        self.add_arc('lid-2', (12, 14), (36, 14), radius_x=12, radius_y=12, sweep=True)
        self.add_line('lid-3', (36, 14), (36, 26))
        self.add_contour('lid', 'lid-1', 'lid-2', 'lid-3', closed=False)
        self.add_line('base-1', (6, 34), (2, 46))
        self.add_line('base-2', (2, 46), (16, 46))
        self.add_arc('base-3', (16, 46), (32, 46), radius_x=8, radius_y=8, sweep=True)
        self.add_line('base-4', (32, 46), (46, 46))
        self.add_line('base-5', (46, 46), (42, 34))
        self.add_contour('base', 'base-1', 'base-2', 'base-3', 'base-4', 'base-5', closed=False)
        self.relate("connect", "seat", "lid")
        self.relate("connect", "seat", "base")
