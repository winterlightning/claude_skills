"""platypus: reconstructed at native SOLO48 size."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd9e4bd26-488d-456c-8a81-23be0e9dd789'
SOURCE_PATH = 'pictographic-primitives/animals/duck bill platypus_d9e4bd26-488d-456c-8a81-23be0e9dd789.svg'
AUTHOR = 'gpt-6'


class Platypus(Solo48):
    icon_id = 'platypus'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('platypus', 'duckbill', 'australia', 'mammal', 'monotreme', 'animal', 'wildlife', 'aquatic')

    def build(self):
        self.add_arc('tail-1', (18, 20), (16, 14), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('tail-2', (16, 14), (29, 2), radius_x=16, radius_y=12, sweep=True)
        self.add_arc('tail-3', (29, 2), (36, 9), radius_x=7, radius_y=7, sweep=True)
        self.add_line('tail-4', (36, 9), (27, 16))
        self.add_line('tail-5', (27, 16), (27, 20))
        self.add_contour('tail', 'tail-1', 'tail-2', 'tail-3', 'tail-4', 'tail-5', closed=False)
        self.add_arc('body-1', (18, 20), (12, 29), radius_x=6, radius_y=9, sweep=False)
        self.add_arc('body-2', (12, 29), (18, 38), radius_x=6, radius_y=9, sweep=False)
        self.add_line('body-3', (18, 38), (28, 38))
        self.add_arc('body-4', (28, 38), (34, 29), radius_x=6, radius_y=9, sweep=False)
        self.add_arc('body-5', (34, 29), (27, 20), radius_x=7, radius_y=9, sweep=False)
        self.add_line('body-6', (27, 20), (18, 20))
        self.add_contour('body', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', closed=True)
        self.relate("connect", 'tail', 'body')
        self.add_line('bill-1', (18, 38), (28, 38))
        self.add_arc('bill-2', (28, 38), (28, 46), radius_x=5, radius_y=4, sweep=True)
        self.add_line('bill-3', (28, 46), (18, 46))
        self.add_arc('bill-4', (18, 46), (18, 38), radius_x=5, radius_y=4, sweep=True)
        self.add_contour('bill', 'bill-1', 'bill-2', 'bill-3', 'bill-4', closed=True)
        self.relate("connect", 'bill', 'body')
        self.add_line('left-foreleg', (12, 29), (8, 24))
        self.relate("connect", 'left-foreleg', 'body')
        self.add_line('right-foreleg', (34, 29), (40, 24))
        self.relate("connect", 'right-foreleg', 'body')
        self.add_line('left-hindleg', (18, 38), (8, 38))
        self.relate("connect", 'left-hindleg', 'body')
        self.relate("connect", 'left-hindleg', 'bill')
        self.add_line('right-hindleg', (28, 38), (40, 38))
        self.relate("connect", 'right-hindleg', 'body')
        self.relate("connect", 'right-hindleg', 'bill')
