# Review candidate; original preserved.
"""sea-lion: HRECT_XL ink (6,6)-(42,42). Left-facing raised head, sweeping back and splayed flippers."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7188aa8a-305f-404d-bfe3-07ee8f265206'
SOURCE_PATH = 'pictographic-primitives/animals/seal body_7188aa8a-305f-404d-bfe3-07ee8f265206.svg'
AUTHOR = 'gpt-6'

class SeaLionVariant2(Solo48):
    icon_id = 'sea-lion-v2'
    variant_of = 'sea-lion'
    variant_label = 'Roomier openings — pending review'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals/marine'
    aliases = ()
    keywords = ('sea lion', 'seal', 'flippers', 'marine', 'animal', 'ocean', 'zoo', 'whiskers')

    def build(self) -> None:
        """Opening repair: Broadened the rear flipper and removed the crossing at its tip."""
        self.add_arc('body-1', (12, 6), (22, 15), radius_x=10, radius_y=10, sweep=True)
        self.add_line('body-2', (22, 15), (22, 19))
        self.add_line('body-3', (22, 19), (28, 19))
        self.add_arc('body-4', (28, 19), (42, 34), sweep=True, radius_x=18, radius_y=18)
        self.add_line('body-5', (42, 34), (42, 42))
        self.add_arc('body-6', (42, 42), (34, 42), radius_x=8, radius_y=4, sweep=True)
        self.add_line('body-7', (34, 42), (36, 34))
        self.add_line('body-8', (36, 34), (32, 30))
        self.add_arc('body-9', (32, 30), (25, 34), sweep=True, radius_x=20, radius_y=12)
        self.add_line('body-10', (25, 34), (30, 42))
        self.add_arc('body-11', (30, 42), (17, 37), radius_x=13, radius_y=6, sweep=True)
        self.add_line('body-12', (17, 37), (9, 40))
        self.add_line('body-13', (9, 40), (6, 38))
        self.add_arc('body-14', (6, 38), (10, 30), radius_x=12, radius_y=12, sweep=False)
        self.add_arc('body-15', (10, 30), (6, 19), radius_x=18, radius_y=18, sweep=True)
        self.add_arc('body-16', (6, 19), (6, 14), radius_x=3, radius_y=5, sweep=True)
        self.add_arc('body-17', (6, 14), (6, 9), radius_x=4, radius_y=5, sweep=True)
        self.add_arc('body-18', (6, 9), (12, 6), radius_x=7, radius_y=7, sweep=True)
        self.add_contour('body', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', 'body-8', 'body-9', 'body-10', 'body-11', 'body-12', 'body-13', 'body-14', 'body-15', 'body-16', 'body-17', 'body-18', closed=True)
        self.add_line('flipper-1', (17, 29), (17, 37))
        self.add_contour('flipper', 'flipper-1', closed=False)
        self.add_dot('eye', (12, 15))
        self.relate('connect', 'body', 'flipper')
