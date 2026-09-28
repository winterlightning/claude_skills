'Fossil tablet: a clear fossil silhouette inside a smooth balanced stone frame.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ac47ac3a-e57f-5b00-8f8a-5ae0e9fb9419'
SOURCE_PATH = 'pictographic-primitives/animals/dinosaur pteranodon fossil_ac47ac3a-e57f-5b00-8f8a-5ae0e9fb9419.svg'
AUTHOR = 'gpt-6'


class FossilTablet(Solo48):
    icon_id = 'fossil-tablet'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    categories = ("animals", "primitives")
    aliases = ()
    keywords = ('fossil', 'dinosaur', 'skeleton', 'pterosaur', 'stone', 'tablet', 'archaeology', 'prehistoric')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('tablet-0', (10, 6), (38, 6))
        self.add_arc('tablet-1', (38, 6), (42, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('tablet-2', (42, 10), (42, 38))
        self.add_arc('tablet-3', (42, 38), (38, 42), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('tablet-4', (38, 42), (10, 42))
        self.add_arc('tablet-5', (10, 42), (6, 38), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('tablet-6', (6, 38), (6, 10))
        self.add_arc('tablet-7', (6, 10), (10, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('fossil-1', (15, 31), (15, 23))
        self.add_line('fossil-2', (15, 23), (30, 18))
        self.add_line('fossil-3', (30, 18), (33, 29))
        self.add_line('spine-1', (26, 15), (23, 22))
        self.add_line('spine-2', (23, 22), (29, 30))
        self.add_line('spine-3', (29, 30), (26, 33))
        self.add_contour('tablet', *('tablet-0', 'tablet-1', 'tablet-2', 'tablet-3', 'tablet-4', 'tablet-5', 'tablet-6', 'tablet-7'), closed=True)
        self.add_contour('fossil', *('fossil-1', 'fossil-2', 'fossil-3'), closed=False)
        self.add_contour('spine', *('spine-1', 'spine-2', 'spine-3'), closed=False)
        self.relate('connect', *('spine', 'fossil'))
