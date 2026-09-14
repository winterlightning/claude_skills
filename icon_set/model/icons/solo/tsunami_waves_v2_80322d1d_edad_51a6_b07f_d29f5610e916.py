# Variant of tsunami-waves; parent file remains unchanged.
"""Restored two open curling crests of different heights over a waterline, instead of two closed rounded shells.

Construction: Supplied weather reference: open crest, inward curl and waterline. No useful local Lucide wave match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '80322d1d-edad-51a6-b07f-d29f5610e916'
SOURCE_PATH = 'pictographic-primitives/weather/tsunami waves_80322d1d-edad-51a6-b07f-d29f5610e916.svg'
AUTHOR = 'gpt-6'

class TsunamiWavesVariant2(Solo48):
    icon_id = 'tsunami-waves-v2'
    variant_of = 'tsunami-waves'
    variant_label = 'Restore recognizable weather geometry'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/weather'
    aliases = ()
    keywords = ('tsunami', 'wave', 'sea', 'water', 'disaster', 'swell')

    def build(self) -> None:
        self.add_line('rear-face', (6, 30), (6, 20))
        self.add_arc('rear-crest', (6, 20), (32, 20), radius_x=14, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('rear-curl', (32, 20), (20, 20), radius_x=6, radius_y=2, sweep=False, large_arc=False)
        self.add_arc('rear-wash', (20, 20), (26, 26), radius_x=6, radius_y=6, sweep=False, large_arc=False)
        self.add_contour('rear-wave', 'rear-face', 'rear-crest', 'rear-curl', 'rear-wash', closed=False)
        self.add_arc('front-crest', (26, 26), (42, 34), radius_x=18, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('front-curl', (42, 34), (34, 34), radius_x=5, radius_y=2, sweep=False, large_arc=False)
        self.add_arc('front-wash', (34, 34), (40, 40), radius_x=6, radius_y=6, sweep=False, large_arc=False)
        self.add_contour('front-wave', 'front-crest', 'front-curl', 'front-wash', closed=False)
        self.relate("connect", 'rear-wave', 'front-wave')
        self.add_line('water', (6, 40), (24, 40))
