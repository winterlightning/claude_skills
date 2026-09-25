"""Restored a large open curling wave behind the house and an explicit waterline; removed the crescent-like closed outline. Small window omitted.

Construction: Supplied weather reference: open crest, inward curl and waterline. No useful local Lucide wave match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dd42d4e7-bf58-44a9-babb-9b0772ecce14'
SOURCE_PATH = 'pictographic-primitives/weather/flood house wave_dd42d4e7-bf58-44a9-babb-9b0772ecce14.svg'
AUTHOR = 'gpt-6'

class WaveBehindHouse(Solo48):
    icon_id = 'wave-behind-house'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    aliases = ()
    keywords = ('flood', 'house', 'wave', 'tsunami', 'water', 'disaster')

    def build(self) -> None:
        self.add_line('crest', (20, 6), (26, 6))
        self.add_arc('outer-face', (26, 6), (42, 29), radius_x=16, radius_y=23, sweep=True, large_arc=False)
        self.add_contour('outer', 'crest', 'outer-face', closed=False)
        self.add_arc('inner-upper', (20, 6), (32, 18), radius_x=12, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('inner-lower', (32, 18), (26, 29), radius_x=6, radius_y=11, sweep=True, large_arc=False)
        self.add_contour('inner', 'inner-upper', 'inner-lower', closed=False)
        self.relate("connect", 'outer', 'inner')
        self.add_polyline('house', (6, 27), (6, 21), (12, 15), (18, 21), (18, 27), closed=True)
        self.add_arc('surface-left', (18, 27), (26, 29), radius_x=9, radius_y=9, sweep=True, large_arc=False)
        self.add_arc('surface-right', (26, 29), (42, 29), radius_x=15, radius_y=15, sweep=False, large_arc=False)
        self.add_contour('surface', 'surface-left', 'surface-right', closed=False)
        self.relate("connect", 'inner', 'surface')
        self.relate("connect", 'outer', 'surface')
        self.relate("connect", 'house', 'surface')
        self.add_arc('water-left', (6, 39), (24, 39), radius_x=15, radius_y=15, sweep=True, large_arc=False)
        self.add_arc('water-right', (24, 39), (42, 39), radius_x=15, radius_y=15, sweep=False, large_arc=False)
        self.add_contour('water', 'water-left', 'water-right', closed=False)
