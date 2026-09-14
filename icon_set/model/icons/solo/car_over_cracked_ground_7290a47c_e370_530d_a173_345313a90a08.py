"""A side-view car with two wheels and divided windows tilts slightly over a horizontal road. The ground drops into a deep central fissure, with two angular tremor marks underneath.

Kept car roof and wheels over one ground fissure; dropped window division and extra tremor marks.
Construction reference: No useful exact local match; geometric car silhouette and paired circular wheels.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7290a47c-e370-530d-a173-345313a90a08'
SOURCE_PATH = 'pictographic-primitives/weather/earthquake car shaking_7290a47c-e370-530d-a173-345313a90a08.svg'
AUTHOR = 'gpt-6'

class CarOverCrackedGround(Solo48):
    icon_id = 'car-over-cracked-ground'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weather"
    aliases = ()
    keywords = ('car', 'earthquake', 'crack', 'road', 'tremor', 'disaster')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_polyline('car-top', (6, 22), (6, 16), (12, 16), (17, 8), (31, 8), (37, 16), (42, 16), (42, 22), closed=False)
        self.add_line('body-base', (6, 22), (13, 22))
        self.add_line('body-mid', (13, 22), (35, 22))
        self.add_line('body-end', (35, 22), (42, 22))
        self.add_contour('body', 'body-base', 'body-mid', 'body-end', closed=False)
        self.relate("connect", 'car-top', 'body')
        self.add_arc('left-wheel-a', (13, 22), (13, 28), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('left-wheel-b', (13, 28), (13, 22), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('left-wheel', 'left-wheel-a', 'left-wheel-b', closed=True)
        self.relate("connect", 'body', 'left-wheel')
        self.add_arc('right-wheel-a', (35, 22), (35, 28), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('right-wheel-b', (35, 28), (35, 22), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('right-wheel', 'right-wheel-a', 'right-wheel-b', closed=True)
        self.relate("connect", 'body', 'right-wheel')
        self.add_polyline('ground', (6, 37), (18, 37), (24, 40), (30, 37), (42, 37), closed=False)
