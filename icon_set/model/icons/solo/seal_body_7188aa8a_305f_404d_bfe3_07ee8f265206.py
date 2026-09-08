"""sea-lion: HRECT_XL ink (0,3)-(48,45). Left-facing raised head, sweeping back and splayed flippers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7188aa8a-305f-404d-bfe3-07ee8f265206'
SOURCE_PATH = 'pictographic-primitives/animals/seal body_7188aa8a-305f-404d-bfe3-07ee8f265206.svg'
AUTHOR = 'gpt-6'


class SeaLion(Solo48):
    icon_id = 'sea-lion'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/marine"
    aliases = ()
    keywords = ('sea lion', 'seal', 'flippers', 'marine', 'animal', 'ocean', 'zoo', 'whiskers')

    def build(self) -> None:
        self.add_arc('body-1', (12, 5), (22, 15), radius_x=10, radius_y=10, sweep=True)
        self.add_line('body-2', (22, 15), (22, 19))
        self.add_line('body-3', (22, 19), (28, 19))
        self.add_arc('body-4', (28, 19), (46, 37), radius_x=18, radius_y=18, sweep=True)
        self.add_line('body-5', (46, 37), (46, 39))
        self.add_arc('body-6', (46, 39), (38, 43), radius_x=8, radius_y=4, sweep=False)
        self.add_line('body-7', (38, 43), (41, 35))
        self.add_line('body-8', (41, 35), (36, 30))
        self.add_arc('body-9', (36, 30), (25, 34), radius_x=20, radius_y=12, sweep=True)
        self.add_line('body-10', (25, 34), (30, 43))
        self.add_arc('body-11', (30, 43), (17, 37), radius_x=13, radius_y=6, sweep=True)
        self.add_line('body-12', (17, 37), (9, 40))
        self.add_line('body-13', (9, 40), (3, 38))
        self.add_arc('body-14', (3, 38), (10, 30), radius_x=12, radius_y=12, sweep=False)
        self.add_arc('body-15', (10, 30), (5, 19), radius_x=18, radius_y=18, sweep=True)
        self.add_arc('body-16', (5, 19), (2, 14), radius_x=3, radius_y=5, sweep=True)
        self.add_arc('body-17', (2, 14), (6, 9), radius_x=4, radius_y=5, sweep=True)
        self.add_arc('body-18', (6, 9), (12, 5), radius_x=7, radius_y=7, sweep=True)
        self.add_contour('body', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', 'body-8', 'body-9', 'body-10', 'body-11', 'body-12', 'body-13', 'body-14', 'body-15', 'body-16', 'body-17', 'body-18', closed=True)
        self.add_line('flipper-1', (17, 29), (17, 37))
        self.add_contour('flipper', 'flipper-1', closed=False)
        self.add_dot('eye', (12, 15))
        self.relate("connect", 'body', 'flipper')
