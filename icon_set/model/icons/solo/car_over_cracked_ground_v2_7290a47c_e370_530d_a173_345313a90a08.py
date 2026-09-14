# Variant of car-over-cracked-ground; parent file remains unchanged.
"""A side-view car with two wheels and divided windows tilts slightly over a horizontal road. The ground drops into a deep central fissure, with two angular tremor marks underneath.

Kept car roof and wheels over one ground fissure; dropped window division and extra tremor marks.
Construction reference: No useful exact local match; geometric car silhouette and paired circular wheels.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7290a47c-e370-530d-a173-345313a90a08'
SOURCE_PATH = 'pictographic-primitives/weather/earthquake car shaking_7290a47c-e370-530d-a173-345313a90a08.svg'
AUTHOR = 'gpt-6'

class CarOverCrackedGroundVariant2(Solo48):
    icon_id = 'car-over-cracked-ground-v2'
    variant_of = 'car-over-cracked-ground'
    variant_label = 'Roomier spacing — review 02'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/weather'
    aliases = ()
    keywords = ('car', 'earthquake', 'crack', 'road', 'tremor', 'disaster')

    def build(self) -> None:
        self.add_polyline('car-top', (4, 20), (4, 12), (12, 12), (17, 8), (31, 8), (37, 12), (44, 12), (44, 20), closed=False)
        self.add_line('body-base', (4, 20), (13, 20))
        self.add_line('body-mid', (13, 20), (35, 20))
        self.add_line('body-end', (35, 20), (44, 20))
        self.add_contour('body', 'body-base', 'body-mid', 'body-end', closed=False)
        self.relate('connect', 'car-top', 'body')
        self.add_arc('left-wheel-a', (13, 20), (13, 28), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('left-wheel-b', (13, 28), (13, 20), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('left-wheel', 'left-wheel-a', 'left-wheel-b', closed=True)
        self.relate('connect', 'body', 'left-wheel')
        self.add_arc('right-wheel-a', (35, 20), (35, 28), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('right-wheel-b', (35, 28), (35, 20), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('right-wheel', 'right-wheel-a', 'right-wheel-b', closed=True)
        self.relate('connect', 'body', 'right-wheel')
        self.add_polyline('ground', (4, 37), (18, 37), (24, 40), (30, 37), (44, 37), closed=False)
