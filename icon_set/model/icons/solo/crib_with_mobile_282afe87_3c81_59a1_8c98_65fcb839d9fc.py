'Crib mobile: equal toy spacing and a regular crib rail, with clear gaps around the suspended toys.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '282afe87-3c81-59a1-8c98-65fcb839d9fc'
SOURCE_PATH = 'pictographic-primitives/babies/baby care cot mobile crib_282afe87-3c81-59a1-8c98-65fcb839d9fc.svg'
AUTHOR = 'gpt-6'


class CribWithMobile(Solo48):
    icon_id = 'crib-with-mobile'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "babies"
    categories = ("babies", "primitives")
    aliases = ()
    keywords = ('crib', 'with', 'mobile', 'baby', 'nursery', 'toy')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('crib-1', (6, 42), (6, 30))
        self.add_line('crib-2', (6, 30), (42, 30))
        self.add_line('crib-3', (42, 30), (42, 42))
        self.add_line('rail', (6, 38), (42, 38))
        self.add_line('slat-18', (18, 30), (18, 38))
        self.add_line('slat-30', (30, 30), (30, 38))
        self.add_line('mobile-1', (10, 15), (10, 6))
        self.add_line('mobile-2', (10, 6), (38, 6))
        self.add_line('mobile-3', (38, 6), (38, 15))
        self.add_line('middle', (24, 6), (24, 15))
        self.add_arc('toy-10-top', (7, 18), (13, 18), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('toy-10-bottom', (13, 18), (7, 18), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('toy-24-top', (21, 18), (27, 18), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('toy-24-bottom', (27, 18), (21, 18), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('toy-38-top', (35, 18), (41, 18), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('toy-38-bottom', (41, 18), (35, 18), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('crib', *('crib-1', 'crib-2', 'crib-3'), closed=False)
        self.add_contour('mobile', *('mobile-1', 'mobile-2', 'mobile-3'), closed=False)
        self.add_contour('toy-10', *('toy-10-top', 'toy-10-bottom'), closed=True)
        self.add_contour('toy-24', *('toy-24-top', 'toy-24-bottom'), closed=True)
        self.add_contour('toy-38', *('toy-38-top', 'toy-38-bottom'), closed=True)
        self.relate('connect', *('rail', 'crib'))
        self.relate('connect', *('slat-18', 'crib'))
        self.relate('connect', *('slat-18', 'rail'))
        self.relate('connect', *('slat-30', 'crib'))
        self.relate('connect', *('slat-30', 'rail'))
        self.relate('connect', *('mobile', 'middle'))
        self.relate('connect', *('toy-10', 'mobile'))
        self.relate('connect', *('toy-24', 'middle'))
        self.relate('connect', *('toy-38', 'mobile'))
