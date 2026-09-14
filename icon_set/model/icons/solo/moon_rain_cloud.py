# Review candidate; original preserved.
"""A crescent moon rises behind the upper-right side of an open-bottom cloud. Three parallel diagonal rain strokes fall toward the lower left beneath the foreground cloud.

Reduced secondary lobes and rain count; preserved rightward crescent behind a lower-left cloud.
Construction reference: Lucide moon and cloud: coherent overlapping silhouettes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '93e91edf-3294-4be6-b0ea-84ff55057f87'
SOURCE_PATH = 'pictographic-primitives/weather/weather night rain_93e91edf-3294-4be6-b0ea-84ff55057f87.svg'
AUTHOR = 'gpt-6'

class MoonRainCloud(Solo48):
    icon_id = 'moon-rain-cloud'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/weather'
    aliases = ()
    keywords = ('moon', 'rain', 'cloud', 'night', 'shower', 'weather')

    def build(self) -> None:
        """Opening repair: Broadened the crescent by rebalancing its inner and outer curves."""
        self.add_arc('cloud-dome', (16, 30), (28, 22), radius_x=12, radius_y=8, sweep=True, large_arc=True)
        self.add_arc('cloud-right-upper', (28, 22), (36, 26), radius_x=8, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('cloud-right-lower', (36, 26), (28, 30), radius_x=8, radius_y=4, sweep=True, large_arc=False)
        self.add_line('cloud-base', (28, 30), (16, 30))
        self.add_contour('cloud', 'cloud-dome', 'cloud-right-upper', 'cloud-right-lower', 'cloud-base', closed=True)
        self.add_arc('moon-outer', (28, 22), (42, 8), sweep=True, large_arc=False, radius_x=10, radius_y=12)
        self.add_arc('moon-inner', (42, 8), (42, 30), sweep=False, large_arc=False, radius_x=5, radius_y=11)
        self.add_line('moon-tip', (42, 30), (36, 26))
        self.add_contour('moon', 'moon-outer', 'moon-inner', 'moon-tip', closed=False)
        self.relate('connect', 'moon', 'cloud')
        self.add_line('rain-left', (16, 39), (15, 40))
        self.add_line('rain-right', (29, 39), (28, 40))
