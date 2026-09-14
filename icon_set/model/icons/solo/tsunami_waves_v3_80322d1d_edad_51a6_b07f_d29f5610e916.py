# Variant of tsunami-waves-v2; parent file remains unchanged.
"""Restored two open curling crests of different heights over a waterline, instead of two closed rounded shells.

Construction: Supplied weather reference: open crest, inward curl and waterline. No useful local Lucide wave match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '80322d1d-edad-51a6-b07f-d29f5610e916'
SOURCE_PATH = 'pictographic-primitives/weather/tsunami waves_80322d1d-edad-51a6-b07f-d29f5610e916.svg'
AUTHOR = 'gpt-6'

class TsunamiWavesVariant3(Solo48):
    icon_id = 'tsunami-waves-v3'
    variant_of = 'tsunami-waves-v2'
    variant_label = 'Restore recognizable weather geometry'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/weather'
    aliases = ()
    keywords = ('tsunami', 'wave', 'sea', 'water', 'disaster', 'swell')

    def build(self) -> None:
        self.add_line('rear-base', (6, 30), (8, 20))
        self.add_arc('rear-rise', (8, 20), (22, 6), radius_x=14, radius_y=14, sweep=True, large_arc=False)
        self.add_arc('rear-crest', (22, 6), (32, 16), radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_contour('rear-outer', 'rear-base', 'rear-rise', 'rear-crest', closed=False)
        self.add_arc('rear-lip', (32, 16), (20, 20), radius_x=7, radius_y=7, sweep=False, large_arc=False)
        self.add_arc('rear-face', (20, 20), (24, 30), radius_x=10, radius_y=10, sweep=False, large_arc=False)
        self.add_contour('rear-inner', 'rear-lip', 'rear-face', closed=False)
        self.relate("connect", 'rear-outer', 'rear-inner')
        self.add_arc('front-rise', (24, 30), (34, 22), radius_x=10, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('front-crest', (34, 22), (42, 26), radius_x=8, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('front-hollow', (42, 26), (34, 34), radius_x=8, radius_y=8, sweep=False, large_arc=False)
        self.add_arc('front-face', (34, 34), (42, 42), radius_x=8, radius_y=8, sweep=False, large_arc=False)
        self.add_contour('front', 'front-rise', 'front-crest', 'front-hollow', 'front-face', closed=False)
        self.relate("connect", 'rear-inner', 'front')
        self.add_arc('water-left', (6, 40), (14, 38), radius_x=8, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('water-right', (14, 38), (24, 30), radius_x=10, radius_y=8, sweep=False, large_arc=False)
        self.add_contour('water', 'water-left', 'water-right', closed=False)
        self.relate("connect", 'water', 'rear-inner')
        self.relate("connect", 'water', 'front')
