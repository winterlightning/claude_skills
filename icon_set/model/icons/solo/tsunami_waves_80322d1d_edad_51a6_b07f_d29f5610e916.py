"""A tall curling wave rises at the left behind a smaller curling wave on the right. Their crests turn inward, and separate undulating lower edges spread across the base.

Retained two separate inward curling crests of unequal height; removed foam fragments and secondary waterlines.
Construction reference: No useful exact local wave match; coherent circular crest and broad elliptical trough.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '80322d1d-edad-51a6-b07f-d29f5610e916'
SOURCE_PATH = 'pictographic-primitives/weather/tsunami waves_80322d1d-edad-51a6-b07f-d29f5610e916.svg'
AUTHOR = 'gpt-6'

class TsunamiWaves(Solo48):
    icon_id = 'tsunami-waves'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weather"
    aliases = ()
    keywords = ('tsunami', 'wave', 'sea', 'water', 'disaster', 'swell')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_line('rear-base', (26, 36), (10, 36))
        self.add_arc('rear-inner-lower', (10, 36), (14, 30), radius_x=4, radius_y=6, sweep=False, large_arc=False)
        self.add_arc('rear-inner-upper', (14, 30), (6, 20), radius_x=10, radius_y=10, sweep=False, large_arc=False)
        self.add_arc('rear-outer', (6, 20), (34, 20), radius_x=15, radius_y=12, sweep=True, large_arc=False)
        self.add_contour('rear-wave', 'rear-base', 'rear-inner-lower', 'rear-inner-upper', 'rear-outer', closed=False)
        self.add_arc('front-outer-left', (24, 28), (34, 20), radius_x=10, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('front-outer-right', (34, 20), (42, 28), radius_x=10, radius_y=8, sweep=True, large_arc=False)
        self.add_line('front-fall', (42, 28), (42, 34))
        self.add_arc('front-trough-right', (42, 34), (36, 40), radius_x=8, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('front-trough-left', (36, 40), (26, 36), radius_x=10, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('front-inner-lower', (26, 36), (32, 32), radius_x=6, radius_y=4, sweep=False, large_arc=False)
        self.add_arc('front-inner-upper', (32, 32), (24, 28), radius_x=8, radius_y=4, sweep=False, large_arc=False)
        self.add_contour('front-wave', 'front-outer-left', 'front-outer-right', 'front-fall', 'front-trough-right', 'front-trough-left', 'front-inner-lower', 'front-inner-upper', closed=True)
        self.relate("connect", 'front-wave', 'rear-wave')
