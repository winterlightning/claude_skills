'Bear head with the neck joined to both endpoints of the head contour. HRECT_XL (6,6)-(42,42) preserves the profile. Roaring jaws and eye retained. Deliberate right-facing asymmetry.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3b805db1-6ba6-4ad5-8913-496730af8a1d'
SOURCE_PATH = 'pictographic-primitives/animals/grizzly head side_3b805db1-6ba6-4ad5-8913-496730af8a1d.svg'
AUTHOR = 'gpt-6'

class GrizzlyHeadProfile(Solo48):
    icon_id = 'grizzly-head-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('bear', 'grizzly', 'head', 'profile', 'roar', 'snout', 'wildlife', 'animal')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('head-1', (6, 17), (10, 13))
        self.add_line('head-2', (10, 13), (8, 9))
        self.add_bezier('head-3', (8, 9), *(((8.46706416, 7.18720021), (10.12893424, 6), (12, 6)),))
        self.add_bezier('head-4', (12, 6), *(((14.95947971, 6), (17.50699408, 8.08158004), (18, 11)),))
        self.add_line('head-5', (18, 11), (23, 11))
        self.add_arc('head-6', (23, 11), (35, 17), radius_x=13, radius_y=13, large_arc=False, sweep=True)
        self.add_line('head-7', (35, 17), (42, 22))
        self.add_line('head-8', (42, 22), (42, 28))
        self.add_arc('head-9', (42, 28), (37, 30), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('head-10', (37, 30), (31, 30))
        self.add_arc('head-11', (31, 30), (28, 33), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_arc('head-12', (28, 33), (31, 36), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('head-13', (31, 36), (40, 38))
        self.add_line('head-14', (40, 38), (32, 42))
        self.add_arc('head-15', (32, 42), (23, 40), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_line('head-16', (23, 40), (15, 42))
        self.add_line('eye', (28, 21), (28, 21))
        self.add_line('neck-top', (6, 17), (6, 29))
        self.add_arc('neck-1', (6, 29), (15, 42), radius_x=18, radius_y=18, large_arc=False, sweep=False)
        self.add_contour('head', *('head-1', 'head-2', 'head-3', 'head-4', 'head-5', 'head-6', 'head-7', 'head-8', 'head-9', 'head-10', 'head-11', 'head-12', 'head-13', 'head-14', 'head-15', 'head-16'), closed=False)
        self.add_contour('neck', *('neck-top', 'neck-1'), closed=False)
        self.relate('connect', *('neck', 'head'))
