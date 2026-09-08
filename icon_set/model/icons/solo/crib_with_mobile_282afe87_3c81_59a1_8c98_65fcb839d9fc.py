"""Crib with three suspended toys; Lucide bed informs rails and upright joins. Teardrops reduced to round beads."""
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
    category = "objects/baby"
    aliases = ()
    keywords = ('crib', 'with', 'mobile', 'baby', 'nursery', 'toy')

    def build(self) -> None:
        # Centerline keyshape: SQUARE; Crib with three suspended toys; Lucide bed informs rails and upright joins. Teardrops reduced to round beads.
        self.add_polyline('left-post', (2, 23), (2, 28), (2, 40), (2, 46), closed=False)
        self.add_polyline('right-post', (46, 23), (46, 28), (46, 40), (46, 46), closed=False)
        self.add_polyline('top-rail', (2, 28), (13, 28), (24, 28), (35, 28), (46, 28), closed=False)
        self.relate("connect", 'top-rail', 'left-post')
        self.relate("connect", 'top-rail', 'right-post')
        self.add_polyline('bottom-rail', (2, 40), (13, 40), (24, 40), (35, 40), (46, 40), closed=False)
        self.relate("connect", 'bottom-rail', 'left-post')
        self.relate("connect", 'bottom-rail', 'right-post')
        self.add_line('slat-13', (13, 28), (13, 40))
        self.relate("connect", 'slat-13', 'top-rail')
        self.relate("connect", 'slat-13', 'bottom-rail')
        self.add_line('slat-24', (24, 28), (24, 40))
        self.relate("connect", 'slat-24', 'top-rail')
        self.relate("connect", 'slat-24', 'bottom-rail')
        self.add_line('slat-35', (35, 28), (35, 40))
        self.relate("connect", 'slat-35', 'top-rail')
        self.relate("connect", 'slat-35', 'bottom-rail')
        self.add_polyline('mobile-bar', (10, 8), (24, 8), (38, 8), closed=False)
        self.add_line('hanger', (24, 2), (24, 8))
        self.relate("connect", 'hanger', 'mobile-bar')
        self.add_line('toy-10-thread', (10, 8), (10, 15))
        self.add_arc('toy-10-a', (10, 15), (10, 21), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('toy-10-b', (10, 21), (10, 15), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('toy-10', 'toy-10-a', 'toy-10-b', closed=True)
        self.relate("connect", 'toy-10-thread', 'mobile-bar')
        self.relate("connect", 'toy-10-thread', 'toy-10')
        self.add_line('toy-24-thread', (24, 8), (24, 15))
        self.add_arc('toy-24-a', (24, 15), (24, 21), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('toy-24-b', (24, 21), (24, 15), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('toy-24', 'toy-24-a', 'toy-24-b', closed=True)
        self.relate("connect", 'toy-24-thread', 'mobile-bar')
        self.relate("connect", 'toy-24-thread', 'toy-24')
        self.add_line('toy-38-thread', (38, 8), (38, 15))
        self.add_arc('toy-38-a', (38, 15), (38, 21), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('toy-38-b', (38, 21), (38, 15), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('toy-38', 'toy-38-a', 'toy-38-b', closed=True)
        self.relate("connect", 'toy-38-thread', 'mobile-bar')
        self.relate("connect", 'toy-38-thread', 'toy-38')
