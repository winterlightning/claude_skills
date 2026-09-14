# Variant of wave-behind-house; parent file remains unchanged.
"""Restored a large open curling wave behind the house and an explicit waterline; removed the crescent-like closed outline. Small window omitted.

Construction: Supplied weather reference: open crest, inward curl and waterline. No useful local Lucide wave match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dd42d4e7-bf58-44a9-babb-9b0772ecce14'
SOURCE_PATH = 'pictographic-primitives/weather/flood house wave_dd42d4e7-bf58-44a9-babb-9b0772ecce14.svg'
AUTHOR = 'gpt-6'

class WaveBehindHouseVariant2(Solo48):
    icon_id = 'wave-behind-house-v2'
    variant_of = 'wave-behind-house'
    variant_label = 'Restore recognizable weather geometry'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/weather'
    aliases = ()
    keywords = ('flood', 'house', 'wave', 'tsunami', 'water', 'disaster')

    def build(self) -> None:
        self.add_polyline('house', (6, 40), (6, 29), (10, 23), (16, 29), (16, 40), closed=True)
        self.add_line('face', (42, 29), (42, 20))
        self.add_arc('crest', (42, 20), (20, 20), radius_x=12, radius_y=12, sweep=False, large_arc=False)
        self.add_arc('curl', (20, 20), (32, 20), radius_x=6, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('wash', (32, 20), (26, 26), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_contour('breaking-wave', 'face', 'crest', 'curl', 'wash', closed=False)
        self.add_line('water', (16, 40), (42, 40))
        self.relate("connect", 'house', 'water')
