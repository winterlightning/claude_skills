"""Nursery mobile with unequal threads, circle, crescent and triangle."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '98dc90c1-4206-5d40-b53b-07eca24686a7'
SOURCE_PATH = 'pictographic-primitives/babies/baby care cot mobile_98dc90c1-4206-5d40-b53b-07eca24686a7.svg'
AUTHOR = 'gpt-6'


class CribMobile(Solo48):
    icon_id = 'crib-mobile'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/baby"
    aliases = ()
    keywords = ('crib', 'mobile', 'baby', 'nursery', 'toy')

    def build(self) -> None:
        # Centerline keyshape: HRECT_L; Nursery mobile with unequal threads, circle, crescent and triangle.
        self.add_polyline('bar', (2, 8), (9, 8), (25, 8), (39, 8), (46, 8), closed=False)
        self.add_line('left-thread', (9, 8), (9, 20))
        self.add_arc('ball-a', (9, 20), (9, 30), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('ball-b', (9, 30), (9, 20), radius_x=5, radius_y=5, sweep=True)
        self.add_contour('ball', 'ball-a', 'ball-b', closed=True)
        self.relate("connect", 'left-thread', 'bar')
        self.relate("connect", 'left-thread', 'ball')
        self.add_line('middle-thread', (25, 8), (25, 24))
        self.add_arc('moon-outer', (25, 24), (25, 40), radius_x=8, radius_y=8, sweep=False)
        self.add_arc('moon-inner', (25, 40), (25, 24), radius_x=30, radius_y=30, sweep=True)
        self.add_contour('moon', 'moon-outer', 'moon-inner', closed=True)
        self.relate("connect", 'middle-thread', 'bar')
        self.relate("connect", 'middle-thread', 'moon')
        self.add_line('right-thread', (39, 8), (39, 21))
        self.add_polyline('triangle', (39, 21), (46, 33), (32, 33), closed=True)
        self.relate("connect", 'right-thread', 'bar')
        self.relate("connect", 'right-thread', 'triangle')
