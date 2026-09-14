# Review candidate; original preserved.
"""Three nested semicircular rainbow bands bridge the gap between two clouds at the lower corners. The clouds face inward with rounded lobes and level lower edges.

Two rainbow bands meet clouds with separate crowns, side lobes, and flat bases; third rainbow band omitted.
Construction reference: Lucide cloud: clean small lobes; concentric rainbow arcs with shared center.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '41049662-f336-4650-9604-e8d4818347cc'
SOURCE_PATH = 'pictographic-primitives/weather/weather clouds rainbow_41049662-f336-4650-9604-e8d4818347cc.svg'
AUTHOR = 'gpt-6'

class RainbowBetweenClouds(Solo48):
    icon_id = 'rainbow-between-clouds'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/weather'
    aliases = ()
    keywords = ('rainbow', 'cloud', 'sky', 'weather', 'arc', 'sunlight')

    def build(self) -> None:
        """Opening repair: Made both rainbow arcs share a centred ellipse construction so their crowns no longer cross."""
        self.add_arc('rainbow-outer', (6, 34), (42, 34), sweep=True, large_arc=False, radius_x=18, radius_y=26)
        self.add_arc('rainbow-inner', (16, 34), (32, 34), sweep=True, large_arc=False, radius_x=8, radius_y=16)
        self.add_arc('left-crown-left', (6, 34), (10, 28), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('left-crown-right', (10, 28), (16, 34), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('left-lobe', (16, 34), (16, 40), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('left-base', (16, 40), (7, 40))
        self.add_arc('left-corner', (7, 40), (6, 37), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('left-side', (6, 37), (6, 34))
        self.add_contour('left', 'left-crown-left', 'left-crown-right', 'left-lobe', 'left-base', 'left-corner', 'left-side', closed=True)
        self.relate('connect', 'left', 'rainbow-outer')
        self.relate('connect', 'left', 'rainbow-inner')
        self.add_arc('right-crown-left', (42, 34), (38, 28), radius_x=6, radius_y=6, sweep=False, large_arc=False)
        self.add_arc('right-crown-right', (38, 28), (32, 34), radius_x=6, radius_y=6, sweep=False, large_arc=False)
        self.add_arc('right-lobe', (32, 34), (32, 40), radius_x=3, radius_y=3, sweep=False, large_arc=False)
        self.add_line('right-base', (32, 40), (41, 40))
        self.add_arc('right-corner', (41, 40), (42, 37), radius_x=3, radius_y=3, sweep=False, large_arc=False)
        self.add_line('right-side', (42, 37), (42, 34))
        self.add_contour('right', 'right-crown-left', 'right-crown-right', 'right-lobe', 'right-base', 'right-corner', 'right-side', closed=True)
        self.relate('connect', 'right', 'rainbow-outer')
        self.relate('connect', 'right', 'rainbow-inner')
